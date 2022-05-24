from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Registro)
admin.site.register(Tipo_persona)
admin.site.register(Persona)