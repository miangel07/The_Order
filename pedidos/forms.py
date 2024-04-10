from django import forms # type: ignore

from .models import Pedido,DetallePedido

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields =[
            'cliente',
            'para_llevar',
            'observaciones',
            'productos',
        ]
class factura(forms.ModelForm):
    class Meta:
        model=DetallePedido
        fields = [
            'pedido',
            'producto',
            'cantidad',
            'empaque',
        ]