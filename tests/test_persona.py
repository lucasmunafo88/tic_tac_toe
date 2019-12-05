from jugadores.persona import Persona


class Test_persona(object):
    def correr_tests(self):
        self.test_get_simbolo()
        print("========================================================")
        print("Todas las pruebas PERSONA fueron realizadas con exito")
        print("========================================================")


    def test_get_simbolo(self):
        persona = Persona("X")
        simbolo_esperado = "X"
        simbolo_recibido = persona.get_simbolo()
        assert (
            simbolo_recibido == simbolo_esperado
        ), "persona.get_simbolo() no devuelve el simbolo esperado"
        print("SUCCEEDED persona.get_simbolo()")

    def test_insertar_posicion(self):
        # Probablemente para testear el input sera necesario usar una libreria
        # de un framework
        pass
