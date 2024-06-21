---
title: goldinvo.com
layout: default
---

<div class="homepage">
  <!-- Unique homepage navbar -->
  <nav class="secondary-font link-highlight">
    <div><a href="/">goldinvo.com</a></div>
    <ul> 
        <li><a href="/blog">Blog</a></li>
        <li><a href="/recipes">Recipes</a></li>
        <li><a href="/about">About</a></li>
    </ul>
  </nav>

  <div class="gallery">
    {% for post in site.posts %}
      {% if post.featured %}
        <a href="{{ post.url }}"><img src="{{ post.featured-image }}"></a>
      {% endif %}
    {% endfor %}
  </div>
</div>
