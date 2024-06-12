---
layout: page
title: Index
permalink: /recipes/all-recipes
---
See also: [Index (Graded)](/recipes/graded)

# Index
<div class="recipes-index">
<ul>
{% for node in site.pages %}
{% if node.path contains "recipes" %}
{% unless node.path contains "$misc" %}
<li {% if node.path contains "index" %}class="folder"{% endif %}><a href="{{node.url}}">{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>
</div>