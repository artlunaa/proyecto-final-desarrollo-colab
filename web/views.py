from django.shortcuts import render
from .models import Alumno, Materia


# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})


def crear_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        carrera = request.POST['carrera']
        semestre = request.POST['semestre']
        alumno = Alumno(nombre=nombre, apellido=apellido, email=email, carrera=carrera, semestre=semestre)
        alumno.save()
        return render(request, 'crud-alumno/crear.html', {'mensaje': 'Alumno creado correctamente'})
    return render(request, 'crud-alumno/crear.html')