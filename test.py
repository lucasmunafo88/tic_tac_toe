from tests.test_pc import Test_pc
from tests.test_persona import Test_persona
from tests.test_main import Test_main

if __name__ == "__main__":
    test_pc = Test_pc()
    test_persona = Test_persona()
    test_main = Test_main()

    test_pc.correr_tests()
    test_persona.correr_tests()
    test_main.correr_tests()