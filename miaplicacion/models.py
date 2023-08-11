from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Libros(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    cantidadDePaginas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Staff(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Sagas(models.Model):
    nombre = models.CharField(max_length=50)
    cantidadDeLibros = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __srt__(self):
        return f"{self.user} [{self.imagen}]"