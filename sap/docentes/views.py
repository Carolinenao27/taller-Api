from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader


from docentes.forms import DocenteFormulario
from docentes.models import Docente

# Create your views here.

def agregar_docente(request):
    pagina = loader.get_template('agregar_docentes.html')
    if request.method == 'GET':
         formulario = DocenteFormulario
    elif request.method == 'POST':
        formulario = DocenteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_docente(request, idDocente):
    pagina = loader.get_template('ver_docentes.html')
    docente = get_object_or_404(Docente, pk=idDocente)
    mensaje = {'docente': docente}
    return HttpResponse(pagina.render(mensaje, request))



def editar_docente(request, idDocente):
    pagina = loader.get_template('editar_docentes.html')
    docente = get_object_or_404(Docente, pk=idDocente)
    if request.method == "GET":
        formulario = DocenteFormulario(instance=docente)

    elif request.method == "POST":
        formulario = DocenteFormulario(request.POST, instance=docente)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

    mensaje = {'formulario': formulario}

    return HttpResponse(pagina.render(mensaje, request))

def eliminar_docente(request, idDocente):
    docente = get_object_or_404(Docente, pk=idDocente)
    if docente:
        docente.delete()
        return redirect('inicio')
from django.shortcuts import render

# Create your views here.
