from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    productos = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
        super(Cart,self).save(*args,**kwargs)