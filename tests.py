import unittest
from validator import valida_cdvpy

class testes(unittest.TestCase):

    def test_zero(self):
        result = valida_cdvpy('032345')
        self.assertEqual(False, result)

    def test_numero_caracteres(self):
        result = valida_cdvpy('032345565')
        self.assertEqual(False, result)

    def test_somente_digito(self):
        result = valida_cdvpy('A03f45')
        self.assertEqual(False, result)

    def test_duplicado_par(self):
        result = valida_cdvpy('332335')
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()


