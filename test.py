from tests.test_pc import Test_pc
from tests.test_persona import Test_persona

if __name__ == "__main__":
    test_pc = Test_pc()
    test_persona = Test_persona()
    test_pc.correr_tests()
    test_persona.correr_tests()