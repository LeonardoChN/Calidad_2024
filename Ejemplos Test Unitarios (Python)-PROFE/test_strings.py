import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('inacap'.upper(), 'INACAP')

    def test_isupper(self):
        self.assertTrue('INACAP'.isupper())
        self.assertFalse('inacap'.isupper())

    def test_split(self):
        s = 'hola mundo'
        self.assertEqual(s.split(), ['hola', 'mundo'])
        # compruebe que s.split falla cuando el separador no es una cadena
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()