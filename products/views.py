from django.shortcuts import render
from django.contrib import messages

from .models import Product, Category,  Subcategory


# Create your views here.
def display_products(request):

    products = Product.objects.all()

    template = 'products/products.html'

    context = {
        products: 'products',
    }

    return render(request, template, context)
