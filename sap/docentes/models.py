from django.core.exceptions import ValidationError
from django.db import models

class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.nombre}'
class Materia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.nombre}'
class Docente(models.Model):
    JORNADA = [
        ("Matutino", "MATUTINO"),
        ("Vespertino", "VESPERTINO"),
        ("Nocturno", "NOCTURNO"),
    ]

    SEXO = [
        ("M", "MASCULINO"),
        ("F", "FEMENINO"),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, null=True)
    jornada = models.CharField(max_length=10, choices=JORNADA, null=True)

    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido} {self.materia} '
class Alumno(models.Model):
    SEXO = [
        ("M", "MASCULINO"),
        ("F", "FEMENINO"),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} - {self.nombre} {self.apellido}'