"""
URL configuration for sap project.

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
from django.urls import path

from docentes.views import agregar_docente, ver_docente, editar_docente, eliminar_docente
from webapp.views import mostrar_docentes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_docentes, name= 'inicio'),
    path('agregar_docentes/', agregar_docente),
    path('ver_docente/<int:idDocente>', ver_docente),
    path('editar_docente/<int:idDocente>', editar_docente),
    path('eliminar_docente/<int:idDocente>', eliminar_docente),

]

