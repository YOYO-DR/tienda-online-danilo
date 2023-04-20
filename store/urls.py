from django.urls import path

from .views import *

urlpatterns = [
    # Leave as empty string for base url
    path('', Store.as_view(), name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('register/', register, name="register"),
    path('login/', Ingresar.as_view(), name="login"),
    path('cerrar/', cerrar, name="cerrar"),
]
