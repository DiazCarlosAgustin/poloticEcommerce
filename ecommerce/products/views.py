from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

# Create your views here.
class ProductIndexListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['object_list']
        context['last_products'] = Product.objects.all().order_by('-created_at')[:1]
        
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context