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
    search_method = "menu_search"

    template = 'products/products.html'

    if request.GET:
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
            search_method = "search_form"

        if 'category' in request.GET:
            cat_selected = request.GET['category']

            """
            get queryset from Product model for the category id
            based on the selected subcategory name
            code ref. https://overiq.com/django-1-11/django-orm-basics-part-2/
            """
            cat_products = Product.objects.filter(category__name=cat_selected)
            # print(cat_products)
            products = cat_products

            category_search = Category.objects.filter(name=cat_selected)
            # print(category_search)

            category = category_search
            print(category)

            # category = cat_selected

            search_method = "menu_search"

        if 'subcategory' in request.GET:
            subcat_selected = request.GET['subcategory']

            """get queryset from Product model for the subcategory id
            based on the selected subcategory name"""
            subcat_products = \
                Product.objects.filter(subcategory__name=subcat_selected)

            products = subcat_products
            print(products)

            category_search = \
                Category.objects.filter(subcategory__name=subcat_selected)
            # print(category_search)

            category = category_search
            print(category)

            subcategory = subcat_selected

            search_method = "menu_search"

    context = {
        "products": products,
        "search_term": search_query,
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
