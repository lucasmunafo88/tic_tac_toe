from time import sleep

from jugadores.pc import Pc
from tablero import Tablero
import numpy as np

class Test_pc (object):
    
    def correr_tests(self):
        """
        Corre todos los tests.
        """
        self.test_insertar_posicion_aleatoria()
        self.test_insertar_posicion_condicionada()
        self.test_get_simbolo()
        print("============================================")
        print("Todas las pruebas PC fueron realizadas con exito")
        return

    def __pc_insertar_movimiento(self, partida, pc):
        """
        Inserta el movimiento de la pc en la instancia de tablero (o partida) pasado como parametro. 
        """
        # Como hago muchas inserciones de pc en el tablero decidi abstraerlo en una funcion aparte "privada"
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
        self.__pc_insertar_movimiento(tablero_vacio, pc)
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
            """
            Genera todas las posibilidades que se pueden dar en una partida
            """
            # Como el movimiento condicionado se da a partir de dos simbolos iguales en la misma linea
            # unicamente lo hice con un simbolo.
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

        def verificar_assert(nombre_test, codigo_insertar_recibido, codigo_insertar_esperado, es_declaracion):
            """
            A partir de las posibilidades dadas por el generador crea dos instancias de tablero (o partida), donde
            en una almacena el tablero que se espera recibir y en la otra el tablero donde la pc ya realizo su movimiento.
            Ambas varibles 'codigo...' llevan el codigo que se tiene que ejecutar para insertar en ambos tableros (recibido/esperado)
            los movimientos a testearse. 
            """
            for posicion_posible, posicion_esperada, tablero_jugado in generador_posibilidades():
                tablero_nuevo = Tablero()
                tablero_recibido = tablero_nuevo.get_tablero()
                tablero_esperado = tablero_jugado.get_tablero()
                if es_declaracion:
                    exec(codigo_insertar_recibido)
                    exec(codigo_insertar_esperado)
                else:
                    eval(codigo_insertar_recibido)
                    eval(codigo_insertar_esperado)
                self.__pc_insertar_movimiento(tablero_nuevo,pc)
                assert (tablero_recibido == tablero_esperado).all(), "pc.insertar_posicion() ({} condicionada) no inserta la posicion esperada".format(nombre_test)
                print("SUCCEEDED pc.insertar_posicion() ({} condicionada)".format(nombre_test))

        pc = Pc("O")

        # !!! SIEMPRE EN codigo_insertar_recibido SE PASA COMO PARAMETRO tablero_recibido, posicion_posible 
        # !!! SIEMPRE EN codigo_insertar_ESPERADO SE PASA COMO PARAMETRO tablero_esperado, posicion_esperada 
        verificar_assert("Diagonal principal", "np.fill_diagonal(tablero_recibido, posicion_posible)", "np.fill_diagonal(tablero_esperado, posicion_esperada)", False)
        verificar_assert("Diagonal secundaria", "np.fill_diagonal(np.fliplr(tablero_recibido), posicion_posible)", "np.fill_diagonal(np.fliplr(tablero_esperado), posicion_esperada)", False)

        for i in range(3):
            verificar_assert("Horizontal {}".format(i+1), "tablero_recibido[{}] = posicion_posible".format(i), "tablero_esperado[{}] = posicion_esperada".format(i), True)
            verificar_assert("Vertical {}".format(i+1), "tablero_recibido[:,{}] = posicion_posible".format(i), "tablero_esperado[:,{}] = posicion_esperada".format(i), True)

    def test_get_simbolo(self):
        pc = Pc("X")
        simbolo_esperado = "X"
        simbolo_recibido = pc.get_simbolo()
        assert simbolo_recibido == simbolo_esperado, "pc.get_simbolo() no devuelve el simbolo esperado"
        print("SUCCEEDED pc.get_simbolo()")