from django.contrib import admin

from docentes.models import Docente, Materia, Alumno, Universidad

# Register your models here.
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Alumno)
admin.site.register(Universidad)