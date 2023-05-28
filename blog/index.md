---
layout: page
title: Blog
---
<div class="blog-list">
  <ul>
    {% for post in site.posts %}
      <li>
        <img src="{{ post.featured-image }}">
        <div class="meta">
          <a href="{{ post.url }}"><div id="title">{{ post.title }}</div></a>
          <div>{{ post.excerpt | strip_html }}</div>
          <div id="date">{{ post.date | date: "%b %-d, %Y" }}</div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>