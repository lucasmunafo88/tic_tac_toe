from main import Tic_tac_toe
from jugadores.pc import Pc
from jugadores.persona import Persona

class Test_main(object):

    def correr_tests(self):
        """
        Corre todos los tests.
        """
        self.test_definir_jugadores_PVC()
        self.test_definir_jugadores_PVP()
        self.test_definir_jugadores_CVC()
        self.test_primer_turno()

    def test_definir_jugadores_PVC(self):
        tic_tac_toe = Tic_tac_toe()
        recibido = tic_tac_toe.definir_jugadores_PVC()
                
        assert isinstance(recibido[0], Persona) and isinstance(recibido[1], Pc),\
            "tic_tac_toe.definir_jugadores_PVC() no devuelve una tupla de (Persona, Pc)"
        print("SUCCEEDED tic_tac_toe.definir_jugadores_PVC()")

    def test_definir_jugadores_PVP(self):
        tic_tac_toe = Tic_tac_toe()
        recibido = tic_tac_toe.definir_jugadores_PVP()
                
        assert isinstance(recibido[0], Persona) and isinstance(recibido[1], Persona),\
            "tic_tac_toe.definir_jugadores_PVP() no devuelve una tupla de (Persona, Persona)"
        print("SUCCEEDED tic_tac_toe.definir_jugadores_PVP()")

    def test_definir_jugadores_CVC(self):
        tic_tac_toe = Tic_tac_toe()
        recibido = tic_tac_toe.definir_jugadores_CVC()
                
        assert isinstance(recibido[0], Pc) and isinstance(recibido[1], Pc),\
            "tic_tac_toe.definir_jugadores_CVC() no devuelve una tupla de (Pc, Pc)"
        print("SUCCEEDED tic_tac_toe.definir_jugadores_CVC()")

    def test_primer_turno(self):
        tic_tac_toe = Tic_tac_toe()
        persona = Persona('X')
        pc = Pc('O')
        jugadores = (persona, pc)
        recibido = tic_tac_toe.primer_turno(jugadores)
 
        assert recibido == jugadores or recibido == jugadores[::-1],\
            "tic_tac_toe.primer_turno() no devuelve una tupla de jugadores."
        print("SUCCEEDED tic_tac_toe.prier_turno()")
