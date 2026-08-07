#!/usr/bin/env python3
"""Pick today's insight slug (UTC day modulo) and write _data/active_insight.yml."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INSIGHTS_DIR = ROOT / "_insights"
OUT = ROOT / "_data" / "active_insight.yml"


def insight_slugs() -> list[str]:
    files = sorted(INSIGHTS_DIR.glob("*.md"))
    return [f.stem for f in files]


def utc_day_index() -> int:
    now = datetime.now(timezone.utc)
    return int(now.timestamp() // 86400)


def main() -> int:
    slugs = insight_slugs()
    if not slugs:
        print(f"No insight markdown files found in {INSIGHTS_DIR}", file=sys.stderr)
        return 1

    slug = slugs[utc_day_index() % len(slugs)]
    content = (
        "# Slug of the insight shown on the homepage (basename of _insights/<slug>.md).\n"
        "# Updated daily by .github/workflows/update-daily-insight.yml\n"
        f"slug: {slug}\n"
    )

    if OUT.exists() and OUT.read_text(encoding="utf-8") == content:
        print(f"Active insight already {slug!r}; no write needed.")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote active insight slug: {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
