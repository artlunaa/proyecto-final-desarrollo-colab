from django.shortcuts import render, redirect
from .models import Alumno, Materia


# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})


def crear_alumno(request):
    if request.method == 'POST':
        alumno_id = request.POST.get('id', None)
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        carrera = request.POST['carrera']
        semestre = request.POST['semestre']

        if alumno_id:
            Alumno.objects.filter(id=alumno_id).update(nombre=nombre, apellido=apellido, email=email, carrera=carrera, semestre=semestre)
            message = 'Alumno actualizado correctamente'
        else:
            Alumno.objects.create(nombre=nombre, apellido=apellido, email=email, carrera=carrera, semestre=semestre)
            message = 'Alumno creado correctamente'
        return render(request, 'crud-alumno/crear.html', {'message': message})

    alumno = Alumno.objects.get(id=request.GET.get('id', None)) if request.GET.get('id', None) else None
    return render(request, 'crud-alumno/crear.html', {'alumno': alumno})


def eliminar_alumo(request):
    if request.method == 'POST':
        id = request.POST['id']
        alumno = Alumno.objects.get(id=id)
        alumno.delete()
    return redirect('index')
