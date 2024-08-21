---
grade: S
title: Grading
---
<!-- I am definitely not using Jekyll tools the way they were supposed to be used here -->
See also: [Index (Ungraded)](/recipes/all-recipes)

# Index (Graded):
<div class="recipes-index">
<h3> E: Posts that I'm happy with </h3>
<ul>
{% assign sorted = site.pages | sort: "title" %}
{% for node in sorted %}
{% if node.path contains "recipes" and node.grade == 'E' %}
{% unless node.path contains "$misc" %}
<li><a href="{{node.url}}">{% if node.path contains "index" %}<img src="/icons/folder.svg">{% endif %}{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> A: Meets standard </h3>
<ul>
{% assign sorted = site.pages | sort: "title" %}
{% for node in sorted %}
{% if node.path contains "recipes" and node.grade == 'A' %}
{% unless node.path contains "$misc" %}
<li><a href="{{node.url}}">{% if node.path contains "index" %}<img src="/icons/folder.svg">{% endif %}{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> D: In development </h3>
<ul>
{% assign sorted = site.pages | sort: "title" %}
{% for node in sorted %}
{% if node.path contains "recipes" and node.grade == 'D' %}
{% unless node.path contains "$misc" %}
<li><a href="{{node.url}}">{% if node.path contains "index" %}<img src="/icons/folder.svg">{% endif %}{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> B: On to-do list; no content </h3>
<ul>
{% assign sorted = site.pages | sort: "title" %}
{% for node in sorted %}
{% if node.path contains "recipes" and node.grade == 'B' %}
{% unless node.path contains "$misc" %}
<li><a href="{{node.url}}">{% if node.path contains "index" %}<img src="/icons/folder.svg">{% endif %}{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>

<h3> S: Stubs </h3>
<ul>
{% assign sorted = site.pages | sort: "title" %}
{% for node in sorted %}
{% if node.path contains "recipes" and node.grade == 'S' %}
{% unless node.path contains "$misc" %}
<li><a href="{{node.url}}">{% if node.path contains "index" %}<img src="/icons/folder.svg">{% endif %}{{node.title}}</a></li>
{% endunless %}
{% endif %}
{% endfor %}
</ul>


</div>