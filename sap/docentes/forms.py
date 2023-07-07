from django.forms import ModelForm, EmailInput

from docentes.models import Docente


class DocenteFormulario(ModelForm):
    class Meta:
        model = Docente
        fields = ('nombre', 'apellido', 'sexo','email', 'materia','universidad','jornada')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }