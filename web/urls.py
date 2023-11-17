from django.urls import path
from .views import index, crear_alumno, eliminar_alumo

urlpatterns = [
    path('alumnos', index, name="index"),
    path('alumnos/crear_alumno', crear_alumno, name="crear_alumno"),
    path('alumnos/eliminar_alumno', eliminar_alumo, name="eliminar_alumno"),
]
