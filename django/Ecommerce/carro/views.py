from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from store.models import Product, Variation


# va a ser una función privada (por eso empieza por '_', para ver si está creado el carro, sino lo crea)
def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart


# representa la creación del carrito de compra
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # vamos a hacer que los variation se haga a una coleccion variable...
    product_variation = []

    if request.method == 'POST':
        for item in request.POST:
            key = item  # nombre del Variation (color)
            value = request.POST[key]  # el valor (verde)
            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key,
                                                  variation_value__iexact=value)
                product_variation.append(variation)

            except:
                pass
    # creamos el carrito de la compra por si exite...
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()

    # insercción del registro
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)

        # vamos a capturar los variations
        ex_var_list = []
        id = []
        # vamos a comparar para ver si son iguales los variations
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(item.id)

        # hacemos la comparacion
        if product_variation in ex_var_list:
            # necesitamos el indice para poder actualizar el variation
            index = ex_var_list.index(product_variation)
            item_id = id[index]
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()
        else:
            item = CartItem.objects.create(product=product, quantity=1, cart=cart)

            # verificamos que hay productos en la collección
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()


    else:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        # verificamos que hay productos en la collección
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)

        cart_item.save()

    return redirect('carro')


# función para restar productos
def borrar_cart(request, product_id, cart_item_id):
    #me va a dar el objeto del carrito
    cart = Cart.objects.get(cart_id=_cart_id(request))
    #me va a dar el producto en cuestion
    product = get_object_or_404(Product, id=product_id)

    try:

        # y lo que contiene de productos y cantidades
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass

    return redirect('carro')


# función para la funcionalidad del botón eliminar
def borrar_cart_item(request, product_id, cart_item_id):

    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)

    cart_item.delete()

    return redirect('carro')



# envio a la página del carro
def carro(request, total=0, quantity=0, cart_items=None):
    iva = 0
    precio_total = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items= CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            #para saber los productos y el precio
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        iva = (21 * total) / 100
        precio_total = total + iva
    except ObjectDoesNotExist:
        pass # solo ignora la excepción

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'iva': iva,
        'precio_total': precio_total
    }
    return render(request, 'store/carro.html', context)
