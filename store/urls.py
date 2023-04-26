from django.urls import path

from .views import *

urlpatterns = [
    # Leave as empty string for base url
    path('', StoreView.as_view(), name="store"),
    path('cart/', CartView.as_view(), name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('register/', RegisterForm.as_view(), name="register"),
    path('login/', IngresarView.as_view(), name="login"),
    #cerrar sesión
    path('cerrar/', LogoutView.as_view(), name="cerrar"),
    path('product/<int:pk>/',ProductDetailView.as_view(),name='detalle_product'),
    path('delete/item/<int:pk>/',cantiCarrito, name="delete_item_cart"),
    path('aumentar/item/<int:pk>/',aumentarCantidad, name="aumentar_item"),
    path('disminuir/item/<int:pk>/',disminurCantidad, name="disminuir_item")
]
