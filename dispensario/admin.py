from django.contrib import admin
from .models import medicamento, cliente, venta, proveedore


# Register your models here.


admin.site.register(medicamento)
admin.site.register(cliente)
admin.site.register(venta)
admin.site.register(proveedore)

