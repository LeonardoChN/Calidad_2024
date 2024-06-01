import unittest
from mi_calculadora import Calculadora

class TestCalculadora(unittest.TestCase):


    @classmethod #Este a diferencia del test 3 solo se llama 1 vez y carga el setup para abajo con el dato asignado
    def setUpClass(self):
        self.calculadora = Calculadora(8, 2)

    def test_suma(self):
        self.assertEqual(self.calculadora.get_suma(), 10, 'la SUMA esta mal')

    def test_resta(self):
        self.assertEqual(self.calculadora.get_resta(), 6, 'la RESTA esta mal')

    def test_multiplicar(self):
        self.assertEqual(self.calculadora.get_multiplicar(), 16, 'la MULTIPLICACION esta mal')

    def test_dividir(self):
        self.assertEqual(self.calculadora.get_dividir(), 4, 'la DIVISION esta mal')


if __name__ == '__main__':
    unittest.main()
