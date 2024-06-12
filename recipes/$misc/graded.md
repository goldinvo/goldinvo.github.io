---
layout: page
title: Grading
permalink: /recipes/graded
---
<!-- I am definitely not using Jekyll tools the way they were supposed to be used here -->
See also: [Index (Ungraded)](/recipes/all-recipes)

# Index (Graded):
<div class="recipes-index">
<h3> E: In-depth & high quality </h3>
<ul>
{% for node in site.pages %}
{% if node.path contains "recipes" and node.grade == 'E' %}
{% unless node.path contains "$misc" %}
<li {% if node.path contains "index" %}class="folder"{% endif %}><a href="{{node.url}}">{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> A: Meets standard </h3>
<ul>
{% for node in site.pages %}
{% if node.path contains "recipes" and node.grade == 'A' %}
{% unless node.path contains "$misc" %}
<li {% if node.path contains "index" %}class="folder"{% endif %}><a href="{{node.url}}">{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> D: In development </h3>
<ul>
{% for node in site.pages %}
{% if node.path contains "recipes" and node.grade == 'D' %}
{% unless node.path contains "$misc" %}
<li {% if node.path contains "index" %}class="folder"{% endif %}><a href="{{node.url}}">{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> B: On to-do list; no content </h3>
<ul>
{% for node in site.pages %}
{% if node.path contains "recipes" and node.grade == 'B' %}
{% unless node.path contains "$misc" %}
<li {% if node.path contains "index" %}class="folder"{% endif %}><a href="{{node.url}}">{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

</div>