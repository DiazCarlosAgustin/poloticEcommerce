from .models import Product
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['titulo','descripcion','imagen','precio','categoria']
        widgets =  {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control py-2',
                'id': 'titulo'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control py-2',
                'id': 'descripcion'
            }),
            'imagen': forms.FileInput(attrs={
                'id': 'imagen',
                'class': 'py-2'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control py-2',
                'id': 'precio'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control py-2',
                'id': 'precio'
            }),
            
        }

    # def save(self):
    #     return Product.objects.create(
    #         self.cleaned_data.get('titulo'),
    #         self.cleaned_data.get('descripcion'),
    #         self.cleaned_data.get('imagen'),
    #         self.cleaned_data.get('precio'),
    #         self.cleaned_data.get('categoria'),
    #     )
        