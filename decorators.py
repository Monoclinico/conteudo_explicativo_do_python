# ========================== DECORATOR NORMAL ======================================
# O decorator, nada mais é que um método para envolver uma função, modificando seu comportamento.
# Exemplo 1:
def cria_potencia(x):
    def potencia(num):
        return x ** num
    return potencia

# Potência de 2 e 3
potencia_2 = cria_potencia(2)
potencia_3 = cria_potencia(3)

# Resultado
print(potencia_2(2))
print(potencia_3(2))

# Exemplo 2:
def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")
    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
# Resultado
funcao_decorada()

# ======================== DECORATOR COM @ ===========================
# A decoração ocorre na linha antes do cabeçalho da função. 
# O "@" é seguido pelo nome da função do decorador.

def nosso_decorador(func):
  def funcao_interna(a,b):
    print("Incio")
    func(a,b)
    print("Fim")
  return funcao_interna

@nosso_decorador # funcao decoradora
def soma(a,b):
  print(a+b)

# @nosso_decorador == soma = nosso_decorador(soma)
 
soma(6,3)
# Incio
# 9
# Fim


def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter # <- succ = call_counter(succ)
def succ(x):
    return x + 1


print(succ.calls) # 0
for i in range(10):
    succ(i)
print(succ.calls) # 10

# ===================== DECORATOR COMPOSTO =========================
# Exemplo 1:
class separadores:
  @staticmethod
  def linhas(funcao):
    def cima():
      print("-"*10)
      funcao()
    return cima

@separadores.linhas
def linguagem():
  print("Python")

linguagem()

# Exemplo 2:

def fun1():
  def fun2():
    pass
  def fun3(funcao):
    def fun4():
      print("<><><><><><><><><><>")
      funcao()
      print("<><><><><><><><><><>")
    return fun4
  def fun5(funcao):
    def fun6():
      print("++++++++++++++++++++")
      funcao()
      print("++++++++++++++++++++")
    return fun6

  fun2.linha1 = fun3
  fun2.linha2 = fun5
  return fun2

f = fun1()

@f.linha1
def certo():
  print("Deu Certo")

@f.linha2
def errado():
  print("Deu Errado")

certo()
errado()

# <><><><><><><><><><>
# Deu Certo
# <><><><><><><><><><>
# ++++++++++++++++++++
# Deu Errado
# ++++++++++++++++++++


# ======================== DECORATOR COM PARAMETRO ===========================

def agradecer(argumento):
    def agradecer_decorator(func):
        def function_wrapper(x):
            print(argumento)
            func(x)
        return function_wrapper
    return agradecer_decorator

@agradecer("Obrigado!")
def pessoa(x):
    print(x)

pessoa("Claudio")

# ======================== DECORATOR EM CLASSES ===========================

class DecorarNome:
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self,nome):
        self.f(nome)

    @staticmethod
    def coloca_sobrenome(f):
      def sobrenome(nome):
        print("Sobrenome:")
        f(nome)
      return sobrenome


@DecorarNome
def nome(nome):
  print(nome)

nome("Jeremias") # Jeremias

@DecorarNome.coloca_sobrenome
def segundo_nome(nome):
  print(nome)

segundo_nome("Camargo")
# Sobrenome:
# Camargo

# ======================== PROPERTY ================================
# Um método usado para obter um valor é decorado com "@property", ou seja, 
# colocamos essa linha diretamente na frente do cabeçalho. 
# O método que deve funcionar como setter é decorado com "@ x.setter". 
# Se a função tivesse sido chamada "f", teríamos que decorá-la com "@ f.setter".

class Q:

    def __init__(self,x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)

q1 = Q(7)
q1.x = -9
print(q1.x)

# --------------------------- Property -----------------------
class P:

    def __init__(self,anos:int=0):
        self.idade = anos

    @property # mesma coisa do x.getter
    def idade(self):
        return self.__x

    @idade.setter
    def idade(self, anos):
        self.__x = anos
        

    @idade.getter # pode ser substituido pelo property
    def idade(self):
      return self.__x

p1 = P(40)
p1.idade = 23
print(p1.idade) # 23
