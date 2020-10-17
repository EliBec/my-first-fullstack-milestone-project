from django.shortcuts import render, redirect, reverse,\
                             HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.
def display_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # code to add items to the shopping cart
    """
    code below learned and taken from CI's project example
    and modified to this project
    """
    product = get_object_or_404(Product, pk=item_id)
    item_quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    product_size = None

    if 'product_size' in request.POST:
        product_size = request.POST['product_size']

    """
    Assign to a var the session's dict (if it exists)
    If the dict does not exist, then assign and EMPTY dict
    """
    cart_session = request.session.get('cart_session', {})

    if product_size:
        if item_id in list(cart_session.keys()):
            if product_size in cart_session[item_id]['items_by_size'].keys():
                cart_session[item_id]['items_by_size'][product_size] \
                    += item_quantity
                messages.success(request,
                                 f'Updated quantity to \
                                     {cart_session[item_id]["items_by_size"][product_size]}\
                                     for {product.name} and \
                                     {product_size.upper()}')
            else:
                cart_session[item_id]['items_by_size'][product_size] \
                    = item_quantity
                messages.success(request,
                                 f'Added {product_size.upper()} to \
                                    {product.name}')
        else:
            cart_session[item_id] = \
                {'items_by_size': {product_size: item_quantity}}
            messages.success(request,
                             f'Added {product_size.upper()} to {product.name}')
    else:
        # important clarification: the quantity serves as value
        # for the item_id key, BUT item_id is not literal, but
        # passed in as a parameter into this view
        if item_id in list(cart_session.keys()):
            cart_session[item_id] += item_quantity
            messages.success(request,
                             f'Updated {product.name} quantity to \
                              {cart_session[item_id]}')
        else:
            cart_session[item_id] = item_quantity
            messages.success(request,
                             f'Added {product.name} to your Cart')

    # save the new asssigned quantity value into the session's cart
    request.session['cart_session'] = cart_session
    print(request.session['cart_session'])

    return redirect(redirect_url)


def update_cart_qty(request, item_id):
    # code to update item quantity in shopping cart
    """
    code below learned and taken from CI's project example
    and modified to this project
    """
    product = get_object_or_404(Product, pk=item_id)
    item_quantity = int(request.POST.get('quantity'))
    print(item_quantity)

    product_size = None

    if 'product_size' in request.POST:
        product_size = request.POST['product_size']

    cart_session = request.session.get('cart_session', {})

    if product_size:
        if item_quantity > 0:
            cart_session[item_id]["items_by_size"][product_size] \
                = item_quantity
            messages.success(request,
                             f'Updated quantity to \
                             {cart_session[item_id]["items_by_size"][product_size]}\
                             for {product.name} and \
                             {product_size.upper()}')
        else:
            del cart_session[item_id]['items_by_size'][product_size]
            if not cart_session[item_id]['items_by_size']:
                cart_session.pop[item_id]
                messages.success(request,
                                 f'Removed size {product_size.upper()}\
                                    {product.name} from your Cart')
    else:
        if item_quantity > 0:
            cart_session[item_id] = item_quantity
            messages.success(request,
                             f'Updated {product.name} quantity to \
                              {cart_session[item_id]}')
        else:
            # Python's pop() method to remove the key
            cart_session.pop(item_id)
            messages.success(request,
                             f'Removed {product.name} from your Cart')

    request.session['cart_session'] = cart_session

    return redirect(reverse('display_cart'))


def remove_from_cart(request, item_id):
    # code to remove item in shopping cart
    print('remove from cart')
    product = get_object_or_404(Product, pk=item_id)
    try:
        product_size = None

        if 'product_size' in request.POST:
            product_size = request.POST['product_size']

        """
        Assign to a var the session's dict (if it exists)
        If the dict does not exist, then assign and EMPTY dict
        """
        cart_session = request.session.get('cart_session', {})

        if product_size:
            del cart_session[item_id]['items_by_size'][product_size]
            if not cart_session[item_id]['items_by_size']:
                cart_session.pop(item_id)
                messages.success(request,
                                 f'Removed size {product_size.upper()}\
                                    {product.name} from your Cart')
        else:
            cart_session.pop(item_id)
            messages.success(request,
                             f'Removed {product.name} from your Cart')

        request.session['cart_session'] = cart_session

        """
        returns a 200 status code back to Javascript
        since it was the submit method that indirectly
        made the call for this view
        """
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

