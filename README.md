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

## Daily insight

The homepage “Today’s insight” section is driven by markdown files in `_insights/` and the active slug in `_data/active_insight.yml`. A GitHub Actions cron (`.github/workflows/update-daily-insight.yml`) rotates the slug once per day (00:00 UTC).

### Add an insight

1. Add `_insights/<slug>.md` with optional `attribution` front matter and the insight body.
2. The next cron run (or a manual workflow dispatch) will include it in the rotation.

### Force today’s insight

Edit `_data/active_insight.yml` and set `slug` to the basename of the desired file (without `.md`).
