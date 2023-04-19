from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store.as_view(), name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('register/', views.register, name="register"),
    path('login/', views.ingresar, name="login"),
    path('cerrar/', views.cerrar, name="cerrar"),
]
