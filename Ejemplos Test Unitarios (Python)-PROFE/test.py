'''

Method	                    Checks that
assertEqual(a, b)	        a == b
assertNotEqual(a, b)	    a != b
assertTrue(x)	            bool(x) is True
assertFalse(x)	            bool(x) is False
assertIs(a, b)	            a is b
assertIsNot(a, b)	        a is not b
assertIsNone(x)	            x is None
assertIsNotNone(x)	        x is not None
assertIn(a, b)	            a in b
assertNotIn(a, b)	        a not in b
assertIsInstance(a, b)	    isinstance(a, b)
assertNotIsInstance(a, b)	not isinstance(a, b)

'''

import unittest
from mi_calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        calculadora = Calculadora(8, 2) # 8+2 = 10
        self.assertEqual(calculadora.get_suma(), 10, 'la SUMA esta mal')

    def test_resta(self):
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_resta(), 7, 'la RESTA esta mal')

    def test_multiplicar(self):
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_multiplicar(), 16, 'la MULTIPLICACION esta mal')

    def test_dividir(self):
        calculadora = Calculadora(8, 2)
        self.assertEqual(calculadora.get_dividir(), 4, 'la DIVISION esta mal')

if __name__ == '__main__':
    unittest.main()