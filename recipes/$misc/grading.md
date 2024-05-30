---
layout: page
title: Grading
permalink: /recipes/grading
---
<!-- I am definitely not using Jekyll tools the way they were supposed to be used  -->
Grades:
- S: extensive revisions and information{% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'S' %}{% unless node.path contains "$misc" %}
    - [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}
- A: tested and has seen revisions{% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'A' %}{% unless node.path contains "$misc" %}
    - [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}
- B: tested before, passable entry{% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'B' %}{% unless node.path contains "$misc" %}
    - [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}
- C: untested; basic info{% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'C' %}{% unless node.path contains "$misc" %}
    - [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}
- D: little to no info; want to try, TODO{% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'D' %}{% unless node.path contains "$misc" %}
    - [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}