from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Product
from .forms import ProductForm
# Create your views here.
class ProductIndexListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('-created_at')[3:10]
        context['last_products'] = Product.objects.all().order_by('-created_at')[:3]
        
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductSearchListView(ListView):
    template_name='products/search.html'

    def get_queryset(self):
        filters = Q(titulo__icontains=self.query()) | Q(categoria__descripcion__icontains = self.query())
        return Product.objects.filter(filters)

    def query(self):
        print(self.request.GET.get('search'))
        return self.request.GET.get('search')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()

        return context

def eliminarProducto(request, id):
    producto = get_object_or_404(Product, id=id)
    producto.delete()
    return redirect('home')

def editProducto(request, id): 
    producto =  get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=producto)
        return render(request, 'products/editProduct.html',{
            'form':form
        })