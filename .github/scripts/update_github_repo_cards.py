#!/usr/bin/env python3
"""Write _data/github_repo_cards.json from GitHub pinned repos (GraphQL) or github_repos (REST)."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_data" / "github_repo_cards.json"
REPOS_YML = ROOT / "_data" / "repositories.yml"


def graphql(query: str, variables: dict, token: str) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.github+json",
        "User-Agent": "kutayeroglu.github.io-repo-cards",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request("https://api.github.com/graphql", data=body, headers=headers, method="POST")
    with urlopen(req) as r:
        return json.loads(r.read().decode())


def rest_repo(full_name: str, token: str) -> dict:
    url = f"https://api.github.com/repos/{full_name}"
    headers = {
        "User-Agent": "kutayeroglu.github.io-repo-cards",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    with urlopen(req) as r:
        return json.loads(r.read().decode())


def normalize_rest(d: dict) -> dict:
    return {
        "name": d["name"],
        "owner": d["owner"]["login"],
        "full_name": d["full_name"],
        "description": (d.get("description") or "")[:500],
        "html_url": d["html_url"],
        "stargazers_count": d["stargazers_count"],
        "forks_count": d["forks_count"],
        "language": d.get("language"),
        "language_color": None,
    }


def normalize_graphql(node: dict) -> dict:
    owner = node["owner"]["login"]
    name = node["name"]
    lang = node.get("primaryLanguage") or {}
    return {
        "name": name,
        "owner": owner,
        "full_name": f"{owner}/{name}",
        "description": (node.get("description") or "")[:500],
        "html_url": node["url"],
        "stargazers_count": node["stargazerCount"],
        "forks_count": node["forkCount"],
        "language": lang.get("name"),
        "language_color": lang.get("color"),
    }


def fetch_pinned(cfg: dict, token: str, max_repos: int) -> list[dict]:
    users = cfg.get("github_users") or []
    if not users:
        print("github_repo_cards.source=pinned requires github_users in _data/repositories.yml", file=sys.stderr)
        return []
    login = users[0]
    q = """
    query($login: String!) {
      user(login: $login) {
        pinnedItems(first: 6, types: REPOSITORY) {
          nodes {
            ... on Repository {
              name
              owner { login }
              description
              stargazerCount
              forkCount
              url
              primaryLanguage { name color }
            }
          }
        }
      }
    }
    """
    data = graphql(q, {"login": login}, token)
    if data.get("errors"):
        print(json.dumps(data["errors"], indent=2), file=sys.stderr)
        return []
    user = data.get("data", {}).get("user")
    if not user:
        print("GraphQL: user not found", file=sys.stderr)
        return []
    out: list[dict] = []
    for node in user.get("pinnedItems", {}).get("nodes") or []:
        if not node:
            continue
        out.append(normalize_graphql(node))
        if len(out) >= max_repos:
            break
    return out


def fetch_manual(cfg: dict, token: str, max_repos: int) -> list[dict]:
    names = cfg.get("github_repos") or []
    out: list[dict] = []
    for full in names[:max_repos]:
        full = str(full).strip()
        if not full:
            continue
        try:
            d = rest_repo(full, token)
            out.append(normalize_rest(d))
        except HTTPError as e:
            print(f"Warning: could not fetch {full}: {e}", file=sys.stderr)
    return out


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN", "")
    cfg = yaml.safe_load(REPOS_YML.read_text())
    cards_cfg = cfg.get("github_repo_cards") or {}
    source = (cards_cfg.get("source") or "pinned").strip().lower()
    max_repos = int(cards_cfg.get("max_repos", 6))

    meta_source = source
    repos_out: list[dict] = []

    if source == "pinned":
        repos_out = fetch_pinned(cfg, token, max_repos)
        if not repos_out:
            print("No pinned repositories (or fetch failed); using github_repos list.", file=sys.stderr)
            meta_source = "manual"
            repos_out = fetch_manual(cfg, token, max_repos)
    else:
        repos_out = fetch_manual(cfg, token, max_repos)

    payload = {
        "meta": {
            "source": meta_source,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        },
        "repositories": repos_out,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"Wrote {len(repos_out)} repos to {OUT} (meta.source={meta_source})")


if __name__ == "__main__":
    main()
