from django.contrib import admin
from .models import Camion, Conductor, Carga, Cliente, TipoMadera

# Register your models here.

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = ("placa","modelo","capacidad_carga","conductor")
    search_fields = ("placa","modelo","conductor__nombre")

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ("nombre","licencia_conducir","telefono")
    search_fields = ("nombre","licencia_conducir")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre_empresa","telefono","correo_electronico")
    search_fields = ("nombre_empresa","correo_electronico")

@admin.register(TipoMadera)
class TipoMaderaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Carga)
class CargaAdmin(admin.ModelAdmin):
    list_display = ("tipo_madera","cantidad","peso","camion","cliente")
    list_filter = ("tipo_madera","camion","cliente")