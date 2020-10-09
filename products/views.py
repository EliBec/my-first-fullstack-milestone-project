from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory


# Create your views here.
def display_all_products(request):

    products = Product.objects.all()
    search_query = None

    template = 'products/products.html'

    # logic for Search form
    if request.GET:
        if 'srch_qry' in request.GET:
            search_query = request.GET['srch_qry']
            if not search_query:
                messages.error(request, 'No search results were found')
                return redirect(reverse('products'))

            query_result = Q(name__icontains=search_query) | \
                Q(short_desc__icontains=search_query) | \
                Q(brand__icontains=search_query)

            products = products.filter(query_result)

    context = {
        "products": products,
        "search_term": search_query
    }

    return render(request, template, context)


def display_product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'

    context = {
        "product": product,
    }

    return render(request, template, context)
