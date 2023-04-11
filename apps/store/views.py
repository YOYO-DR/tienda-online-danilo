from django.shortcuts import render

def store(request):
  context = {'title':'Tienda'}
  return render(request,'store/store.html', context)

def cart(request):
  context = {'title':'Carrito'}
  return render(request, 'store/cart.html', context)

def checkout(request):
  context = {'title':'Pago'}
  return render(request, 'store/checkout.html', context)

