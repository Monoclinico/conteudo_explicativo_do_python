
import unittest
from minha_soma import soma
from fractions import Fraction 


class TesteSoma(unittest.TestCase):
  def test_lista_interios(self):
    dados = [2,4,7]
    resultado = soma(dados)
    self.assertEqual(resultado,13)

  def test_lista_fracionarios(self):
    dados = [Fraction(1,5), Fraction(2,5), Fraction(2,5)]
    resultado = soma(dados)
    self.assertEqual(resultado, 1)

  def test_tipo_diferente(self):
    dados = "ERRRO"
    with self.assertRaises(TypeError):
      resultado = soma(dados)
      del resultado

if __name__ == "__main__":
  unittest.main()