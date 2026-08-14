# Personal webpage

This is my personal website, built with [al-folio](https://github.com/alshedivat/al-folio), a Jekyll theme for academics.

## Running locally
Just run:
```
docker compose up
```
Then open http://localhost:8080

## Arts gallery

The `/arts/` page is driven by `_data/arts.yml` and image files in `assets/img/arts/`.

### Add an image

1. Put the image in `assets/img/arts/` (e.g. `my-sketch.jpg`).
2. Add an entry in `_data/arts.yml`:

```yaml
- title: My Sketch
  image: assets/img/arts/my-sketch.jpg
  alt: Short description for accessibility
  caption: Optional text shown in the lightbox
  date: 12-06-26
  width: 1200
  height: 900
  class: span-6 tall
```

`date` is shown on the card (e.g. `DD-MM-YY`).  
`width` / `height` should match the real pixel size (PhotoSwipe needs them).  
`class` controls layout: `span-6` / `span-3` / `span-4`, plus optional `tall` or `short`.

### Remove an image

1. Delete that entry from `_data/arts.yml`.
2. Optionally delete the file under `assets/img/arts/`.

## Weekly insight

The homepage “This week’s insight” section is driven by markdown files in `_insights/` and the active slug in `_data/active_insight.yml`. A GitHub Actions cron (`.github/workflows/update-weekly-insight.yml`) advances to the next insight once per week (Monday 00:00 UTC).

Rotation follows each file’s `order` front matter (lowest first). Equal `order` values break ties alphabetically by slug. After the highest `order`, it wraps to the lowest. Each successful job run advances one step, including a manual workflow dispatch.

### Add an insight

1. Add `_insights/<slug>.md` with an integer `order`, optional `attribution`, and the insight body.
2. The next cron run (or a manual workflow dispatch) will include it in the sequence.

### Force this week’s insight

Edit `_data/active_insight.yml` and set `slug` to the basename of the desired file (without `.md`). The following job run will advance from that slug.
