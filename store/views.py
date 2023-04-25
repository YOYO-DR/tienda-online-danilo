from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product,Cart
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .form import UserRegisterForm
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
import json #para manejar el body del json

#vista de los articulos
class StoreView(ListView):
    model = Product
    template_name = 'store/store.html'

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            query=Product.objects.filter(name__icontains=busqueda)
            return query
        else:
          return super().get_queryset()
  
    def post(self, request, *args, **kwargs):
        data=json.load(request) # con esta funcion lo convierto a diccionario
        if data['action']=='add_cart':
            product_id=data['product_id']
            user_id=data['user_id']
            produ=Cart.objects.filter(user_id=user_id,product_id=product_id).exists()
            if produ:
              carri=Cart.objects.get(user_id=user_id,product_id=product_id)
              carri.cantidad+=1
              carri.total=carri.cantidad*carri.product.price
              carri.save()
            else:
              precioProduct=Product.objects.get(id=product_id).price
              Cart(user_id=user_id,product_id=product_id,cantidad=1,total=precioProduct).save()
            return JsonResponse({'success':True})
        else:
          return JsonResponse({'success':False})

    def get_context_data(self, **kwargs):
        # recupero el context para enviar datos
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store'
        context['cart_url'] = reverse_lazy('cart')
        context['can_carrito']=Cart.objects.filter(user_id=self.request.user.id).count()
        return context

#regitro
def register(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data["username"]
            form.save()
            # messages.success(request, f"Usuario {username} creado")
            return redirect('store')
        else:
            context['error']='Ha ocurrido un error'
    else:
        form = UserRegisterForm()
    context['form'] = form
    context['title']='Registro'
    return render(request, 'store/register.html', context)

#login
class IngresarView(LoginView):
    template_name = 'store/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # si esta logueado lo mando a la vista principal
            return redirect('store')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # recupero el context para enviar datos
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

#carrito
class CartView(ListView):
  model = Cart
  template_name = 'store/cart.html'

  def dispatch(self, request, *args, **kwargs):
      if not request.user.is_authenticated:
          return redirect('login')
      return super().dispatch(request, *args, **kwargs)

  def get_queryset(self):
      query=Cart.objects.filter(user_id=self.request.user.id)
      return query
  def get_context_data(self, **kwargs):
      context=super().get_context_data(**kwargs)
      canCarrito=self.get_queryset().count()
      if canCarrito==0:
        context['title']='Carrito'
      else:
        context['title']=f'Carrito {canCarrito}'
      return context

#vista para comprar
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

#cerrar sesión
def cerrar(request):
    logout(request)
    return redirect('login')

#vista detail de los productos
class ProductDetailView(DetailView):
    model = Product
    template_name='store/product_detail.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=context['object'].name
        context['cart_url'] = reverse_lazy('cart')
        context['store_url'] = reverse_lazy('store')
        return context