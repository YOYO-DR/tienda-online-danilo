from django.urls import path

from .views import *

urlpatterns = [
    # Leave as empty string for base url
    path('', StoreView.as_view(), name="store"),
    path('cart/', CartView.as_view(), name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('register/', register, name="register"),
    path('login/', IngresarView.as_view(), name="login"),
    path('cerrar/', cerrar, name="cerrar"),
]
