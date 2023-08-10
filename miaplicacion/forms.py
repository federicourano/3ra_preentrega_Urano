from django import forms

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