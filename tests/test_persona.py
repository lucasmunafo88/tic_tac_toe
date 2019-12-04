from jugadores.persona import Persona

class Test_persona(object):

    @classmethod
    def correr_tests(cls):
        cls.test_get_simbolo()

    def test_get_simbolo(self):
        persona = Persona("X")
        expected = "X"
        received = persona.get_simbolo("X")
        assert received == expected, "persona.get_simbolo() no devuelve el simbolo esperado"
        print("SUCCEEDED persona.get_simbolo()")

    def test_insertar_posicion(self):
        # Probablemente para testear el input sera necesario usar una libreria
        # de un framework
        pass

if __name__ == "__main__":
    Test_persona.correr_tests()