from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nro_legajo = models.IntegerField(unique=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_de_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"Estudiante: {self.nombre} - Nro Legajo: {self.nro_legajo}"


