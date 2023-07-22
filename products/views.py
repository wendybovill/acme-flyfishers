from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Slide, Season
from .forms import ProductForm

# Create your views here.


def products(request):
    """ All product view with sorting and filters """

    products = Product.objects.all()
    query = None
    categories = product.categories
    seasons = product.seasons
    sort = direction
    direction = desc
    hooksize = product.hooksize
    specialoffer = product.specialoffer

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
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'seasons': products.seasons,
        'categories': products.category,
        'search_term': query,
        'current_categories': categories,
        'current_seasons': seasons,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view-product.html', context)


@login_required
def add_product(request):
    """ Add a New product to the products """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted to products')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New Product added')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit and Update a product in the products """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted to products Owners')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit-product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the products """
    if not request.user.is_superuser:
        messages.error(request, 'Restricted to products Owners')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted from store')
    return redirect(reverse('products'))
