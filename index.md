---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Gallery
layout: page
---

<div class="gallery">
  <!-- <div class="posts"> -->
    {% for post in site.posts %}
      {% if post.featured %}
        <a href="{{ post.url }}">
          <img src="{{ post.featured-image }}">
        </a>
      {% endif %}
    {% endfor %}
  <!-- </div> -->
</div>