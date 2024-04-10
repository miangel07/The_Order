from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductoForm
def registro(request):
    
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
        
    return render(request,'productos.html',{"form":form}) 
