---
title: goldinvo.com
layout: page
disable-hidden-nav: true
---

<div class="homepage">
  <div class="gallery">
    {% for post in site.posts %}
      {% if post.featured %}
        <a href="{{ post.url }}"><img src="{{ post.featured-image }}"></a>
      {% endif %}
    {% endfor %}
  </div>
</div>
