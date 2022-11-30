# Sources
# https://docs.djangoproject.com/en/4.1/topics/db/models/
# https://docs.djangoproject.com/en/4.1/ref/models/fields/#smallintegerfield

from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50)
    

class Hogar(models.Model):
    id_hogar = models.AutoField(primary_key=True)
    # codigo_hogar = models.IntegerField()
    nombre = models.CharField(max_length=30)
    pin = models.SmallIntegerField()
    lugar = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)


class Modulo(models.Model):
    TIPOS = (
        ('A', "Actuador"),
        ('S', "Sensor"),
    )
    SENALES = (
        ('A', "Analoga"),
        ('D', "Digital"),
        ('P', "PWM"),
    )
    id_modulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    senal = models.CharField(max_length=1, choices=SENALES)


class Dispositivo(models.Model):
    ESTADOS = (
        ('0', "Apagado"),
        ('1', "Encendido")
    )
    id_dispositivo = models.AutoField(primary_key=True)
    id_hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE)
    id_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADOS)
    valor = models.SmallIntegerField()


class Control(models.Model):
    id_usuario = models.ForeignKey(Usuario, 
        on_delete=models.CASCADE)
    id_hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)


class Informe(models.Model):
    id_usuario = models.ForeignKey(Usuario, 
        on_delete=models.SET_NULL, blank=True, null=True)
    id_hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE)
    id_dispositivo = models.ForeignKey(Dispositivo, 
        on_delete=models.CASCADE)
    valor_antes = models.IntegerField()
    valor_actual = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)




    