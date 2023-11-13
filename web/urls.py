from django.urls import path
from .views import index, crear_alumno

urlpatterns = [
    path('', index, name="index"),
    path('crear_alumno', crear_alumno, name="crear_alumno")
]
