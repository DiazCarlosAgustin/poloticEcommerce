from django.db import models
from django.utils.text import slugify
from categories.models import Category
from django.db.models.signals import pre_save
import uuid
import json
# Create your models here.
class Product(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='products/', null =False, blank=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoria')
    slug = models.SlugField(null=False,blank=False, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def save(self,*args,**kwargs):
        self.slug = slugify(self.titulo)
        super(Product,self).save(*args,**kwargs)
        
def set_slug(sender, instance, *args, **kwargs):
    if instance.titulo and not instance.slug:
        slug = slugify(instance.titulo)

        while Product.objects.filter(slug=slug).exists():
           slug = slugify(
               '{}-{}'.format(instance.titulo,str(uuid.uuid4())[:8])
           )  

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
