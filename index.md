---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Gallery
layout: page
script: /scripts/index.js
---

<div class="gallery">

  <div class="buttons">
    <button type="button" id="gal-shuffle">Shuffle</button>
  </div>

  <div class="posts">
    {% for post in site.posts %}
      <a id="{{ forloop.index0 }}" href="{{ post.url }}">
        <img src="{{ post.featured-image }}">
      </a>
    {% endfor %}
  </div>

</div>