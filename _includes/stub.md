<!-- {% comment %}
    To use: 
    {% include stub.html src="relative/path.md"%}
{% endcomment %} -->

<!-- TODO: currently search through site.pages for target post. Maybe there is a better way to reference? -->
{% for node in site.pages %}
{% if node.path == include.src %}
    
{% if node.content contains "<!-- stub -->" %}
<div>
    <h3>{{node.title}}</h3>
    {{ node.content | split: "<!-- end_excerpt -->" | first | split: "<!-- begin_excerpt -->" | last }}
</div>
{% endif %}

{% endif %}
{% endfor %}


