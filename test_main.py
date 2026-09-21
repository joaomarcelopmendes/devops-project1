import unittest
from main import soma, subtrai, multiplica, divide, saudacao

class TestMain(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
    def test_subtrai(self):
        self.assertEqual(subtrai(5, 2), 3)
    def test_multiplica(self):
        self.assertEqual(multiplica(3, 4), 12)
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
    def test_saudacao(self):
        self.assertEqual(saudacao("Testes"), "Olá, Testes!")

if __name__ == '__main__':
    unittest.main()