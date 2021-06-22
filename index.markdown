---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Gallery
layout: page
---
<div class="gallery">
  {% for post in site.posts %}
    <a href="{{ post.url }}">
      <img src="{{ post.featured-image }}">
    </a>
  {% endfor %}
</div>

<script>
  const parent = document.querySelector(".gallery");
  const shuffled = shuffle(Array.from(parent.children));
  shuffled.forEach(child => parent.appendChild(child));
</script>