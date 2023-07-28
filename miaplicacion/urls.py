from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="Inicio"),
    path('libros/', libros, name="Libros"),
    path('autores/', autores, name="Autores"),
    path('staff/', staff, name="Staff"),

    path('libroform/', librosForm, name="libroform"),
    path('autorform/', autoresForm, name="autorform"),
    path('staffform/', StaffForm, name="staffform"),

    path('buscarlibro/', buscarLibro, name="buscarlibro"),
    path('buscar2/', buscar2, name="buscar2"),
]