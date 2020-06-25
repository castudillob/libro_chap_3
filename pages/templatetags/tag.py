from django import template

register = template.Library()

@register.simple_tag
def hello_world(name):
    suma = 2+3
    publica = str(suma)
    salute = 'Hello' + ' ' + name + ' ' + publica

    return salute