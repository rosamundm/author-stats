from django import template
from .models import Book

register = template.Library()


@register.filter
def words_remaining(goalwordcount, wordcount):
    remaining = abs(goalwordcount-wordcount)
    return remaining


"""
# THE TEMPLATE:

{% load stat_tags %}
# headings:
   title
   date_added
   and so on
# body:
   {% for stat in stats %} #i.e. "stats" is context_object_name

 stat.title
 stat.date_added

 {% some_stat_fn stat.pk} # this is the template tag!

 {% endfor %}

 """
