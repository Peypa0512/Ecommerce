from django.shortcuts import render, get_object_or_404

from carro.models import CartItem
from carro.views import _cart_id
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        # vamos a llamar a una instancia de Paginator
        paginator = Paginator(products, 3)

        # como acceder a cada uno de los grupos con el parametro ?page=1 del navegador
        page = request.GET.get('page')

        # ahora que me envie esa página los productos
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count

    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    #puede que el usuario nos pase el slug de la BBDD y puede que no exista...
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        # si da un error
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            # que me busque por fecha de creación descendiente, vamos a hacer una doble consulta con or(Q) |
            productos = Product.objects.order_by('-create_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            productos_counts = productos.count()

    context = {
        'products': productos,
        'product_count': productos_counts,
    }
    return render (request, 'store/store.html', context)











