from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from confApp.views import (
    products,
    DetalleProducto,
    DetalleProducto2,
    Inicio,
    Iniciar_sesion,
    Inicio_proveedores,
    save_producto,
    estado_entrega,
    cambiar_estado,
    PedidoExitoso
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('products/', products, name='productos'),
    path('DetalleProducto/', DetalleProducto, name='DetalleDeProductos'),
    path('DetalleProducto2/', DetalleProducto2, name='DetalleDeProducto2'),
    path('', Inicio, name='Inicio1'),
    path('iniciarsesion/', Iniciar_sesion, name='InicioSesion'),
    path('IncioProveedores/', Inicio_proveedores, name='InicioProveedores'),
    path('success/', save_producto, name='saveProducto'),
    path('PedidoExitoso/',PedidoExitoso,name='PedidoConExito'),
    path('estado/', estado_entrega, name='EstadoEntrega'),
    path("logrado/", cambiar_estado, name="cambiar_estado")
]
