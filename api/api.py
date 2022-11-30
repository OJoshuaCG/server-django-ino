from .models import Usuario, Hogar, \
        Dispositivo, Control, Informe
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer, HogarSerializar, \
        DispositivoSerializer, ControlSerializer, InformeSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer


class HogarViewSet(viewsets.ModelViewSet):
    queryset = Hogar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HogarSerializar


class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DispositivoSerializer


class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ControlSerializer


class InformeViewSet(viewsets.ModelViewSet):
    queryset = Informe.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InformeSerializer