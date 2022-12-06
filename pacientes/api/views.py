from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from pacientes.models import Paciente
from pacientes.api.serializers import PacienteSerializer


class PacienteApiViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['usuario__persona__ci', 'usuario__persona__nombre',
                     'usuario__persona__apellido_paterno', 'usuario__persona__apellido_materno']
