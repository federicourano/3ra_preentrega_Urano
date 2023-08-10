from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="Inicio"),

    path('libros/', libroList.as_view(), name="Libros"),
    path('create_libros/', libroCreate.as_view(), name="create_libro"),
    path('detail_libros/<int:pk>/', libroDetail.as_view(), name="detail_libro"),
    path('update_libros/<int:pk>/', libroUpdate.as_view(), name="update_libro"),
    path('delete_libros/<int:pk>/', libroDelete.as_view(), name="delete_libro"),
    path('buscarlibro/', buscarLibro, name="buscarlibro"),
    path('buscar2/', buscar2, name="buscar2"),

    path('autores/', autorList.as_view(), name="Autores"),
    path('create_autor/', autorCreate.as_view(), name="create_autor"),
    path('detail_autor/<int:pk>/', autorDetail.as_view(), name="detail_autor"),
    path('update_autor/<int:pk>/', autorUpdate.as_view(), name="update_autor"),
    path('delete_autor/<int:pk>/', autorDelete.as_view(), name="delete_autor"),

    path('staff/', staffList.as_view(), name="Staff"),
    path('create_staff/', staffCreate.as_view(), name="create_staff"),
    path('detail_staff/<int:pk>/', staffDetail.as_view(), name="detail_staff"),
    path('update_staff/<int:pk>/', staffUpdate.as_view(), name="update_staff"),
    path('delete_staff/<int:pk>/', staffDelete.as_view(), name="delete_staff"),

    path('sagas/', sagaList.as_view(), name="Sagas"),
    path('create_saga/', sagaCreate.as_view(), name="create_saga"),
    path('detail_saga/<int:pk>/', sagaDetail.as_view(), name="detail_saga"),
    path('update_saga/<int:pk>/', sagaUpdate.as_view(), name="update_saga"),
    path('delete_saga/<int:pk>/', sagaDelete.as_view(), name="delete_saga"),
]