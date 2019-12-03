from tablero import tablero

class tic_tac_toe(object):
    def comenzar_partida(self):
        partida = tablero()

        partida.insertar_posicion('X')
        partida.verificar_tablero()
        partida.insertar_posicion('X')
        partida.verificar_tablero()
        partida.insertar_posicion('X')
        partida.verificar_tablero()

        # movimientos = range(9)
        # for turno in movimientos:
                        

    def victoria(self, player):
        print("El jugador {} ha ganado!!").format(player)


if __name__ == '__main__':
    juego = tic_tac_toe()
    juego.comenzar_partida()

