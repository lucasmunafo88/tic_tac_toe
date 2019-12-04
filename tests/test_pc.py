from time import sleep

from jugadores.pc import Pc
from tablero import Tablero
import numpy as np

class Test_pc (object):
    
    def correr_tests(self):
        self.test_insertar_posicion_aleatoria()
        self.test_insertar_posicion_condicionada()

    def _insertar_pc(self, partida, pc):
        partida.insertar_posicion(pc.get_simbolo(), pc.insertar_posicion(partida))
        return

    def test_insertar_posicion_aleatoria(self):
        """
        Testea cuando la pc inserta sin amenazas (x x -) o posibles victorias (o o -).
        """
        # Para este test voy a necesitar instanciar un tablero nuevo, es decir sin
        # ningun simbolo.
        pc = Pc("O")
        tablero_vacio = Tablero()
        self._insertar_pc(tablero_vacio, pc)
        tablero_recibido = tablero_vacio.get_tablero()

        posiciones_tablero = np.array([
            ["O","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ])
        tablero_jugado = Tablero()
        tablero_jugado.set_tablero(posiciones_tablero)
        tablero_esperado = tablero_jugado.get_tablero()

        assert (tablero_recibido == tablero_esperado).all(), "pc.insertar_posicion() no inserta la posicion esperada"
        print("SUCCEEDED pc.insertar_posicion()")
        sleep(2)


    def test_insertar_posicion_condicionada(self):
        """
        Testtea todas las posibilidades de jugadas.
        """
        # Basandome en el principio de la funcion de verificar tablero dentro de tablero
        # se me ocurrio realizar un test con todas las posibles combinaciones que puede llegar a jugar
        # la pc.
        # Para el test voy a utilizar unicamente un simbolo ('X') ya que para la pc es eactamente
        # lo mismo, es decir lo unico que le importa es que hay dos simbolos iguales en una fila
        # con un espacio ocupable.

        def generador_infinito(funcion):
            """
            Utilizado como decorador para poder reutilizar un generador.
            """
            # Como voy a necesitar reutilizar mi generador hago esta clase
            # para pisar __iter__. Con esto tambien evito clonarlo 8 con tee()
            class _generador_infinito(object):
                def __init__(self, *args, **kwargs):
                    self.__args = args
                    self.__kwargs = kwargs
                def __iter__(self):
                    return funcion(*self.__args, **self.__kwargs)
            return _generador_infinito

        @generador_infinito
        def generador_posibilidades():
            tablero_esperado = Tablero()
            movimientos_posibles = np.array([
                ["X","X","-"],
                ["X","-","X"],
                ["-","X","X"]
            ])

            movimientos_esperados = np.array([
                ["X","X","O"],
                ["X","O","X"],
                ["O","X","X"]
            ])
            for indice in range(3):
                yield (movimientos_posibles[indice], movimientos_esperados[indice],\
                     tablero_esperado)

        pc = Pc("O")

        for posicion_posibe, posicion_esperada, tablero_jugado in generador_posibilidades():
            tablero_nuevo = Tablero()
            tablero_recibido = tablero_nuevo.get_tablero()
            tablero_esperado = tablero_jugado.get_tablero()
            np.fill_diagonal(tablero_recibido, posicion_posibe)
            np.fill_diagonal(tablero_esperado, posicion_esperada)
            self._insertar_pc(tablero_nuevo,pc)
            assert (tablero_recibido == tablero_esperado).all(), "pc.insertar_posicion() (diagonal principal condicionada) no inserta la posicion esperada"
            print("SUCCEEDED pc.insertar_posicion() (diagonal principal condicionada)")
            sleep(2)            

        # diagonal_principal = np.diag(self.posiciones_tablero)
        # diagonal_secundaria = set(np.diag(np.fliplr(self.posiciones_tablero)))
        # if diagonal_principal in [{'X'}, {'O'}]:
        #     return diagonal_principal.pop()
        # elif diagonal_secundaria in [{'X'}, {'O'}]:
        #     return diagonal_secundaria.pop()
        # # LUEGO VERIFICO LAS HORIZONTALES Y VERTICALES
        # for i in range(3):
        #     horizontal = set(self.posiciones_tablero[i][:])
        #     vertical = set(self.posiciones_tablero[:,i])
        #     if horizontal in [{'X'}, {'O'}]:
        #         return horizontal.pop()
        #     elif vertical in [{'X'}, {'O'}]:
        #         return vertical.pop()
        # return None

if __name__ == "__main__":
    
    Test_pc.correr_tests()