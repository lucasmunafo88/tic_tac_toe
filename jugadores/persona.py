class Persona(object):
    
    simbolo = "-"
    COLOR_AMARILLO = '\033[93m'
    COLOR_COLORADO = '\033[91m'
    COLOR_END = '\033[0m'

    def __init__(self, simbolo):
        self.simbolo = simbolo

    def insertar_posicion(self, tablero):
        posicion = input(self.COLOR_AMARILLO + "Ingresa la posicion donde queres jugar..." + self.COLOR_END).upper()
        while posicion not in tablero.posiciones_validas:
            tablero.dibujar_tablero()
            posicion = input(self.COLOR_COLORADO + "Posicion inexistente o ya utilizada, porfavor reingresa la posicion donde queres jugar..." + self.COLOR_END).upper()
        return tablero.posiciones_validas[posicion]

    def get_simbolo(self):
        return self.simbolo