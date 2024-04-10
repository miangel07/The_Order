from django.shortcuts import render,redirect
from pedidos.models import Pedido

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})
def cambiar_estado(request, pedido_id):
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.estado = nuevo_estado
        pedido.save()
        return redirect('lista_pedidos')
