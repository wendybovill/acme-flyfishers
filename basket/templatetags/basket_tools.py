from django import template

register = template.Library()


@register.filter(name='subtotal_sum')
def subtotal_sum(price, quantity):
    return price * quantity
