import random


class Dado:
    __caras = 6

    def __init__(self, fcaras):
        self.setCaras(fcaras)

    def lanzar(self):
        return random.randint(1, self.__caras)

    def getCaras(self):
        return self.__caras

    def setCaras(self, fcaras):
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numere de cares incorrecte")
