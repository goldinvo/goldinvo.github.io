---
layout: page
title: Index
permalink: /recipes/all-recipes
---
[grading](/recipes/grading)
# Index
{% for node in site.pages %}
{% if node.path contains "recipes" and node.grade %}
{% unless node.path contains "$misc" %}
- [{{node.title}}]({{node.url}})
{% endunless %}
{% endif %}
{% endfor %}