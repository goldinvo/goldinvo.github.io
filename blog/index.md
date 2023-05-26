---
layout: page
title: Blog
---
<div>
  <ul class="blog-list">
    {% for post in site.posts %}
      <li>
        <img src="{{ post.featured-image }}">
        <div>
            <a href="{{ post.url }}"><h1>{{ post.title }}</h1></a>
            <span>{{ post.date | date: "%b %-d, %Y" }}</span>
            <span>{{ post.excerpt }}</span>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>