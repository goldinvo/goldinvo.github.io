---
layout: page
title: Blog
content-type: mixed
---
<div class="blog-list">
  <ul>
    {% for post in site.posts %}
      <li>
        <a id="thumbnail" href="{{ post.url }}"><img src="{{ post.featured-image }}"></a>
        <div class="meta">
          <a id="title" class="link-highlight secondary-font" href="{{ post.url }}">{{ post.title }}</a>
          <div>{{ post.excerpt | strip_html }}</div>
          <div id="date">{{ post.date | date: "%b %-d, %Y" }}</div>
        </div>
      </li>
    {% endfor %}
  </ul>
</div>