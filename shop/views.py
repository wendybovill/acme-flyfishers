from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Slide, Season

# Create your views here.


def shop(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    seasons = None
    sort = None
    direction = None
    hooksize = None
    specialoffer = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'season':
                sortkey = 'season__name'
            if sortkey == 'hooksize':
                sortkey = 'hooksize'
            if sortkey == 'specialoffer':
                sortkey = 'specialoffer'
            elif sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'season' in request.GET:
            seasons = request.GET['season'].split(',')
            products = products.filter(season__name__in=seasons)
            seasons = Season.objects.filter(name__in=seasons)

        if 'hooksize' in request.GET:
            products = request.GET['hooksize'].split(',')
            products = products.filter(hooksize__name__in=products)
            products = Product.objects.filter(name__in=products)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_seasons': seasons,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/shop.html', context)
