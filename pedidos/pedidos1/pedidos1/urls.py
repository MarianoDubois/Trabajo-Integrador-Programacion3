"""pedidos1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from confApp.views import (
    products,
    DetalleProducto,
    DetalleProducto2,
    Inicio,
    Iniciar_sesion,
    Inicio_proveedores,
    save_producto,
    estado_entrega
)
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('products/', products, name='productos'),
    path('DetalleProducto/', DetalleProducto, name='DetalleDeProductos'),
    path('DetalleProducto2/', DetalleProducto2, name='DetalleDeProducto2'),
    path('', Inicio, name='Inicio1'),
    path('iniciarsesion/', Iniciar_sesion, name='InicioSesion'),
    path('IncioProveedores/', Inicio_proveedores, name='InicioProveedores'),
    path('success/', save_producto, name='saveProducto'),
    path('estado/', estado_entrega, name='EstadoEntrega')
]
