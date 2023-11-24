from django.db import models


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField()
    materias = models.ManyToManyField('Materia')


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    profesor = models.CharField(max_length=50)
    alumnos = models.ManyToManyField(Alumno)


class Calificaciones(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha = models.DateField(auto_now_add=True)
