from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
# estos mensajes se guardan en el request
#from django.contrib import messages
# users
from .form import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


class Store(ListView):
    model = Product
    template_name = 'store/store.html'


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
        form = UserRegisterForm()
    context['form'] = form
    return render(request, 'store/register.html', context)

class Ingresar(LoginView):
    template_name='store/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: #si esta logueado lo mando a la vista principal
            return redirect('store')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #recupero el context para enviar datos
        context['title']='Iniciar sesión'
        return context


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def cerrar(request):
    logout(request)
    return redirect('login')
