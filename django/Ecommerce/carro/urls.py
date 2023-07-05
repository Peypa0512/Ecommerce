from django.urls import path
from . import views

urlpatterns = [
    path('', views.carro, name="carro"),
    path('add_cart/<int:product_id>/', views.add_cart, name="add_cart"),
    path('borrar_cart/<int:product_id>/<int:cart_item_id>/', views.borrar_cart, name="borrar_cart"),
    path('borrar_cart_item/<int:product_id>/<int:cart_item_id>/', views.borrar_cart_item, name="borrar_cart_item"),

]
