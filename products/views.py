from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory


# Create your views here.
def display_all_products(request):

    products = Product.objects.all()
    search_query = None
    category = None
    subcategory = None
    search_method = "menusearch"
    sortkey = None
    direction = None

    template = 'products/products.html'

    if request.GET:

        # call sorting logic function if we get 'sort' as parameter
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
        if 'direction' in request.GET:
            direction = request.GET['direction']

        products = sorting_by(sortkey, direction, products)

        # logic for Search form
        if 'srch_qry' in request.GET:
            search_query = request.GET['srch_qry']
            if not search_query:
                messages.error(request, 'No search results were found')
                return redirect(reverse('products'))

            query_result = Q(name__icontains=search_query) | \
                Q(short_desc__icontains=search_query) | \
                Q(brand__icontains=search_query)

            products = products.filter(query_result)
            search_method = "searchform"

    context = {
        "products": products,
        "search_term": search_query,
        "category": category,
        "subcategory": subcategory,
        "search_method": search_method
    }

    return render(request, template, context)


def products_by_category(request, category_name):

    products= None
    subcategory = None
    category = None
    direction = None
    sortkey = None

    # find the category record first
    category_search = Category.objects.filter(name=category_name)

    #  if found, then find linked products and category
    if category_search:
        cat_products = Product.objects.filter(category__name=category_name)
        products = cat_products
        category = category_search

    # if category not found then, it means the subcategory was passed.
    # so, search subcategory. If found, then get linked products and category
    else:
        subcategory_search = Subcategory.objects.filter(name=category_name)

        """
        queryset codes below learned from:
        https://overiq.com/django-1-11/django-orm-basics-part-2/
        """
        if subcategory_search:
            cat_products = \
                Product.objects.filter(subcategory__name=category_name)

            category_search = \
                Category.objects.filter(subcategory__name=category_name)

            products = cat_products
            subcategory = subcategory_search
            category = category_search

    if request.GET:

        # call sorting logic function if we get 'sort' as parameter
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
        if 'direction' in request.GET:
            direction = request.GET['direction']

        products = sorting_by(sortkey, direction, products)

    template = 'products/products_categories.html'

    search_method = "breadcrumb"

    context = {
        "products": products,
        "category": category,
        "subcategory": subcategory,
        "search_method": search_method
    }

    return render(request, template, context)


def display_product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'

    context = {
        "product": product,
    }

    return render(request, template, context)


def sorting_by(sortkey, direction, products):

    if sortkey == 'category':
        sortkey = 'category__name'
    if sortkey == 'subcategory':
        sortkey = 'subcategory__name'
    if direction == 'desc':
        sortkey = f'-{sortkey}'  # the - reverses the sorting order

    products_sorted = products.order_by(sortkey)

    return products_sorted
