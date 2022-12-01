from dotenv import load_dotenv
from os import getenv
from pyfirmata import Arduino
from rest_framework import viewsets, status, response
from rest_framework.decorators import detail_route
from .models import Informe
from .serializers import InformeSerializer


load_dotenv()
PORT = getenv('ARDUINO_PORT')
BOARD = Arduino(PORT)


class Controlador(viewsets.ViewSet):
    def digitalWrite(self, pin, valor):
        try:
            self.BOARD.digital[pin].write(valor)
            return True
        except:
            return False


    def digitalRead(self, pin, valor):
        try:
            valor = self.BOARD.digital[pin].read()
            return valor
        except:
            return False


    def analogWrite(self, pin, valor):
        try:
            pin = f"A{pin}"
            self.BOARD.analog[pin].write(valor)
            return True
        except:
            return False


    def analogRead(self, pin, valor):
        try:
            pin = f"A{pin}"
            valor = self.BOARD.analog[pin].read()
            return valor
        except:
            return False


    def pwmWrite(self, pin, valor):
        try:
            self.BOARD.analog[pin].wirte(valor)
            return True
        except:
            return False


    def pwmRead(self, pin, valor):
        try:
            valor = self.BOARD.analog[pin].read()
            return valor
        except:
            return False


    TURING = [
        [digitalWrite, digitalRead],
        [analogWrite, analogRead],
        [pwmWrite, pwmRead],
    ]

    SENALES = {
        "Analoga":0,
        "A":0,
        "Digital":1,
        "D":1,
        "PWM":2,
        "P":2,
    }

    TIPOS = {
        "Actuador":0,
        "A":0,
        "Sensor":1,
        "S":1,
    }


    def interaccion(self, request):
        pin = request.pin
        senal = request.senal
        tipo = request.tipo
        valor = request.valor

        i, j = self.SENALES[senal], self.TIPOS[tipo]
        estado = self.TURING[i][j](pin, valor)
        
        if(estado):
            return response.Response(
                status=status.HTTP_200_OK,
            )
        
        return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
        )
