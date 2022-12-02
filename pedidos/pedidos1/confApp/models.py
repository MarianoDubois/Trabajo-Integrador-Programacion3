# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CondicionesIva(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Condiciones_Iva'
        verbose_name_plural = "Condiciones de Iva"


class Detalles(models.Model):
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_venta = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='id_venta', blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)

    def subtotal(self):
        subtotal = (self.id_producto.precio_unidad*self.cantidad)
        return subtotal
    
    def __str__(self):
        return f"Detalle Numero({str(self.id)}) Subtotal({str(self.subtotal())}$)"

    class Meta:
        managed = False
        db_table = 'Detalles'
        verbose_name_plural = "Detalles"


class EstadosVenta(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Estados_Venta'
        verbose_name_plural = "Estados de la Venta"


class Localidades(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Localidades'
        verbose_name_plural = "Localidades"


class Productos(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    precio_unidad = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    id_unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='id_unidad_medida', blank=True,null=True)
    
    def restock(self, nuevo_stock):
        producto = Productos.objects.get(id=self.id)
        producto.stock = producto.stock+nuevo_stock
        producto.save()
    
    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Productos'
        verbose_name_plural = "Productos"


class Proveedores(models.Model):
    cuit = models.BigIntegerField(blank=True, null=True)
    razon_social = models.CharField(max_length=30, blank=True, null=True)
    id_condicion_iva = models.ForeignKey(CondicionesIva, models.DO_NOTHING, db_column='id_condicion_iva', blank=True,
                                         null=True)
    id_localidad = models.ForeignKey(Localidades, models.DO_NOTHING, db_column='id_localidad', blank=True, null=True)
    calle = models.CharField(max_length=30, blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    departamento = models.CharField(max_length=30, blank=True, null=True)
    piso = models.IntegerField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.razon_social

    class Meta:
        managed = False
        db_table = 'Proveedores'
        verbose_name_plural = "Proveedores"


class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'Unidad_Medida'
        verbose_name_plural = "Unidades de medida"


class Ventas(models.Model):
    id_proveedor = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    id_estado = models.ForeignKey(EstadosVenta, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    direccion_entrega = models.CharField(max_length=30, blank=True, null=True)

    def stock_finder(self):
        if self.id_estado == 1:
            detalles = Detalles.objects.all().filter(id_venta=self.id)
            for detalle in detalles:
                producto = detalle.id_producto
                cantidad = detalle.cantidad
                Productos.restock(producto, cantidad)

    def set_estado(self, nuevo_estado):
        venta = Ventas.objects.get(id=self.id)
        venta.id_estado = nuevo_estado
        venta.save()
        self.stock_finder()
    
    def total(self):
        list_detalles = Detalles.objects.all().filter(id_venta=self.id)
        suma = 0
        for detalle in list_detalles:
            precio = detalle.id_producto.precio_unidad
            cantidad = detalle.cantidad
            suma = suma+(precio*cantidad)
        return suma


    def __str__(self):
        return f"Venta Numero({str(self.id)}) Total(+{str(self.total())}$)"

    class Meta:
        managed = False
        db_table = 'Ventas'
        verbose_name_plural = "Ventas"
