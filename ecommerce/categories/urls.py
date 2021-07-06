from django.urls import path

from . import views

app_name  = 'categorias'
urlpatterns = [
    path('<int:id>', views.viewCategory ,name='categorias'),
]
