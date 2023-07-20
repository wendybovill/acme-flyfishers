from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    grand_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    ukmail = Decimal(2.99)

    subdelivery = total * Decimal(
        settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    ukdelivery = ukmail + subdelivery

    delivery = ukdelivery

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
