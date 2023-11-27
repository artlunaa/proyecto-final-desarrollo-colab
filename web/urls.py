from django.urls import path
from .views import index_alumno, crear_alumno, eliminar_alumo, index_materia, crear_materia, eliminar_materia, login, \
    panel, inscribir_alumno_a_materia, captura_calificaciones

urlpatterns = [
    path('', login, name="login"),
    path('panel', panel, name="panel"),

    path('alumnos', index_alumno, name="alumno_index"),
    path('alumnos/crear_alumno', crear_alumno, name="crear_alumno"),
    path('alumnos/eliminar_alumno', eliminar_alumo, name="eliminar_alumno"),

    path('materias', index_materia, name="materia_index"),
    path('materias/crear_materia', crear_materia, name="crear_materia"),
    path('materias/eliminar_materia', eliminar_materia, name="eliminar_materia"),

    path('inscribir-alumnos-a-materias', inscribir_alumno_a_materia, name="inscribir_alumno_a_materia"),
    path('captura-calificaciones', captura_calificaciones, name="captura_calificaciones"),
]
