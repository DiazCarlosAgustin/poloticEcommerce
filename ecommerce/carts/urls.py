from django.urls import path

from . import views
app_name = "cart"
urlpatterns = [
    path('', views.cart ,name='carrito'),
    path('add_cart/<slug:param_slug>', views.add_cart ,name='add_cart'),
    path('remove_cart/<int:param>', views.remove_cart ,name='remove_cart'),
    path('clear_cart', views.clear_cart ,name='clear_cart'),
]