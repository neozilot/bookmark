from django.test import TestCase

# Create your tests here.
{% block pagination %}
    {% if is_paginated %}
        <ul class="pagination justify-content-center pagination-sm">
            {% if page_obj.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="{% url 'list' %}?page={{ page_obj.previous_page_number }}" tabindex="-1">Previous</a>
                </li>
            {% else %}
            <li class="page-item disabled">
                <a class="page-link" href="#" tabindex="-1">Previous</a>
            </li>
            {% endif %}

            {% for object in page_obj.paginator.page_range %}
                <li class="page-item {% if page_obj.number == forloop.counter %} disabled {% endif %}">
                    <a class="page-link" href="{{ request.path }}?page={{ forloop.counter }}">{{ forloop.counter }}</a>
                </li>
            {% endfor %}

            {% if page_obj.has_next %}
                <li class="page-item">
                    <a class="page-link" href="{% url 'list' %}?page={{ page_obj.next_page_number }}">Next</a>
                </li>
            {% else %}
            <li class="page-item disabled">
                <a class="page-link" href="#">Next</a>
            </li>
            {% endif %}
        </ul>
    {% endif %}
{% endblock %}