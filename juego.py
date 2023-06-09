import dado


class Juego:
    """
    #CLASE JUEGO DE TIRAR DADOS
    ### Clase juego en la que tenemos diferentes funciones con las que checkeamos y gestionamos los parametros introducidos
    en el objeto
    """
    # Objetos privados par asi utilizar setters para validar(el get se hace dentro del setter)
    __jugador1 = ""
    __jugador2 = ""
    __jugador3 = ""
    __lanzamientos = 0

    def __init__(self, jugador1, jugador2, jugador3, caras1, caras2, caras3, caras4, lanzamientos, visualizar_proceso):
        """
        Inicializador de la clase
        :param jugador1: Nombre de **jugador** uno pasa por la funcion de set para validar
        :param jugador2: Nombre de **jugador** dos pasa por la funcion de set para validar
        :param jugador3: Nombre de **jugador** tres pasa por la funcion de set para validar
        :param caras1: Caras1 pasa a la clase dado si no cumple la condicion del condicional
        :param caras2: Caras2 pasa a la clase dado si no cumple la condicion del condicional
        :param caras3: Caras3 pasa a la clase dado si no cumple la condicion del condicional
        :param caras4: Caras4 pasa a la clase dado si no cumple la condicion del condicional
        :param lanzamientos: Lanzamientos pasan por la funcion set para validar
        :param visualizar_proceso: Boolean para ver si se quiere mostrar el proceso o no
        """
        self.set_jugador1(jugador1)
        self.set_jugador2(jugador2)
        self.set_jugador3(jugador3)
        self.set_lanzamientos(lanzamientos)
        # Validador de condicionales para comprobar que las 4 caras sean diferentes si
        # dos son iguales salta la Excepcion
        if caras1 == caras2 or caras1 == caras3 or caras1 == caras4:
            raise Exception("Les cares dels daus no poden ser iguals")
        elif caras2 == caras1 or caras2 == caras3 or caras2 == caras4:
            raise Exception("Les cares dels daus no poden ser iguals")
        elif caras3 == caras2 or caras3 == caras1 or caras3 == caras4:
            raise Exception("Les cares dels daus no poden ser iguals")
        elif caras4 == caras2 or caras4 == caras3 or caras4 == caras1:
            raise Exception("Les cares dels daus no poden ser iguals")
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(caras2)
        self.dado3 = dado.Dado(caras3)
        self.dado4 = dado.Dado(caras4)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (visualizar_proceso in ("S", "s"))
        self.resultado_jugador1 = 0
        self.resultado_jugador2 = 0
        self.resultado_jugador3 = 0

    def set_jugador1(self, fjugador1):
        """
        Validación de que jugador 1 no tenga como nombre mas de 20 caracteres
        :param fjugador1: Variable que se le pasa del inicializador cuando se llama a la funcion
        :return: Si no cumple la condición se asigna a la variable privada
        """
        if len(fjugador1) > 20:
            raise Exception("La longitud del nom del jugador 1 no pot ser major de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        """
        Validación de que jugador 2 no tenga como nombre mas de 20 caracteres
        :param fjugador2: Variable que se le pasa del inicializador cuando se llama a la funcion
        :return: Si no cumple la condición se asigna a la variable privada
        """
        if len(fjugador2) > 20:
            raise Exception("La longitud del nom del jugador 2 no pot ser major de 20")
        else:
            self.__jugador2 = fjugador2

    def set_jugador3(self, fjugador3):
        """
        Validación de que jugador 3 no tenga como nombre mas de 20 caracteres
        :param fjugador3: Variable que se le pasa del inicializador cuando se llama a la funcion
        """
        if len(fjugador3) > 20:
            raise Exception("La longitud del nom del jugador 3 no pot ser major de 20")
        else:
            self.__jugador3 = fjugador3

    def set_lanzamientos(self, flanzamientos):
        """
        Validacion de que el numero de lanzamientos esta dentro del rango
        :param flanzamientos: Variable que se le pasa del inicializador cuando se llama a la funcion
        """
        if not 2 < flanzamientos < 1000:
            raise Exception("El nombre de llançaments ha d'estar entre 2 i 1000")
        else:
            self.__lanzamientos = flanzamientos

    def lanzar_dados(self):
        """
        Funcion que lanza los dados y llama a la función dado para realizar la suma de los lanzamientos y conseguir
        los puntos
        """
        for x in range(self.__lanzamientos):
            # jugador1
            resul_dado1 = self.dado1.lanzar()
            resul_dado2 = self.dado2.lanzar()
            resul_dado3 = self.dado3.lanzar()
            resul_dado4 = self.dado4.lanzar()
            self.resultado_jugador1 += (resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)

            if self.__intermedios:
                print(f"{self.__jugador1}: {resul_dado1} {resul_dado2} {resul_dado3} {resul_dado4}"
                      f"({(resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)})")

            # jugador2
            resul_dado1 = self.dado1.lanzar()
            resul_dado2 = self.dado2.lanzar()
            resul_dado3 = self.dado3.lanzar()
            resul_dado4 = self.dado4.lanzar()
            self.resultado_jugador2 += (resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)

            if self.__intermedios:
                print(f"{self.__jugador2}: {resul_dado1} {resul_dado2} {resul_dado3} {resul_dado4} "
                      f"({(resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)})")

            # jugador 3
            resul_dado1 = self.dado1.lanzar()
            resul_dado2 = self.dado2.lanzar()
            resul_dado3 = self.dado3.lanzar()
            resul_dado4 = self.dado4.lanzar()
            self.resultado_jugador3 += (resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)

            if self.__intermedios:
                print(f"{self.__jugador2}: {resul_dado1} {resul_dado2} {resul_dado3} {resul_dado4} "
                      f"({(resul_dado1 + resul_dado2 + resul_dado3 + resul_dado4)})")

    def mostrar_resultado(self):
        """
        Función que muestra el resultado de la partida y el ganador
        """
        print("Resultats:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Jugador 3: {self.__jugador3}")
        print(f"Numere de llançaments: {self.__lanzamientos}")
        print(f"Daus: {self.dado1.getCaras()},{self.dado2.getCaras()},{self.dado3.getCaras()}y{self.dado4.getCaras()}")
        print(f"Punts jugador 1: {self.resultado_jugador1}")
        print(f"Punts jugador 2: {self.resultado_jugador2}")
        print(f"Punts jugador 3: {self.resultado_jugador3}")
        if self.resultado_jugador1 > self.resultado_jugador2 and self.resultado_jugador1 > self.resultado_jugador3:
            print(f"El GUANYADOR és {self.__jugador1} con {self.resultado_jugador1} punts")
        elif self.resultado_jugador2 > self.resultado_jugador1 and self.resultado_jugador2 > self.resultado_jugador3:
            print(f"El GUANYADOR és {self.__jugador1} con {self.resultado_jugador1} punts")
        elif self.resultado_jugador3 > self.resultado_jugador1 and self.resultado_jugador3 > self.resultado_jugador2:
            print(f"El GUANYADOR és {self.__jugador1} con {self.resultado_jugador1} punts")
        elif self.resultado_jugador1 == self.resultado_jugador2 and self.resultado_jugador1 == self.resultado_jugador3:
            print("Hi ha hagut un EMPAT")
