import random


class Bolos:
    def __init__(self):
        self.puntuacionRonda = []
        self.puntuacionPartida = []
        self.marcador = 0
    
    def bolosTirados(self):
        a = random.randint(0,10)
        return a
    
    def anotacion(self):
        for puntuacion in range(0,3):
            self.puntuacionRonda.append(self.bolosTirados())

    def marcador(self):
        for puntuacion in self.puntuacionPartida:
            self.marcador = self.marcador + puntuacion

