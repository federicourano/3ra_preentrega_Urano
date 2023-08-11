from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LibrosForm(forms.Form):
    nombre = forms.CharField(label="Nombre del libro", max_length=50, required=True)
    genero = forms.CharField(label="Genero del libro", max_length=50, required=True)
    cantidadDePaginas = forms.IntegerField(label="Cantidad de paginas", required=True)

class autorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del autor", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del autor", max_length=50, required=True)
    edad = forms.IntegerField(label="Edad del autor", required=True)

class staffForm(forms.Form):
    nombre = forms.CharField(label="Nombre del staff", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del staff", max_length=50, required=True)
    email = forms.EmailField(label="Email del staff", required=True)
    dni = forms.IntegerField(label="DNI del staff", required=True)

class sagasForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la saga", max_length=50, required=True)
    cantidadDeLibros = forms.IntegerField(label="Cantidad de libros", required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label= "Email modificado")
    password1 = forms.CharField(label = "Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contrasela", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class avatarForm(forms.Form):
    imagen = forms.ImageField(required=True)