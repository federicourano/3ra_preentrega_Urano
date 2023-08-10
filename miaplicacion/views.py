from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Create your views here.
def index(request):
    return render(request, "miaplicacion/base.html")

def buscarLibro(request):
    return render(request, "miaplicacion/buscarLibro.html")

def sagas(request):
    ctx = {"Sagas": Sagas.objects.all()}
    return render(request, "miaplicacion/sagas.html", ctx)

def SagasForm(request):
    if request.method == "POST":
        miForm = sagasForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            saga = Sagas(nombre=request.POST["nombre"], cantidadDeLibros=request.POST["cantidadDeLibros"])
            saga.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = sagasForm()
    return render(request, "miaplicacion/librosForm.html", {"form":miForm})

def updateSagas(request, id_saga):
    saga = Sagas.objects.get(id=id_saga)
    if request.method == "POST":
        miForm = sagasForm(request.POST)
        if miForm.is_valid():
            saga.nombre = miForm.cleaned_data.get("nombre")
            saga.cantidadDeLibros = miForm.cleaned_data.get("cantidadDeLibros")
            saga.save()
            return redirect(reverse_lazy("Sagas"))
    else:
        miForm = sagasForm(initial={"nombre":saga.nombre, 
                                     "cantidadDeLibros":saga.cantidadDeLibros})
    return render(request, "miaplicacion/sagasForm.html", {"form": miForm})  

def deleteSagas(request, id_saga):
    saga = Sagas.objects.get(id=id_saga)
    saga.delete()
    return redirect(reverse_lazy("Sagas"))

def buscar2(request):
    if request.GET["busqueda"]:
        busqueda = request.GET["busqueda"]
        libros = Libros.objects.filter(nombre__icontains=busqueda)
        print(libros)
        return render(request, "miaplicacion/resultados.html", {"busqueda":busqueda, "libros":libros})
    return HttpResponse("No se ingresaron datos para buscar")

class libroList(ListView):
    model = Libros

class libroCreate(CreateView):
    model = Libros
    fields = ['nombre', 'genero', 'cantidadDePaginas']
    success_url = reverse_lazy('Libros')

class libroDetail(DetailView):
    model = Libros

class libroUpdate(UpdateView):
    model = Libros
    fields = ['nombre', 'genero', 'cantidadDePaginas']
    success_url = reverse_lazy('Libros')    

class libroDelete(DeleteView):
    model = Libros
    success_url = reverse_lazy('Libros')

class autorList(ListView):
    model = Autor

class autorCreate(CreateView):
    model = Autor
    fields =["nombre", "apellido", "edad"]
    success_url = reverse_lazy("Autores")

class autorDetail(DetailView):
    model = Autor

class autorUpdate(UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'edad']
    success_url = reverse_lazy('Autores')    

class autorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('Autores')

class staffList(ListView):
    model = Staff

class staffCreate(CreateView):
    model = Staff
    fields = ['nombre', 'apellido', 'email', "dni"]
    success_url = reverse_lazy('Staff')

class staffDetail(DetailView):
    model = Staff

class staffUpdate(UpdateView):
    model = Staff
    fields = ['nombre', 'apellido', 'email', "dni"]
    success_url = reverse_lazy('Staff')    

class staffDelete(DeleteView):
    model = Staff
    success_url = reverse_lazy('Staff')

class sagaList(ListView):
    model = Sagas

class sagaCreate(CreateView):
    model = Sagas
    fields = ['nombre', 'cantidadDeLibros']
    success_url = reverse_lazy('Sagas')

class sagaDetail(DetailView):
    model = Sagas

class sagaUpdate(UpdateView):
    model = Sagas
    fields = ['nombre', 'cantidadDeLibros']
    success_url = reverse_lazy('Sagas')    

class sagaDelete(DeleteView):
    model = Sagas
    success_url = reverse_lazy('Sagas')