from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField()


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    profesor = models.CharField(max_length=50)
    alumnos = models.ManyToManyField(Alumno)
