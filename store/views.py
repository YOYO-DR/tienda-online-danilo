from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
# estos mensajes se guardan en el request
from django.contrib import messages
# users
from .form import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


class store(ListView):
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


def ingresar(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('store')
            else:
                messages.error(
                    request, 'El usuario o contraseña son incorrectos')
        else:
            messages.error(request, 'El usuario o contraseña son incorrectos')
    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, 'store/login.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def cerrar(request):
    logout(request)
    return redirect('login')
