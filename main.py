from random import randrange
from os import system
import sys

from tablero import Tablero
from jugadores.persona import Persona
from jugadores.pc import Pc

class Tic_tac_toe(object):

    def comenzar_partida(self):
        """
        Comenzar partida declara los jugadores, quien comienza el turno, y da comienzo a la partida.
        En caso de hallar un ganador se termina la partida. Caso contratio la partida finaliza cuando no hallan
        mas movimientos posibles.
        """
        ganador = None
        seleccion = int(self.mostrar_menu())
        jugadores = {
            1: self.definir_jugadores_PVP,
            2: self.definir_jugadores_PVC,
            3: self.definir_jugadores_CVC,
        }[seleccion]()

        turnos = self.primer_turno(jugadores)

        partida = Tablero()
        movimientos = range(4)
        for _ in movimientos:
            for jugador in turnos:
                try:
                    partida.insertar_posicion(jugador.get_simbolo(), jugador.insertar_posicion(partida))
                except KeyboardInterrupt:
                    input("\nPerdiste por abandono!\nPresiona enter para salir...")
                    sys.exit()
                ganador = partida.verificar_tablero()
                if ganador is not None:
                    print(self.victoria(ganador))
                    break
            else:
                continue
            break
        else:
            print("\nNo hay mas movimientos posibles! :c")
        return

    # ME PARECIO APROPIADO HACER "PRIVADOS" ESTOS METODOS PERO PARA REALIZAR LOS TEST
    # LOS VOY A DEJAR PUBLICOS

    def definir_jugadores_PVC(self):
        """
        Para jugar partidas Player Vs Computer.
        """
        jugador_uno = Persona("X")
        jugador_dos = Pc("O")
        return (jugador_uno, jugador_dos)
    
    def definir_jugadores_PVP(self):
        """
        Para jugar partidas Player vs Player.
        """
        jugador_uno = Persona("X")
        jugador_dos = Persona("O")
        return (jugador_uno, jugador_dos)
    
    def definir_jugadores_CVC(self):
        """
        Para jugar partidas Computer vs Computer.
        """
        jugador_uno = Pc("X")
        jugador_dos = Pc("O")
        return (jugador_uno, jugador_dos)

    def primer_turno(self, jugadores):
        """
        Lanza la moneda para decidir quien juega el primer turno.
        """
        # RANDRANGE ME PUEDE DAR 1 (TRUE) o 0 (FALSE). EN CASO DE QUE SEA TRUE EL JUGADOR UNO (PERSONA) VA SEGUNDO
        if randrange(2):
            jugadores = jugadores[::-1]
        return jugadores
        
    def victoria(self, player):
        """
        Define quien es el ganador de la partida.
        """
        return ("El jugador {} ha ganado!!").format(player)

    def mostrar_menu(self):
        """
        Muestra el menu para seleccionar el tipo de juego
        """
        _ = system('clear')
        seleccion = input("""        Ingresa el modo de juego que queres jugar...

            > 1.     Jugador vs Jugador     <
            > 2.   Jugador vs Computadora   <
            > 3. Computadora vs Computadora <

        Modo de juego: """)
        while seleccion not in ["1","2","3"]:
            _ = system('clear')
            seleccion = input("""        Ups! modo de juengo invalido...

            > 1.     Jugador vs Jugador     <
            > 2.   Jugador vs Computadora   <
            > 3. Computadora vs Computadora <

        Modo de juego: """)
        return seleccion


if __name__ == '__main__':
    juego = Tic_tac_toe()
    juego.comenzar_partida()

