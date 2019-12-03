from random import randrange

from tablero import Tablero
from jugadores.persona import Persona
from jugadores.pc import Pc

class Tic_tac_toe(object):

    jugador_uno = None
    jugador_dos = None

    def comenzar_partida(self):
        """
        Comenzar partida declara los jugadores, quien comienza el turno, y da comienzo a la partida.
        En caso de hallar un ganador se termina la partida. Caso contratio la partida finaliza cuando no hallan
        mas movimientos posibles.
        """
        ganador = None
        partida = Tablero()
        self.definir_jugadores_PVC()
        turnos = self.primer_turno()

        movimientos = range(4)
        for _ in movimientos:
            print(_)
            for jugador in turnos:
                partida.insertar_posicion(jugador.get_simbolo(), jugador.insertar_posicion(partida))
                ganador = partida.verificar_tablero()
                if ganador is not None:
                    self.victoria(ganador)
                    break
            else:
                continue
            break
        print("No hay mas movimientos posibles! :c")
        return

    def definir_jugadores_PVC(self):
        """
        Para jugar partidas Player Vs Computer.
        """
        self.jugador_uno = Persona("X")
        self.jugador_dos = Pc("O")
        return
    
    def definir_jugadores_PVP(self):
        """
        Para jugar partidas Player vs Player.
        """
        self.jugador_uno = Persona("X")
        self.jugador_dos = Persona("O")
        return

    def primer_turno(self):
        """
        Lanza la moneda para decidir quien juega el primer turno.
        """
        # RANDRANGE ME PUEDE DAR 1 (TRUE) o 0 (FALSE). EN CASO DE QUE SEA TRUE EL JUGADOR UNO (PERSONA) VA SEGUNDO
        turnos = [self.jugador_uno, self.jugador_dos]
        if randrange(2):
            turnos = turnos[::-1]
        return turnos
        

    def victoria(self, player):
        """
        Define quien es el ganador de la partida.
        """
        print(("El jugador {} ha ganado!!").format(player))
        return


if __name__ == '__main__':
    juego = Tic_tac_toe()
    juego.comenzar_partida()

