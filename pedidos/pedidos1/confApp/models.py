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

    class Meta:
        managed = False
        db_table = 'Condiciones_Iva'


class Detalles(models.Model):
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_venta = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='id_venta', blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Detalles'


class EstadosVenta(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Estados_Venta'


class Localidades(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Localidades'


class Productos(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    precio_unidad = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    id_unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='id_unidad_medida', blank=True,
                                         null=True)

    class Meta:
        managed = False
        db_table = 'Productos'


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

    class Meta:
        managed = False
        db_table = 'Proveedores'


class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Unidad_Medida'


class Ventas(models.Model):
    id_proveedor = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    id_estado = models.ForeignKey(EstadosVenta, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    direccion_entrega = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ventas'
