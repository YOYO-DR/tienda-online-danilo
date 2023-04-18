from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
# Create your views here.


class store(ListView):
    model = Product
    template_name = 'store/store.html'

    # def get(self, request,*args, **kwargs):  # hacer la busqueda


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
