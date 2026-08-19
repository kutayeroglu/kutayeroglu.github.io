---
name: al-folio-config-first
description: >-
  Customizes this al-folio site via config, data, and content first, then
  additive theme changes only when nothing existing covers the feature. Use
  when adding pages, socials, features, layout tweaks, or any site change, and
  before modifying _layouts, _includes, or _sass.
---

# al-folio config-first

This site is an al-folio theme. Prefer owner-layer edits. Do not patch theme
code when a flag, data file, or front matter already does the job.

Search first; extend only when the theme cannot express the feature.

## Decision order

1. `_config.yml` — feature flags (`enable_*`, search, analytics, exclude)
2. `_data/` — socials, CV, and other structured content
3. Content folders — `_pages/`, `_news/`, `_insights/`, `_bibliography/`, `assets/`
4. Page front matter — per-page on/off (`social`, `announcements`, `weekly_insight`)
5. `_layouts/`, `_includes/`, `_sass/` — only if steps 1–4 cannot express the behavior

Check `_config.yml`, `CUSTOMIZE.md`, and nearby front matter before touching
layouts.

## Prefer

| Goal | Edit |
| --- | --- |
| Toggle a built-in feature | `_config.yml` |
| Add/reorder social links | `_data/socials.yml` |
| Show/hide a page section | that page's front matter |
| Add news, insights, papers | `_news/`, `_insights/`, `_bibliography/` |
| Hide template files | `exclude:` in `_config.yml` (do not delete) |

## When nothing existing covers it

If `_config.yml`, `_data/`, front matter, and `CUSTOMIZE.md` cannot do the job,
theme edits are allowed. Do not stop at "the theme has no flag for this."

Before editing `_layouts/`, `_includes/`, or `_sass/`:

1. State what you searched and why config/data are insufficient
2. Prefer an additive, config-driven extension (new flag, data file, or include)
   over a one-off markup change
3. Keep the new path reusable — later similar requests should be a config/data
   edit, not another layout patch
4. Do not duplicate existing theme behavior under a new name

Use the smallest additive change. Pause only if the work would rewrite a core
layout when a smaller include or partial would do.

## Avoid

- Conditionals in `_layouts/` or `_includes/` that duplicate an existing flag
- Copying theme markup into a page to restyle one section
- Deleting template files instead of excluding them

## Examples

**Social icons in the navbar (covered):** `enable_navbar_social: true` in
`_config.yml`. Set `social: false` in `_pages/about.md` to drop the bottom row.
Do not fork `_layouts/about.liquid` for this.

**Add GitHub (covered):** set `github_username` in `_data/socials.yml`.

**Weekly homepage insight (not covered):** add `_insights/` content plus a
small include and a config/front-matter switch so later insights are data,
not more layout code.
