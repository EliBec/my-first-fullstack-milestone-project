from django.shortcuts import render, redirect


# Create your views here.
def display_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # code to add items to the shopping cart
    """
    code below learned and taken from CI's project example
    and modified to this project
    """
    item_quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    product_size = None

    if 'product_size' in request.POST:
        product_size = request.POST['product_size']
        print(product_size)
    print("no hay")

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
            else:
                cart_session[item_id]['items_by_size'][product_size] \
                    = item_quantity
        else:
            cart_session[item_id] = \
                {'items_by_size': {product_size: item_quantity}}
    else:
        # important clarification: the quantity serves as value
        # for the item_id key, BUT item_id is not literal, but
        # passed in as a parameter into this view
        if item_id in list(cart_session.keys()):
            cart_session[item_id] += item_quantity
        else:
            cart_session[item_id] = item_quantity

    # save the new asssigned quantity value into the session's cart
    request.session['cart_session'] = cart_session
    print(request.session['cart_session'])

    return redirect(redirect_url)
