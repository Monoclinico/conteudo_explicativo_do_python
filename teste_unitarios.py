
# Os tres modulos de testes mais populares são:

# unittest
# nose ou nose2
# pytest


# TESTE sem o modulo de teste
import sys
def test(arg1,arg2):
    """  Imprime o resultado do teste.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if arg1 == arg2:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
test(2,4)

# ====================== UNITTEST =========================
# O nome do metodo deve comecar com test: def test....():

from unittest import TestCase, main

# TESTE SIMPLES
def potencia1(x):
  return x * x

def potencia2(x):
  return x ** 2

class TestPotencias(TestCase):
    def test_igualdade(self):
        self.assertEqual(potencia1(5), potencia2(5))
    def test_maior(self):
        self.assertGreater(potencia1(5),potencia2(2))

# TESTE COM CLASSES
class MinhaSoma:
    def soma(self, n):
        return n + 1

class TesteSoma(TestCase):
    def test_soma(self):
        obj = MinhaSoma()
        self.assertEqual(obj.soma(3), 4)

if __name__ == '__main__':
    main()



    