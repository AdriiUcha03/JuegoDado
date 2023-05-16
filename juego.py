import dado


class Juego:
    __jugador1 = ""
    __jugador2 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, caras1, caras2, caras3, caras4, lanzamientos, visualizar_proceso):
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        self.dado4 = dado.Dado(caras4)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (visualizar_proceso in ("S", "s"))
        self.resultado_jugador1 = 0
        self.resultado_jugador2 = 0

    def set_jugador1(self, fjugador1):
        if len(fjugador1) > 20:
            raise Exception("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador2 = fjugador2

    def set_lanzamientos(self, flanzamientos):
        if not 2 < flanzamientos < 1000:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 100")
        else:
            self.__lanzamientos = flanzamientos

    def lanzar_dados(self):
        for x in range(self.__lanzamientos):
            # jugador1
            resul_dado1 = self.dado1.lanzar()
            resul_dado2 = self.dado2.lanzar()
            resul_dado3 = self.dado3.lanzar()
            resul_dado4 = self.dado4.lanzar()
            self.resultado_jugador1 += (resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)

            if self.__intermedios:
                print(f"{self.__jugador1}: {resul_dado1} {resul_dado2} {resul_dado3} "
                      f"({(resul_dado1 + resul_dado2 + resul_dado3)})")

            # jugador2
            resul_dado1 = self.dado1.lanzar()
            resul_dado2 = self.dado2.lanzar()
            resul_dado3 = self.dado3.lanzar()
            resul_dado4 = self.dado4.lanzar()
            self.resultado_jugador2 += (resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)

            if self.__intermedios:
                print(f"{self.__jugador2}: {resul_dado1} {resul_dado2} {resul_dado3} {resul_dado4} "
                      f"({(resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)})")

    def mostrar_resultado(self):
        print("Resultados:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Numero de lanzamientos: {self.__lanzamientos}")
        print(f"Dados: {self.dado1.getCaras()},{self.dado2.getCaras()},{self.dado3.getCaras()}y{self.dado4.getCaras()}")
        print(f"Puntos jugador 1: {self.resultado_jugador1}")
        print(f"Puntos jugador 2: {self.resultado_jugador2}")
        if self.resultado_jugador1 > self.resultado_jugador2:
            print(f"El GANADOR es {self.__jugador1} con {self.resultado_jugador1} puntos")
        elif self.resultado_jugador1 == self.resultado_jugador2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.__jugador2} con {self.resultado_jugador2} puntos")
