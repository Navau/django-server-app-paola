from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from enfermedades.models import Enfermedad
from enfermedades.api.serializers import EnfermedadSerializer


class EnfermedadApiViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EnfermedadSerializer
    queryset = Enfermedad.objects.all()
