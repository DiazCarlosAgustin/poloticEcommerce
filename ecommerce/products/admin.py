from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ('titulo','descripcion','precio','imagen','categoria')
    list_display = ('__str__','slug')
admin.site.register(Product,ProductAdmin)
