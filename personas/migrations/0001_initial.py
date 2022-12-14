# Generated by Django 4.1.3 on 2022-11-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=500, null=True)),
                ('genero', models.CharField(choices=[('MALE', 'Masculino'), ('FEMALE', 'Femenino'), ('UNDEFINED', 'Sin asignar'), ('OTHER', 'Otro')], default='Sin asignar', max_length=255)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=20, null=True)),
                ('foto', models.ImageField(upload_to='personas')),
            ],
        ),
    ]
