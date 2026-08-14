#!/usr/bin/env python3
"""Advance the homepage insight to the next `order` and write `_data/active_insight.yml`."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INSIGHTS_DIR = ROOT / "_insights"
OUT = ROOT / "_data" / "active_insight.yml"


@dataclass(frozen=True, order=True)
class Insight:
    order: int
    slug: str


def get_insights(insights_dir: Path = INSIGHTS_DIR) -> list[Insight]:
    return [parse_insight(path) for path in insights_dir.glob("*.md")]


def parse_insight(path: Path) -> Insight:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path.name} has no YAML front matter")

    front_matter_end = text.find("\n---", 3)
    if front_matter_end == -1:
        raise ValueError(f"{path.name} has unclosed YAML front matter")

    order: int | None = None
    for raw in text[3:front_matter_end].splitlines():
        line = raw.strip()
        if not line.startswith("order:"):
            continue
        value = line.split(":", 1)[1].strip()
        try:
            order = int(value)
        except ValueError as exc:
            raise ValueError(f"{path.name} has a non-integer order: {value!r}") from exc
        break

    if order is None:
        raise ValueError(f"{path.name} is missing an `order` front-matter field")
    return Insight(order=order, slug=path.stem)


def read_active_slug(path: Path = OUT) -> str | None:
    if not path.exists():
        return None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("slug:"):
            return line.split(":", 1)[1].strip() or None
    return None


def pick_next_insight(insights: list[Insight], current_slug: str | None) -> Insight:
    current = next((insight for insight in insights if insight.slug == current_slug), None)
    if current is None:
        return min(insights)

    higher = [insight for insight in insights if insight > current]
    return min(higher) if higher else min(insights)


def build_active_insight_yaml(slug: str) -> str:
    return (
        "# Slug of the insight shown on the homepage (basename of _insights/<slug>.md).\n"
        "# Updated weekly by .github/workflows/update-weekly-insight.yml\n"
        f"slug: {slug}\n"
    )


def main() -> int:
    try:
        insights = get_insights()
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    if not insights:
        print(f"No insight markdown files found in {INSIGHTS_DIR}", file=sys.stderr)
        return 1

    slug = pick_next_insight(insights, read_active_slug()).slug
    content = build_active_insight_yaml(slug)

    if OUT.exists() and OUT.read_text(encoding="utf-8") == content:
        print(f"Active insight already {slug!r}; no write needed.")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote active insight slug: {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
