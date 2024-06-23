---
layout: page
title: Index
permalink: /recipes/all-recipes
content-type: text-two-columns
---
See also: [Index (Graded)](/recipes/graded)

# Index
<div class="recipes-index">
<ul>
{% assign sorted = site.pages | sort: "title" %}
{% for node in sorted %}
{% if node.path contains "recipes" %}
{% unless node.path contains "$misc" %}
<li><a href="{{node.url}}">{% if node.path contains "index" %}<img src="/assets/icons/folder.svg">{% endif %}{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>
</div>