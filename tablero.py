from os import system
import numpy as np

from collections import Counter

class Tablero(object):

    # La existencia de estos dos diccionarios haciendo referencia a las mismas celdas se debe
    # a que es mas sencillo de verificar su existencia y bloquearlas en caso de que esten ocupadas.
    POSICIONES_VALIDAS = {"A1":(0,0),"A2":(1,0),"A3":(2,0),"B1":(0,1),"B2":(1,1),"B3":(2,1),"C1":(0,2),"C2":(1,2),"C3":(2,2)}
    POSICIONES_VALIDAS_PC = {(0,0):"A1",(1,0):"A2",(2,0):"A3",(0,1):"B1",(1,1):"B2",(2,1):"B3",(0,2):"C1",(1,2):"C2",(2,2):"C3"}
    posiciones_tablero = np.array((4,4))

    def __init__(self):
        """
        Constructor del tablero. Se genera el tablero con las posiciones vacias ('-'). Al mismo tiempo que se genera se lo dibuja.
        """
        # Trabajo con numpy por una cuestion de que es mas sencillo para realizar ciertas
        # operaciones como la diagonal, la diagonal secundaria, etc...
        self.posiciones_tablero = np.array([
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ])
        self.dibujar_tablero()

    def dibujar_tablero(self):
        """
        A partir de la lista de posiciones redibuja el tablero. A la matriz de datos se le appendea los indicadores
        de columnas y filas.
        """
        _ = system('clear')
        coordenadas_numericas = np.array([
            ["1"],
            ["2"],
            ["3"]
        ])
        coordenadas_alfanumericas = np.array([
            [" ","A","B","C"]
        ])
        tablero_coordenadas = np.append(coordenadas_numericas, self.posiciones_tablero, axis=1)
        tablero_coordenadas = np.append(coordenadas_alfanumericas, tablero_coordenadas, axis=0)
        for fila in tablero_coordenadas:
            for columna in fila:
                print("| " + columna + " |", end="")

            # ME PARECIO INTERESATE UTILIZAR LO QUE ALEJANDRO ME HABIA COMENTADO EN LA ENTREVISTA, SIN EMBARGO 
            # CREO QUE SERIA MEJOR REALIZAR UN PRINT LUEGO DE LA SEGUNDA ITERACION
            # else:
            #     print("")

            print("")
        return

    def insertar_posicion(self, simbolo, coordenadas):
        """
        Inserta en una posicion valida no ocupada, el simbolo correspondiente (pasado como parametro, permitiendo de esta forma jugar un PVP).
        """
        fila = coordenadas[0]
        columna = coordenadas[1]
        # HAGO UN POP A LAS POSICIONES VALIDAS PARA VERIFICAR DE FORMA MAS SENCILLA
        self.POSICIONES_VALIDAS.pop(self.POSICIONES_VALIDAS_PC[coordenadas]) 
        self.posiciones_tablero[fila][columna] = simbolo
        self.dibujar_tablero()
        return

    def verificar_tablero(self):
        """
        Verifica si alguno de los dos jugadores se llevo la victoria.
        """
        # PARA LLEVARSE LA VICTORIA TODA UNA LINEA TIENE QUE SER O BIEN 'X' o 'O'
        # SABIENDO ESTO SE PUEDE HACER UN SET Y COMPROBAR QUE EL UNICO ELEMENTO QUE TENGA SEA UNO DE LOS SIMBOLOS
        # PRIMERO VERIFICO LAS DIAGONALES YA QUE SON MAS FACILES DE VERIFICAR
        diagonal_principal = set(np.diag(self.posiciones_tablero))
        diagonal_secundaria = set(np.diag(np.fliplr(self.posiciones_tablero)))
        if diagonal_principal in [{'X'}, {'O'}]:
            return diagonal_principal.pop()
        elif diagonal_secundaria in [{'X'}, {'O'}]:
            return diagonal_secundaria.pop()
        # LUEGO VERIFICO LAS HORIZONTALES Y VERTICALES
        for i in range(3):
            horizontal = set(self.posiciones_tablero[i][:])
            vertical = set(self.posiciones_tablero[:,i])
            if horizontal in [{'X'}, {'O'}]:
                return horizontal.pop()
            elif vertical in [{'X'}, {'O'}]:
                return vertical.pop()
        return None

    def get_tablero(self):
        """
        Getter del tablero. Facilita el conocimiento para pc y persona de la ubicacion de los simbolos.
        """
        return self.posiciones_tablero