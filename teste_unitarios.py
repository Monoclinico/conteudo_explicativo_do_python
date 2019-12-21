
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
import unittest

# TESTE SIMPLES
def potencia1(x):
  return x * x

def potencia2(x):
  return x ** 2

class TestPotencias(unittest.TestCase):
    def teste(self):
        self.assertEqual(potencia1(5), potencia2(5))

# TESTE COM CLASSES
class MinhaSoma:
    def soma(self, n):
        return n + 1

class TesteSoma(unittest.TestCase):
    def teste(self):
        obj = MinhaSoma()
        self.assertEqual(obj.soma(3), 4)

if __name__ == '__main__':
    unittest.main()