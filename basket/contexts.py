from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def basket_contents(request):

    basket_items = []
    subtotal = 0
    full_total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal += item_data * product.price
        product_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    ukmail = Decimal(2.99)

    subdelivery = subtotal * Decimal(
        settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    ukdelivery = ukmail + subdelivery

    delivery = ukdelivery

    full_total = delivery + subtotal

    context = {
        'basket_items': basket_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'delivery': delivery,
        'full_total': full_total,
    }

    return context
