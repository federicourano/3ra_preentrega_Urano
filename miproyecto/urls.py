"""
URL configuration for miproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from miproyecto import settings
#from .views import saludo, bienvenida, diaDeHoy, saludoPersonal, pruebaTemplate, crear_curso

urlpatterns = [
    path('admin/', admin.site.urls),

    path("miaplicacion/", include("miaplicacion.urls"))

    #path('saludar/', saludo), 
    #path('bienvenido/', bienvenida), 
    #path('hoy/', diaDeHoy), 
    #path('saludoPersonal/<nombre>/', saludoPersonal), 
    #path('testTemplate/', pruebaTemplate), 
    #path('crear_curso/<pnombre>/<pcomision>/', crear_curso), 
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)