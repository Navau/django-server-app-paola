# Generated by Django 4.1.3 on 2022-12-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enfermedades', '0003_enfermedad_subtipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfermedad',
            name='paciente',
        ),
    ]
