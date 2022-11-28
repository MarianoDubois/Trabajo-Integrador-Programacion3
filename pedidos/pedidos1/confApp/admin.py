from django.contrib import admin
from .models import CondicionesIva
from .models import Detalles
from .models import EstadosVenta
from .models import Localidades
from .models import Productos
from .models import Proveedores
from .models import UnidadMedida
from .models import Ventas

admin.site.register(CondicionesIva)
admin.site.register(Detalles)
admin.site.register(EstadosVenta)
admin.site.register(Localidades)
admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(UnidadMedida)
admin.site.register(Ventas)