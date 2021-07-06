from django.urls import path

from . import views
app_name  = 'productos'
urlpatterns = [
    path('search', views.ProductSearchListView.as_view(),name='search'),
    path('<slug:slug>',views.ProductDetailView.as_view(), name='producto'),
    path('editar_articulo/<int:id>',views.editProducto, name='editaProducto'),
    path('eliminar_articulo/<int:id>',views.eliminarProducto, name='eliminarProducto'),
]
