from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
from usuarios.api.serializers import UsuarioSerializer

from usuarios.models import Usuario


class UsuarioApiViewSet(ModelViewSet):
    # Se especifica quien va a utilizar los endpoints, en este caso solo los administradores
    # permission_classes = [IsAdminUser]
    # Como queremos que nos devuelvan los datos, es como un transformador de datos
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()  # A que modelo tiene que atacar

    # PARA ENCRIPTAR LA CONTRASEÑA AL CREAR EL USUARIO
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        # print("REQUEST_DATA", request.data)
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if hasattr(request.data, 'password'):
            password = request.data['password']
            if password:
                request.data['password'] = make_password(password)
            else:
                request.data['password'] = request.user.password
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)


class UsuarioView(APIView):
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
