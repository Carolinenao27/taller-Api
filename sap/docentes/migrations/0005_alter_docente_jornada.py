# Generated by Django 4.2.2 on 2023-07-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0004_universidad_docente_universidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='jornada',
            field=models.CharField(choices=[('Matutino', 'MATUTINO'), ('Vespertino', 'VESPERTINO'), ('Nocturno', 'NOCTURNO')], max_length=10, null=True),
        ),
    ]
