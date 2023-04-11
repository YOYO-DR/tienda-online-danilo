from django.urls import path
from .views import *

app_name='store'

urlpatterns = [
 #Leave as empty string for base url
 path('', store, name="tienda"),
 path('cart/', cart, name="carrito"),
 path('checkout/',checkout, name="pago"),
]

