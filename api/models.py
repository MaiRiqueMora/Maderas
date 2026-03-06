from django.db import models

# Create your models here.
class Conductor(models.Model):
    nombre = models.CharField(max_length=120)
    licencia_conducir = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=200)
    def __str__(self): return self.nombre

class Camion(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=80)
    capacidad_carga = models.FloatField(help_text="Toneladas")
    conductor = models.ForeignKey(Conductor, on_delete=models.PROTECT, related_name="camiones")
    def __str__(self): return f"{self.placa} - {self.modelo}"

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    def __str__(self): return self.nombre_empresa

class TipoMadera(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True)
    def __str__(self): return self.nombre

class Carga(models.Model):
    tipo_madera = models.ForeignKey(TipoMadera, on_delete=models.PROTECT, related_name="cargas")
    cantidad = models.FloatField(help_text="m³")
    peso = models.FloatField(help_text="Toneladas")
    camion = models.ForeignKey(Camion, on_delete=models.PROTECT, related_name="cargas")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="cargas")
    def __str__(self): return f"{self.tipo_madera} - {self.cantidad} m³ → {self.cliente}"