from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "miaplicacion/base.html")

def libros(request):
    ctx = {"Libros": Libros.objects.all()}
    return render(request, "miaplicacion/libros.html", ctx)

def librosForm(request):
    if request.method == "POST":
        miForm = LibrosForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            libro = Libros(nombre=request.POST["nombre"], genero=request.POST["genero"], cantidadDePaginas=request.POST["cantidadDePaginas"])
            libro.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = LibrosForm()
    return render(request, "miaplicacion/librosForm.html", {"form":miForm})

def buscarLibro(request):
    return render(request, "miaplicacion/buscarLibro.html")

def autores(request):
    ctx = {"Autores": Autor.objects.all()}
    return render(request, "miaplicacion/autores.html", ctx)

def autoresForm(request):
    if request.method == "POST":
        miForm = autorForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            autor = Autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad=request.POST["edad"])
            autor.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = autorForm()
    return render(request, "miaplicacion/autoresForm.html", {"form":miForm})

def staff(request):
    ctx = {"Staff": Staff.objects.all()}
    return render(request, "miaplicacion/staff.html", ctx)

def StaffForm(request):
    if request.method == "POST":
        miForm = staffForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            staff = Staff(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"], dni=request.POST["dni"])
            staff.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = staffForm()
    return render(request, "miaplicacion/staffForm.html", {"form":miForm})

def buscar2(request):
    if request.GET["busqueda"]:
        busqueda = request.GET["busqueda"]
        libro = Libros.objects.filter(nombre__icontains=busqueda)
        print(libro)
        return render(request, "miaplicacion/resultados.html", {"busqueda":busqueda, "libro":libro})
    return HttpResponse("No se ingresaron datos para buscar")
