from django.shortcuts import render
from .forms import PedidosForm  # Asegúrate de importar el formulario correctamente
from .models import Producto,DetallePedido

def tomar_pedido(request):
    productos_disponibles = Producto.objects.all()  # Obtener todos los productos disponibles
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            # Guardar el pedido en la base de datos
            form.save()
            # Redirigir a una página de confirmación o mostrar un mensaje de éxito
            return render(request, 'factura.html')
    else:
        form = PedidosForm()
    
    return render(request, 'pedidos.html', {'productos': productos_disponibles, 'form': form})



