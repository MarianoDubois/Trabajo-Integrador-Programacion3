from django.contrib import admin

from .models import *

admin.site.register(CondicionesIva)
admin.site.register(Detalles)
admin.site.register(EstadosVenta)
admin.site.register(Localidades)
admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(UnidadMedida)
admin.site.register(Ventas)


class CondicionesIvaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class DetallesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_producto', 'id_venta', 'cantidad',)
    search_fields = ('id', 'id_producto', 'id_venta', 'cantidad',)
    list_filter = ('id', 'id_producto', 'id_venta', 'cantidad',)
    list_per_page = 10


class EstadoVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class Localidades(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'precio_unidad', 'id_unidad_medida',)
    search_fields = ('id', 'nombre', 'stock', 'precio_unidad', 'id_unidad_medida',)
    list_filter = ('id', 'nombre', 'stock', 'precio_unidad', 'id_unidad_medida',)
    list_per_page = 10


class ProveedoresAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cuit', 'razon_social', 'id_condicion_iva', 'id_localidad', 'calle', 'numero', 'departamento', 'piso',
        'telefono', 'fax',)
    search_fields = (
        'id', 'cuit', 'razon_social', 'id_condicion_iva', 'id_localidad', 'calle', 'numero', 'departamento', 'piso',
        'telefono', 'fax',)
    list_filter = (
        'id', 'cuit', 'razon_social', 'id_condicion_iva', 'id_localidad', 'calle', 'numero', 'departamento', 'piso',
        'telefono', 'fax',)
    list_per_page = 10


class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_proveedor', 'id_estado', 'fecha_solicitud', 'fecha_recibido', 'direccion_entrega',)
    search_fields = ('id', 'id_proveedor', 'id_estado', 'fecha_solicitud', 'fecha_recibido', 'direccion_entrega',)
    list_filter = ('id', 'id_proveedor', 'id_estado', 'fecha_solicitud', 'fecha_recibido', 'direccion_entrega',)
    list_per_page = 10
