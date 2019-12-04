from tests.test_pc import Test_pc

if __name__ == "__main__":
    # print(str(os.path.abspath("tic_tac_toe/juggadores/pc.py")))
    # # sys.path.insert(1, 'C:/Users/user/Desktop/tic_tac_toe/jugadores')
    # sys.path.insert(1, str(os.path.abspath("tic_tac_toe/juggadores")))
    # print(sys.path)

    test_pc = Test_pc()

    test_pc.correr_tests()