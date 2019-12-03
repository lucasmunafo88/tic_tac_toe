class Persona(object):
    
    simbolo = "-"

    def __init__(self, simbolo):
        self.simbolo = simbolo

    def insertar_posicion(self, tablero):
        posicion = input("Ingresa la posicion donde queres jugar...").upper()
        while posicion not in tablero.POSICIONES_VALIDAS:
            tablero.dibujar_tablero()
            posicion = input("Posicion inexistente o ya utilizada, porfavor reingresa la posicion donde queres jugar...").upper()
        return tablero.POSICIONES_VALIDAS[posicion]

    def get_simbolo(self):
        return self.simbolo