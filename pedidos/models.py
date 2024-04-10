from django.db import models # type: ignore

from productos.models import Producto

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    para_llevar = models.BooleanField()
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='pendiente')
    cantidad = models.CharField(max_length=20, default=1)
    productos = models.ManyToManyField(Producto, through='DetallePedido')

    def __str__(self):
        return self.cliente
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
    empaque = models.CharField(max_length=50)
    def __str__(self):
        return self.pedido
