---
layout: page
permalink: /arts/
title: arts
description: A small selection of sketches and drawings. Click any image to enlarge.
nav: false
images:
  photoswipe: true
---

These are personal sketches—quick studies and playful ideas.

<div class="arts-gallery pswp-gallery" aria-label="Art gallery">
{% for art in site.data.arts %}
  <a
    class="arts-card {{ art.class }}"
    href="{{ art.image | relative_url }}"
    data-pswp-width="{{ art.width }}"
    data-pswp-height="{{ art.height }}"
    data-pswp-caption="{{ art.caption | escape }}"
    target="_blank"
    rel="noreferrer"
  >
    <img src="{{ art.image | relative_url }}" alt="{{ art.alt | escape }}" loading="lazy">
    <span class="arts-meta">
      <span class="arts-title">{{ art.title }}</span>
      {% if art.date %}
        <span class="arts-note">{{ art.date }}</span>
      {% endif %}
    </span>
  </a>
{% endfor %}
</div>
