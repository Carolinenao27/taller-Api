from django.contrib import admin

from docentes.models import Docente, Materia, Alumno

# Register your models here.
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Alumno)