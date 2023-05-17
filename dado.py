import random


class Dado:
    # Variable privada de asignación de caras
    __caras = 6

    def __init__(self, fcaras):
        """
        Inicializador de la clase que lleva al validador setCaras
        :param fcaras: Variable que se pasa de juego a validar.
        """
        self.setCaras(fcaras)

    def lanzar(self):
        """
        :return: Retorna el numero aleatorio del lanzamiento
        """
        return random.randint(1, self.__caras)

    def getCaras(self):
        """
        :return: Retorna la variable privada
        """
        return self.__caras

    def setCaras(self, fcaras):
        """
        Valida si cumple las condición de caras_permitidas
        :param fcaras: Variable que se pasa de juego con el numero de caras del dado
        :return:
        """
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numere de cares incorrecte")
