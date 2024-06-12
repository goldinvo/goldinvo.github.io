---
layout: page
title: Grading
permalink: /recipes/graded
---
<!-- I am definitely not using Jekyll tools the way they were supposed to be used here -->
# Index (Graded):
### E: In-depth & high quality {% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'E' %}{% unless node.path contains "$misc" %}
- [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}

### A: Meets standard {% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'A' %}{% unless node.path contains "$misc" %}
- [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}

### D: In development {% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'D' %}{% unless node.path contains "$misc" %}
- [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}

### B: On to-do list; no content {% for node in site.pages %}{% if node.path contains "recipes" and node.grade == 'B' %}{% unless node.path contains "$misc" %}
- [{{node.title}}]({{node.url}}){% endunless %}{% endif %}{% endfor %}
