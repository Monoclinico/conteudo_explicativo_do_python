
import unittest
from minha_soma import soma
from fractions import Fraction 


class TesteSoma(unittest.TestCase):
  @staticmethod
  def imprime_informacao():
    print()
    print(" Funcoes de Testes ".center(70,"="))

  def test_lista_interios(self):
    dados = [2,4,7]
    resultado = soma(dados)
    self.assertEqual(resultado,13)

  def test_lista_fracionarios(self):
    dados = [Fraction(1,5), Fraction(2,5), Fraction(2,5)]
    resultado = soma(dados)
    self.assertEqual(resultado, 1)

  def test_tipo_diferente(self):
    dados = ["ERRRO",None,{22,3},True,lambda x: x(3)]
    for d in dados:
      with self.assertRaises(AssertionError):
          soma(d)

if __name__ == "__main__":
  TesteSoma.imprime_informacao()
  unittest.main(verbosity=2)