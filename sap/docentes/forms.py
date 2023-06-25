from django.forms import ModelForm, EmailInput

from docentes.models import Docente


class DocenteFormulario(ModelForm):
    class Meta:
        model = Docente
        fields = ('nombre', 'apellido', 'email', 'materia')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }