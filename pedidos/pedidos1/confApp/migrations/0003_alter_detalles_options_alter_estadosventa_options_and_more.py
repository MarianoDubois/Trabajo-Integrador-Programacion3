# Generated by Django 4.1.2 on 2022-11-30 14:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("confApp", "0002_alter_condicionesiva_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="detalles",
            options={"managed": False, "verbose_name_plural": "Detalles"},
        ),
        migrations.AlterModelOptions(
            name="estadosventa",
            options={"managed": False, "verbose_name_plural": "Estados Venta"},
        ),
        migrations.AlterModelOptions(
            name="localidades",
            options={"managed": False, "verbose_name_plural": "Localidades"},
        ),
        migrations.AlterModelOptions(
            name="productos",
            options={"managed": False, "verbose_name_plural": "Productos"},
        ),
        migrations.AlterModelOptions(
            name="proveedores",
            options={"managed": False, "verbose_name_plural": "Proveedores"},
        ),
        migrations.AlterModelOptions(
            name="unidadmedida",
            options={"managed": False, "verbose_name_plural": "Unidad Medida"},
        ),
        migrations.AlterModelOptions(
            name="ventas",
            options={"managed": False, "verbose_name_plural": "Ventas"},
        ),
    ]
