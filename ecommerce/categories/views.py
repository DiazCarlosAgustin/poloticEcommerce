from products.models import Product
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .models import Category
# Create your views here.

def viewCategory(request, id):
    Products = Product.objects.filter(categoria__id = id)
    name = Category.objects.filter(id=id).get()
    print(name)
    return render(request, 'categorias/categorias.html',
    {
        'productos': Products,
        'name': name
    })


def dropdownCategory(request):
    categorias = Category.objects.all()
    return {
        'categorias': categorias
    }