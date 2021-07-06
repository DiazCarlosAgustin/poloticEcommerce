from django.db.models.expressions import Exists
from .carrito import Cart
from django.http.response import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
# Create your views here.

def cart(request):
    total = 0
    try:
        cart = Cart.objects.filter(user__id=request.user.id)
        for item in cart:
            total += item.productos.precio
    except Cart.DoesNotExist:
        cart = None

    return render(request, 'carrito/carrito.html',{
        "user": request.user,
        "cart":cart,
        "total": total
    })

def add_cart(request, param_slug):
    producto = Product.objects.filter(slug=param_slug)
    usuario = User.objects.filter(id=int(request.user.id))
    # try:
    cart = Cart.objects.filter(user__id = usuario[0].id, productos__id = producto[0].id)
    # except Cart.DoesNotExist:
    if cart is not Exists:
        cart = Cart.objects.create(user=usuario[0],productos=producto[0])
        cart.save()

    return HttpResponseRedirect(reverse("productos:producto", args=(param_slug,)))

def remove_cart(request, param):
    cart = Cart.objects.filter(id=param)
    cart.delete()

    total = 0
    try:
        cart = Cart.objects.filter(user__id=request.user.id)
        for item in cart:
            total += item.productos.precio
    except Cart.DoesNotExist:
        cart = None

    return render(request, 'carrito/carrito.html',{
        "user": request.user,
        "cart":cart,
        "total": total
    })

def clear_cart(request):
    cart = Cart.objects.filter(user__id = request.user.id)
    cart.delete()
    
    total = 0
    try:
        cart = Cart.objects.filter(user__id=request.user.id)
        for item in cart:
            total += item.productos.precio
    except Cart.DoesNotExist:
        cart = None

    return render(request, 'carrito/carrito.html',{
        "user": request.user,
        "cart":cart,
        "total": total
    })