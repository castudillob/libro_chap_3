from django import template

register = template.Library()

@register.simple_tag
def hello_world(name):
    suma = 2+3
    publica = str(suma)
    salute = 'Hola' + ' ' + name + ' la suma es de 3 + 2 es: ' + publica

    return salute