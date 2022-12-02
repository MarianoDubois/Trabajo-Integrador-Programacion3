import datetime

from django.shortcuts import render

from .models import *


# Create your views here.
def home_screen_view(request):
    return render(request, 'index.html')


def products(request):
    productos = Productos.objects.all()
    proveedores = Proveedores.objects.all()
    return render(request, 'products.html', context={'proveedores': proveedores, 'productos': productos})


def DetalleProducto(request):
    return render(request, 'product-detail.html')


def DetalleProducto2(request):
    return render(request, 'product-detail2.html')


def Inicio(request):
    return render(request, 'Inicio.html')


def Iniciar_sesion(request):
    return render(request, 'sign-in.html')


def Registrarse(request):
    return render(request, 'sign-up.html')


def Inicio_proveedores(request):
    return render(request, 'sign-in-proveedores.html')


def Registrarse_proveedores(request):
    return render(request, 'sign-up-proveedores.html')


def estado_entrega(request):
    ventas = Ventas.objects.all()
    estados = EstadosVenta.objects.all()
    return render(request, 'estadoentrega.html', context={'ventas': ventas, 'estados': estados})

def PedidoExitoso(request):
    return render(request, 'PedidoExitoso.html')


def save_producto(request):
    proveedores = Proveedores.objects.all()
    proveedor = proveedores[int(request.POST['proveedor']) - 1]

    productos = Productos.objects.all()
    producto = productos[int(request.POST['producto']) - 1]

    estados = EstadosVenta.objects.all()

    venta = Ventas.objects.create(id_proveedor=proveedor, id_estado=estados[1], fecha_solicitud=datetime.date.today(),
                                  fecha_recibido=None)
    Detalles.objects.create(id_producto=producto, id_venta=venta, cantidad=request.POST['cantidad'])

    return render(request, "PedidoExitoso.html")  # REDIRIGIR A PAGINA DE EXITO

def cambiar_estado(request):
    ventas = Ventas.objects.all()
    venta = ventas[int(request.POST['venta']) -1]

    estados = EstadosVenta.objects.all()
    estado = estados[int(request.POST['estado']) -1]
    
    Ventas.set_estado(venta, estado) 

    return render(request, "PedidoExistoso.html")
