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
            <a href="{{ post.url }}"><h1>{{ post.title }}</h1></a>
            <span>{{ post.excerpt }}</span>
            <span id="date">{{ post.date | date: "%b %-d, %Y" }}</span>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>