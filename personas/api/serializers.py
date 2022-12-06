from rest_framework.serializers import ModelSerializer

from personas.models import Persona


class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'ci', 'nombre', 'apellido_paterno', 'apellido_materno',
                  'telefono', 'direccion', 'genero', 'fecha_nacimiento', 'ciudad', 'foto']
