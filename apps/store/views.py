from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class StoreListView(ListView):
    model = Product
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tienda'
        return context


def cart(request):
    context = {'title': 'Carrito'}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {'title': 'Pago'}
    return render(request, 'store/checkout.html', context)
