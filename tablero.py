from os import system
import numpy as np

class tablero(object):

    POSICIONES_VALIDAS = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
    posiciones_tablero = np.array((4,4))

    def __init__(self):
        """
        Constructor del tablero. Se genera el tablero con las posiciones vacias ('-'). Al mismo tiempo que se genera el tablero se lo dibuja.
        """
        self.posiciones_tablero = np.array([
            [" ","A","B","C"],
            ["1","-","-","-"],
            ["2","-","-","-"],
            ["3","-","-","-"]
        ])
        self.dibujar_tablero()

    def dibujar_tablero(self):
        """
        Funcion que dibuja el tablero. A partir de la lista de posiciones el mismo redibuja el tablero.
        """
        _ = system('clear')
        for fila in self.posiciones_tablero:
            for columna in fila:
                print("| " + columna + " |", end="")

            # ME PARECIO INTERESATE UTILIZAR LO QUE ALEJANDRO ME HABIA COMENTADO EN LA ENTREVISTA, SIN EMBARGO 
            # CREO QUE SERIA MEJOR REALIZAR UN PRINT LUEGO DE LA SEGUNDA ITERACION
            # else:
            #     print("")

            print("")
        return

    def insertar_posicion(self, simbolo):
        """
        Inserta en una posicion valida no ocupada, el simbolo correspondiente (pasado como parametro, permitiendo de esta forma jugar un PVP).
        """
        fila = 0
        columna = 0
        posicion = input("Ingresa la posicion donde queres jugar...").upper()
        fila = int(posicion[1])
        columna = (self.POSICIONES_VALIDAS.index(posicion) // 3) + 1
        while posicion not in self.POSICIONES_VALIDAS or self.posiciones_tablero[fila][columna] != "-":
            self.dibujar_tablero()
            posicion = input("Posicion inexistente o ya utilizada, porfavor reingresa la posicion donde queres jugar...").upper()
            fila = int(posicion[1])
            columna = (self.POSICIONES_VALIDAS.index(posicion) // 3) + 1

        self.posiciones_tablero[fila][columna] = simbolo
        self.dibujar_tablero()
        return

    def verificar_tablero(self):
        """
        Verifica si alguno de los dos jugadores se llevo la victoria.
        """
        # PARA LLEVARSE LA VICTORIA TODA UNA LINEA TIENE QUE SER O BIEN 'X' o 'O'
        # SABIENDO ESTO SE PUEDE HACER UN SET Y COMPROBAR QUE EL UNICO ELEMENTO QUE TENGA SEA UNO DE LOS SIMBOLOS
        # PRIMERO VERIFICO LAS DIAGONALES
        diagonal_principal = set(np.diag(self.posiciones_tablero))
        diagonal_secundaria = set(np.diag(np.fliplr(self.posiciones_tablero)))
        if diagonal_principal in [{'X'}, {'O'}]:
            return diagonal_principal.pop()
        elif diagonal_secundaria in [{'X'}, {'O'}]:
            return diagonal_secundaria.pop()
        # LUEGO VERIFICO LAS HORIZONTALES Y VERTICALES
        for i in range(1,4):
            vertical = set(self.posiciones_tablero[i][1:])
            horizontal = set(self.posiciones_tablero[1:,i])
            if vertical in [{'X'}, {'O'}]:
                return vertical.pop()
            elif horizontal in [{'X', {'O'}]:
                return horizontal.pop()
        return None
