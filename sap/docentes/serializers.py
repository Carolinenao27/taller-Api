from rest_framework import serializers

from docentes.models import Docente, Materia


class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ['nombre']

class DocenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'email', 'materia']