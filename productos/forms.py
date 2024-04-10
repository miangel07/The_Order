from django import forms # type: ignore

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields =[
            'nombre',
            'descripcion',
            'precio',
        ]