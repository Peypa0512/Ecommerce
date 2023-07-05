#vamos a crear las referencias que necesitamos...
from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0

    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        #me va a devolver una colección pero solo quiero 1 elemento, pero que se apunte a ese elemento
        cart_items = CartItem.objects.all().filter(cart=cart[:1])

        # quiero saber la cantidad total de productos
        for cart_item in cart_items:
            cart_count += cart_item.quantity
    except Cart.DoesNotExist:
        cart_count=0
    return dict(cart_count=cart_count)