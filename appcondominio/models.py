from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Residente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.nombre


class Mes(models.Model):
    nombre = models.CharField(max_length=30)
    monto = models.FloatField(default='200.00')
    def __str__(self):
        return self.nombre

class Pago(models.Model):
    empleado = models.ForeignKey(User)
    residente = models.ForeignKey(Residente)
    fecha = models.DateTimeField(default=timezone.now)
    meses = models.ManyToManyField(Mes, through='Factura')
    montototal = models.FloatField()
    def __str__(self):
        return self.empleado.username

class Factura(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)


class FacturaInLine(admin.TabularInline):
    model = Factura
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1


class MesAdmin(admin.ModelAdmin):
    inlines = (FacturaInLine,)


class PagoAdmin (admin.ModelAdmin):
    inlines = (FacturaInLine,)
