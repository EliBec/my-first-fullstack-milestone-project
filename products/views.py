from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory, Rating
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem

from .forms import ProductProfileForm, RatingForm


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
        else:
            sortkey = 'price'
        if 'direction' in request.GET:
            direction = request.GET['direction']
        else:
            direction = 'asc'

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

    products = None
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

    rating_count = 0
    rating_average = 0
    rating_list = {}
    user_rating = {}
    confirmed_purchase = False
    customer_orders = None
    rating_count = 0


    product = get_object_or_404(Product, pk=product_id)

    rating_list = Rating.objects.filter(product=product_id)
    print(rating_list)

    if rating_list is not None:

        for rating in rating_list:
            rating_count = rating_count + 1

        print(rating_count)
        if rating_count > 0:

            rating_average = product.rating / rating_count

            print(rating_average)

            review = None

    if request.user.is_authenticated:
        print("usuario existe")
        profile = request.user.userprofile
        print(profile)

        # see if there is any order linked to the logged-in user
        customer_orders = Order.objects.filter(user_profile=profile)

        """
        if order found, then find the items for that order based on the
        product if passed in
        """
        for order in customer_orders:
            for item in order.lineitems.all():
                if item.product.id == product.id:
                    confirmed_purchase = True
                    break

        if confirmed_purchase:
            print("conpra confirmada")
            user_rating = Rating.objects.filter(
                          customer=request.user,
                          product=product_id)

    template = 'products/product_detail.html'

    context = {
        "product": product,
        "rating_average": rating_average,
        "rating_list": rating_list,
        "user_rating": user_rating,
        "confirmed_purchase": confirmed_purchase,
        "rating_count": rating_count,
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


@login_required
def add_product(request):

    # make sure only super users can add products
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners are allowed'
                       'to perform this task.')
        return redirect(reverse('home'))

    if request.method == "POST":
        #  instance of the ProductProfileForm based on the request data from POST
        product_form_data = ProductProfileForm(request.POST, request.FILES)
        if product_form_data.is_valid():
            product = product_form_data.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('display_product_detail',
                            args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product.'
                           'Please ensure the form is valid.')
    else:
        product_form_data = ProductProfileForm()

    context = {
        'product_form_data': product_form_data,
    }

    template = 'products/addproduct.html'

    return render(request, template, context)


@login_required
def edit_product(request, product_id):

    # make sure only super users can edit products
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners are'
                       'allowed to perform this task.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product_form_data = ProductProfileForm(request.POST,
                                               request.FILES, instance=product)
        if product_form_data.is_valid():
            product_form_data.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('display_product_detail',
                            args=[product.id]))
        else:
            messages.error(request,
                           'Update failed. Pleae ensure the form is valid.')
    else:
        # instantiate the product form based on product for display
        product_form_data = ProductProfileForm(instance=product)

    template = 'products/editproduct.html'

    context = {
        'product_form_data': product_form_data,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):

    #  make sure only super users can delete products
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners are'
                       'allowed to perform this task.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


"""
The following mehtods take care of Product Rating management
"""


@login_required
def add_rating(request, product_id):

    confirmed_purchase = False

    product = get_object_or_404(Product, pk=product_id)

    profile = UserProfile.objects.get(user=request.user)
    # see if there is any order linked to the logged-in user
    customer_orders = Order.objects.filter(user_profile=profile)

    # if order found, then get items form order based on product passed in
    for order in customer_orders:
        for item in order.lineitems.all():
            if item.product.id == product.id:
                confirmed_purchase = True
                break

    if not confirmed_purchase:
        messages.error(request, 'You must have purchased this product in order to post a review')
        return redirect(reverse('display_product_detail',
                                args=[product.id]))

    if request.method == "POST":

        rating_form_data = {
                'nickname': request.POST['nickname'],
                'rating': request.POST['rating'],
                'headline': request.POST['headline'],
                'comment': request.POST['comment'],
                'recommend': request.POST['recommend'],
            }

        rating_form_data = RatingForm(rating_form_data)
        if rating_form_data.is_valid():
            rating = rating_form_data.save(commit=False)
            rating.customer = request.user
            rating.product = product
            rating.save()
            messages.success(request,
                             'Your Rating has been Published! Thank you!')
            return redirect(reverse('display_product_detail',
                                    args=[product.id]))
        else:
            messages.error(request,
                           'Failed to save your reating.'
                           'Please ensure the form is correclty filled.')
    else:
        rating_form_data = RatingForm(instance=profile)

    context = {
        'rating_form_data': rating_form_data,
        'product': product,
    }

    template = 'products/add_rating.html'

    return render(request, template, context)

@login_required
def edit_rating(request, product_id):

    confirmed_purchase = False

    product = get_object_or_404(Product, pk=product_id)
    
    profile = UserProfile.objects.get(user=request.user)
    # see if there is any order linked to the logged-in user
    customer_orders = Order.objects.filter(user_profile=profile)

    # if order found, then find the items for that order based on the 
    # product if passed in
    for order in customer_orders:
        for item in order.lineitems.all():
            if item.product.id == product.id:
                confirmed_purchase = True
                break

    if not confirmed_purchase:
        messages.error(request, 'You must have purchased this product and posted a review in order to edit it')
        return redirect(reverse('display_product_detail',
                                args=[product.id]))

    if request.method == "POST":
        rating_form_data = RatingForm(request.POST, instance=user)
        if rating_form_data.is_valid():
            rating_form_data.save()
            messages.success(request,
                             'Your review has been succesfully updated!')
            return redirect(reverse('display_product_detail',
                                    args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update the review.'
                           'Please ensure form is correctly filled')
    else:
        rating_form_data = RatingForm(instance=profile)

    template = 'products/edit_rating.html'

    context = {
        'product': product,
        'rating_form_data': rating_form_data,
    }
    return render(request, template, context)
   

@login_required
def delete_rating(request, product_id):

    confirmed_purchase = False

    product = get_object_or_404(Product, pk=product_id)

    profile = UserProfile.objects.get(user=request.user)
    # see if there is any order linked to the logged-in user
    customer_orders = Order.objects.filter(user_profile=profile)

    # if order found, then find the items for that order based on the 
    # product if passed in
    for order in customer_orders:
        for item in order.lineitems.all():
            if item.product.id == product.id:
                confirmed_purchase = True
                break

    if not confirmed_purchase:
        messages.error(request, 'You must have purchased this product and posted a review in order to delete it')
        return redirect(reverse('display_product_detail',
                                args=[product.id]))

    rating = get_object_or_404(Rating,
                               customer=request.user, product=product_id)
    rating.delete()
    messages.success(request, 'Your review has been successfully deleted.')
    return redirect(reverse('display_product_detail',
                            args=[product_id]))
