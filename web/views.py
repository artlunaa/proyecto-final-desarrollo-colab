from django.shortcuts import render, redirect
from .models import Alumno, Materia, Calificaciones
from django.contrib.auth import login as auth_login, authenticate


def login(request):
    message = None
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect('panel')
            else:
                message = 'El usuario o contraseña son incorrectos'
    return render(request, 'login.html', {'message': message})


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

    id = request.GET.get('id', None)
    if id:
        alumno = Alumno.objects.get(id=id)
        calificaciones = Calificaciones.objects.filter(alumno_id=id)
    else:
        calificaciones = alumno = None
    return render(request, 'alumno/crear-editar.html', {'alumno': alumno, 'calificaciones': calificaciones})


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


def inscribir_alumno_a_materia(request):
    message = None
    if request.method == 'POST':
        id_alumno = request.POST['id_alumno']
        id_materia = request.POST['id_materia']
        alumno = Alumno.objects.get(id=id_alumno)
        materia = Materia.objects.get(id=id_materia)
        alumno.materias.add(materia)
        alumno.save()
        message = f'Alumno inscrito a "{materia.nombre}" correctamente'
    alumnos = Alumno.objects.all()
    materias = Materia.objects.all()
    return render(request, 'inscribir-alumnos-a-materias.html',
                  {'messsage': message, 'alumnos': alumnos, 'materias': materias})


def captura_calificaciones(request):
    message = None
    id = request.GET.get('id', None)
    alumno = Alumno.objects.get(id=id)
    materias = alumno.materias.all()
    # calificaciones = alumno.calificaciones_set.all().prefetch_related('materia')
    if request.method == 'POST':
        id = request.POST['id_alumno']
        id_materia = request.POST['id_materia']
        calificacion = request.POST['calificacion']
        Calificaciones.objects.create(alumno_id=id, materia_id=id_materia, calificacion=calificacion)
        message = 'Calificacion registrada correctamente'

    return render(request, 'captura-calificaciones.html',
                  {'alumno': alumno, 'materias': materias, 'message': message})
