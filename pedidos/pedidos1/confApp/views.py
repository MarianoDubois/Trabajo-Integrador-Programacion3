from django.shortcuts import render
from .models import *

# Create your views here.
def home_screen_view(request):
    return render(request,'index.html')
    
def products(request):
    productos=Productos.objects.all()
    proveedores=Proveedores.objects.all()
    return render(request,'products.html', context={'proveedores':proveedores,'productos':productos})

def DetalleProducto(request):
    return render(request,'product-detail.html')

def DetalleProducto2(request):
    return render(request,'product-detail2.html')

def Inicio(request):
    return render(request,'Inicio.html')

def Iniciar_sesion(request):
    return render(request,'sign-in.html')

def Registrarse(request):
    return render (request,'sign-up.html')

def Inicio_proveedores(request):
    return render (request, 'sign-in-proveedores.html')

def Registrarse_proveedores(request):
    return render (request, 'sign-up-proveedores.html')

def estado_entrega(request):
    return render(request, 'estadoentrega.html' )

def save_producto(request):

    print(f"---{request.POST}---")

    """proveedores = Proveedores.objects.all()
    proveedor = proveedores[int(request.POST['proveedor'])]
    venta = Ventas.objects.create()"""
    return render(request, "products.html")