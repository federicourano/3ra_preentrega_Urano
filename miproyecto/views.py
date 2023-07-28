from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
#from miaplicacion.models import Curso

def saludo(request):
    return HttpResponse("Hola Mundo!!!")

def bienvenida(request):
    return HttpResponse("<html><h1>Bienvenidos a Django con Python!</h1></html>")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    respuestaDia = f"Hoy es : <br> {dia}"
    return HttpResponse(respuestaDia)

def saludoPersonal(request, nombre):
    saludo = f"Bienvenido {nombre}!"
    return HttpResponse(saludo)

def pruebaTemplate(request):
    
    plantilla = loader.get_template("index.html")
    datos = {
        'nombre': 'JUAN PABLO',
        'apellido': 'RODRIGUEZ',
        'dni': 12345678,
        'fecha_hoy': datetime.datetime.now(),
        'notas': [7,8,10,5,4,3],
    }
    documento = plantilla.render(datos)
    return HttpResponse(documento)

#def crear_curso(request, pnombre, pcomision):
    #curso = Curso(nombre=pnombre, comision=pcomision)
    #curso.save()

    #respuesta = f"El curso creado fue {curso.nombre} de la comision {curso.comision}"
    #return HttpResponse(respuesta)

