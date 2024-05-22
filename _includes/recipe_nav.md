# {{page.title}}

{% assign level = page.url | split:'/' | size | plus:1 %}

{% assign has_recipe = false %}

<ol>
{% for node in site.pages %}
  {% assign node_level = node.url | split:'/' | size %}
  {% if node.url contains page.url and node_level == level %}
  {% unless node.url contains "about" %}  
    {% unless node.path contains "index" %} {% assign has_recipe = true %} {% endunless %}
    {% if node.path contains "index" %} <a href="{{node.url}}"><li>{{node.title}}</li></a> {% endif %}
  {% endunless %}
  {% endif %}
{% endfor %}
</ol>

{% if has_recipe == true %}
## Recipes

<ul>
{% for node in site.pages %}
  {% assign node_level = node.url | split:'/' | size %}
  {% if node.url contains page.url and node_level == level %}
  {% unless node.url contains "about" or node.path contains "index" %}  
    <a href="{{node.url}}"><li>{{node.title}}</li></a>
  {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% endif %}