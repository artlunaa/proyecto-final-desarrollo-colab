from django.shortcuts import render, redirect
from .models import Alumno, Materia


def login(request):
    return render(request, 'login.html')


def panel(request):
    return render(request, 'panel.html')


# Create your views here.
def index_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno/tabla.html', {'alumnos': alumnos})


def crear_alumno(request):
    if request.method == 'POST':
        alumno_id = request.POST.get('id', None)
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        carrera = request.POST['carrera']
        semestre = request.POST['semestre']

        if alumno_id:
            Alumno.objects.filter(id=alumno_id).update(nombre=nombre, apellido=apellido, email=email, carrera=carrera,
                                                       semestre=semestre)
            message = 'Alumno actualizado correctamente'
        else:
            Alumno.objects.create(nombre=nombre, apellido=apellido, email=email, carrera=carrera, semestre=semestre)
            message = 'Alumno creado correctamente'
        return render(request, 'alumno/crear-editar.html', {'message': message})

    alumno = Alumno.objects.get(id=request.GET.get('id', None)) if request.GET.get('id', None) else None
    return render(request, 'alumno/crear-editar.html', {'alumno': alumno})


def eliminar_alumo(request):
    if request.method == 'POST':
        id = request.POST['id']
        alumno = Alumno.objects.get(id=id)
        alumno.delete()
    return redirect('alumno_index')


def index_materia(request):
    materias = Materia.objects.all()
    return render(request, 'materias/tabla.html', {'materias': materias})


def crear_materia(request):
    if request.method == 'POST':
        materia_id = request.POST.get('id', None)
        nombre = request.POST['nombre']
        creditos = request.POST['creditos']
        profesor = request.POST['profesor']

        if materia_id:
            Materia.objects.filter(id=materia_id).update(nombre=nombre, creditos=creditos, profesor=profesor)
            message = 'Materia actualizada correctamente'
        else:
            Materia.objects.create(nombre=nombre, creditos=creditos, profesor=profesor)
            message = 'Materia creada correctamente'

        return render(request, 'materias/crear-editar.html', {'message': message})

    materia = Materia.objects.get(id=request.GET.get('id', None)) if request.GET.get('id', None) else None
    return render(request, 'materias/crear-editar.html', {'materia': materia})


def eliminar_materia(request):
    if request.method == 'POST':
        id = request.POST['id']
        materia = Materia.objects.get(id=id)
        materia.delete()
    return redirect('materia_index')
