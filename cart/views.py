from django.shortcuts import render, redirect


# Create your views here.
def display_cart(request):
    cart_msg = "Let's keep shopping!"
    # template = "home/index.html"
    context = {
        'cart_message': cart_msg,
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    # code to add items to the shopping cart
    """
    code below learned and taken from CI's project example
    and modified to this project
    """
    item_quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    """
    Create an empty (or check if already exsists) session's cart
    dictionary var which will keep track of item qty
    added to the card during the user's session
    """
    session_cart = request.session.get('session_cart', {})

    # important clarification: the quantity serves as value for the item_id
    if item_id in list(session_cart.keys()):
        session_cart[item_id] += item_quantity
    else:
        session_cart[item_id] = item_quantity

    # save the new asssigned quantity value into the session's cart
    request.session['sesssion_cart'] = session_cart
    print(request.session['sesssion_cart'])

    # my code - save the item count and will send it back to the page
    # item_count = request.session['sesssion_cart']
    # print(item_count)

    return redirect(redirect_url)


