import juego
# Creación de la clase juego y relleno de los parametros para jugar al juego dado
juego = juego.Juego(str(input("Introdueix el nom del primer jugador: ")),
                    str(input("Introdueix el nom del segon jugador: ")),
                    str(input("Introdueix el nom del tercer jugador: ")),
                    int(input("Introdueix el numere de cares per al primer dau: ")),
                    int(input("Introdueix el numere de cares per al segon dau: ")),
                    int(input("Introdueix el numere de cares per al tercer dau: ")),
                    int(input("Introdueix el numere de cares per al quart dau: ")),
                    int(input("Introdueix el numere de llançaments: ")),
                    input("Vols veure els resultats intermedis per pantalla? (S/N): "))


juego.lanzar_dados()
juego.mostrar_resultado()
