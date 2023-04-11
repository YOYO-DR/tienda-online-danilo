from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', StoreListView.as_view(), name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
]
