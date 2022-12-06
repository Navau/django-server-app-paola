from rest_framework.serializers import ModelSerializer

from enfermedades.models import Enfermedad


class EnfermedadSerializer(ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ['id', 'nombre', 'subtipo', 'descripcion', 'estado']
