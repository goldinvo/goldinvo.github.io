---
layout: page
title: Blog
---
<div class="blog-list">
  <ul>
    {% for post in site.posts %}
      <li>
        <a href="{{ post.url }}"><img src="{{ post.featured-image }}"></a>
        <div class="meta">
          <a href="{{ post.url }}"><div id="title">{{ post.title }}</div></a>
          <div>{{ post.excerpt | strip_html }}</div>
          <div id="date">{{ post.date | date: "%b %-d, %Y" }}</div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>