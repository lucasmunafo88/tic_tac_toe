from collections import Counter
import numpy as np

class Pc(object):
    
    simbolo = "-"

    def __init__(self, simbolo):
        """
        Constructor de Pc. Recibe como parametro el simbolo que utilizara a lo largo de la partida.
        """
        self.simbolo = simbolo

    def _verificar_posiciones(self, counter):
        """
        Verifica si en cierta linea pasada como parametro existe una combinacion ganadora o peligrosa.
        """
        # En caso de que en una linea se encuentren dos simbolos iguales y un espacio libre significa
        # que o es una amenaza o una posible victoria, por lo que estamos obligados a ocupar esa casilla.
        if "O" in counter:
            if counter["O"] == 2 and '-' in counter:
                return True
        elif "X" in counter:
            if counter["X"] == 2 and '-' in counter:
                return True
        return False

    def insertar_posicion(self, tablero):
        """
        Verifica si en aguna fila o columna queda un solo espacio libre. Si lo hay y los simbolos son
        de la pc ganara sino bloqueara al otro jugador.
        En caso de que no haya un unico espacio libre en fila o columna jugara la primer posicion libre.
        """
        # Para ganar la partida existe un numero finito de combinaciones, dadas por filas, columnas y diagonales.
        # Sabiendo esto descompongo el tablero e inspecciono cada una de ellas en busca de posibles amenazas o posibles victorias.
        # Cuando no existe ninguna de las anteriores esperamos encontrarlas realizando un movimiento aleatorio.
        tablero = tablero.get_tablero()
        counter_diagonal_principal = Counter(np.diag(tablero))
        counter_diagonal_secundaria = Counter(np.diag(np.fliplr(tablero)))
        
        diagonal_principal = np.diag(tablero)
        diagonal_secundaria = np.diag(np.fliplr(tablero))

        if self._verificar_posiciones(counter_diagonal_principal):
            indice = ((np.where(diagonal_principal == '-'))[0][0])
            return (indice, indice)
        if self._verificar_posiciones(counter_diagonal_secundaria):
            indice = (np.where(diagonal_secundaria == '-'))[0][0]
            return (indice, [2,1,0][indice])

        # Verificamos las horizontales y verticales al mismo tiempo
        for i in range(3):
            counter_horizontal = Counter(tablero[i][:])
            counter_vertical = Counter(tablero[:,i])            
            horizontal = tablero[i][:]
            vertical = tablero[:,i]
            if self._verificar_posiciones(counter_horizontal):
                indice = ((np.where(horizontal == '-'))[0][0])
                return (i, indice)
            if self._verificar_posiciones(counter_vertical):
                indice = ((np.where(vertical == '-'))[0][0])
                return (indice, i)

        index = list(zip(*np.where(tablero == '-')))[0]
        return index

    def get_simbolo(self):
        """
        Getter del simbolo de esta pc.
        """
        return self.simbolo