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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
    return render(request, "miaplicacion/base.html")

def acercaDeMi(request):
    return render(request, "miaplicacion/acercaDeMi.html")

@login_required
def buscarLibro(request):
    return render(request, "miaplicacion/buscarLibro.html")

@login_required
def buscar2(request):
    if request.GET["busqueda"]:
        busqueda = request.GET["busqueda"]
        libros = Libros.objects.filter(nombre__icontains=busqueda)
        print(libros)
        return render(request, "miaplicacion/resultados.html", {"busqueda":busqueda, "libros":libros})
    return HttpResponse("No se ingresaron datos para buscar")

class libroList(LoginRequiredMixin, ListView):
    model = Libros

class libroCreate(LoginRequiredMixin, CreateView):
    model = Libros
    fields = ['nombre', 'genero', 'cantidadDePaginas']
    success_url = reverse_lazy('Libros')

class libroDetail(LoginRequiredMixin, DetailView):
    model = Libros

class libroUpdate(LoginRequiredMixin, UpdateView):
    model = Libros
    fields = ['nombre', 'genero', 'cantidadDePaginas']
    success_url = reverse_lazy('Libros')    

class libroDelete(LoginRequiredMixin, DeleteView):
    model = Libros
    success_url = reverse_lazy('Libros')

class autorList(LoginRequiredMixin, ListView):
    model = Autor

class autorCreate(LoginRequiredMixin, CreateView):
    model = Autor
    fields =["nombre", "apellido", "edad"]
    success_url = reverse_lazy("Autores")

class autorDetail(LoginRequiredMixin, DetailView):
    model = Autor

class autorUpdate(LoginRequiredMixin, UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'edad']
    success_url = reverse_lazy('Autores')    

class autorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy('Autores')

class staffList(LoginRequiredMixin, ListView):
    model = Staff

class staffCreate(LoginRequiredMixin, CreateView):
    model = Staff
    fields = ['nombre', 'apellido', 'email', "dni"]
    success_url = reverse_lazy('Staff')

class staffDetail(LoginRequiredMixin, DetailView):
    model = Staff

class staffUpdate(LoginRequiredMixin, UpdateView):
    model = Staff
    fields = ['nombre', 'apellido', 'email', "dni"]
    success_url = reverse_lazy('Staff')    

class staffDelete(LoginRequiredMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy('Staff')

class sagaList(LoginRequiredMixin, ListView):
    model = Sagas

class sagaCreate(LoginRequiredMixin, CreateView):
    model = Sagas
    fields = ['nombre', 'cantidadDeLibros']
    success_url = reverse_lazy('Sagas')

class sagaDetail(LoginRequiredMixin, DetailView):
    model = Sagas

class sagaUpdate(LoginRequiredMixin, UpdateView):
    model = Sagas
    fields = ['nombre', 'cantidadDeLibros']
    success_url = reverse_lazy('Sagas')    

class sagaDelete(LoginRequiredMixin, DeleteView):
    model = Sagas
    success_url = reverse_lazy('Sagas')

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            clave = miForm.cleaned_data.get("password")
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.jpg'
                finally:
                    request.session['avatar'] = avatar
                return render(request, "miaplicacion/base.html")
            else:
                return render(request, "mimiaplicacion/login.html", {"form":miForm, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "miaplicacion/login.html", {"form":miForm, "mensaje": "Usuario o contraseña incorrectos"})
    miForm = AuthenticationForm()
    return render(request, "miaplicacion/login.html", {"form":miForm})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) 
        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "miaplicacion/base.html", {"mensaje":"Usuario Creado exitosamente"})        
    else:
        form = RegistroUsuariosForm()

    return render(request, "miaplicacion/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get("email")
            usuario.first_name = form.cleaned_data.get("first_name")
            usuario.last_name = form.cleaned_data.get("last_name")
            usuario.save()
            return render(request, "miaplicacion/base.html")
        else:
            return render(request, "miaplicacion/editarForm.html", {"form":form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "miaplicacion/editarForm.html", {"form":form, "usuario":usuario.username})

@login_required
def editarPassword(request):
    usuario = request.user
    if request.method == "POST":
        form = PasswordChangeForm(user=usuario, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "miaplicacion/base.html")
        else:
            return render(request, "miaplicacion/editarForm.html", {"form":form})
    else:
        form = PasswordChangeForm(user=usuario)
    return render(request, "miaplicacion/editarForm.html", {"form":form, "usuario":usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = avatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "miaplicacion/base.html")
    else:
        form = avatarForm()
    return render(request, "miaplicacion/agregarAvatar.html", {"form":form})
