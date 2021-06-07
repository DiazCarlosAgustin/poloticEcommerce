from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib import messages

from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm

from products.models import Product
# show index
def index(request):
    Productos = Product.objects.all()
    last_product = Product.objects.all().order_by('-created_at')[:4]
    return render(request, 'index.html',{
        "products": Productos,
        "last_products": last_product,
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('login')


def login_view(request):
    if(request.user.is_authenticated):
        redirect('/')
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.validate()

        if user:
            login(request, user)
            messages.success(request, 'Se inicio sesion correctamente.')
            return redirect(index)
        else:
            messages.warning(request, 'El usuario o contraseña es incorrecta.')

    return render(request, 'user/login.html',{
        'form': form
    })

def register_view(request):
    if(request.user.is_authenticated):
        redirect('/')
    form = RegisterForm(request.POST or None) #si es por el metodo post guardar los datos del usuario, si no dejar vacio

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Se registro correctamente')
            return redirect('index')
        
    return render(request, 'user/register.html',{
        'form': form
    })