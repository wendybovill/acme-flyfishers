from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """ View to view basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ add product qty to basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {basket[item_id]}'))
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def basket_update(request, item_id):
    """update product quantity in basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {basket[item_id]}'))
    else:
        basket.pop(item_id)
        messages.success(request,
                         (f'Updated {product.name} '
                          f'in your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """delete product from basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Deleted {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting item: {e} from basket')
        return HttpResponse(status=500)
