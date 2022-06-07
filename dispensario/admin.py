from django.contrib import admin
from .models import medicamento
from .models import cliente

# Register your models here.


admin.site.register(medicamento)
admin.site.register(cliente)
