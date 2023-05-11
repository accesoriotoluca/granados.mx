from django.shortcuts import render

# Create your views here.

def productos(request):
    render(request, 'productos/productos.html')
