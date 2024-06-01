import unittest
from mi_calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

#fijense en este , no comienza su nombre con test
    def not_a_test_sum(self): #este metodo NO es un test OJO CON ESTO 
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_suma(), 10, 'la SUMA esta mal')

    def test_diff(self):
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_resta(), 6, 'la RESTA esta mal')

    def test_product(self):
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_multiplicar(), 16, 'la MULTIPLICACION esta mal')

    def test_quotient(self):
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_dividir(), 4, 'la DIVISION esta mal')

if __name__ == '__main__':
    unittest.main()