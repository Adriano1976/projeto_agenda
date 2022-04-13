import datetime
from django import template

register = template.Library()


@register.simple_tag
def tempo_atual():
    return datetime.datetime.now().strftime('%H:%M:%S')


@register.simple_tag
def data_atual():
    return datetime.datetime.now().strftime('%d/%m/%Y')
