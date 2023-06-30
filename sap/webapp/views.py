from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from docentes.models import Docente


# Create your views here.
def mostrar_docentes(request):
     cantidad_docentes = Docente.objects.count()
     pagina = loader.get_template('docentes.html')
     #nombres_docentes = Docente.objects.all()
     nombres_docentes = Docente.objects.order_by('apellido')
     datos = {'cantidad': cantidad_docentes, 'docentes':nombres_docentes}


     return HttpResponse(pagina.render(datos, request))