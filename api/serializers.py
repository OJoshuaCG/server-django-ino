from rest_framework import serializers
from .models import Usuario, Hogar, \
        Dispositivo, Control, Informe


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('id_usuario', )


class HogarSerializar(serializers.ModelSerializer):
    class Meta:
        model = Hogar
        fields = '__all__'
        read_only_fields = ('id_hogar', )


class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'
        read_only_fields = ('id_dispositivo', )


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'


class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe
        fields = '__all__'
