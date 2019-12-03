# Programacao Orientada a Objetos
# O conceito da programacao orientada a objetos esta focado na criacao de codigo que possa ser reusado.
# Esse conceito e tambem conhecido como DRY (Nao repete o mesmo)

# ========================== CLASSE ======================
# Objeto é simplesmente uma coleção de dados (variáveis) e métodos (funções) que atuam sobre esses dados. 
# E classe é um modelo para o objeto.
class MinhaNovaClasse:
  """Minha classe de exemplo."""
  atributo_x = 45.50 # atributo
  def metodo_y(self): # metodo
    pass
print(MinhaNovaClasse.atributo_x) # 45.50
print(MinhaNovaClasse.metodo_y) # <function MinhaNovaClasse.metodo_y at 0x0000000001EB78C8>

# ====================== OBJETO ====================================
# Um objeto também é chamado de instância de uma classe e o 
# processo de criação desse objeto é chamado de instanciação.
objeto = MinhaNovaClasse()
objeto.numero_qualquer = 77
print(objeto) # <__main__.MinhaNovaClasse object at 0x00000000020C4438>
print(objeto.numero_qualquer) # 77

# ====================== SELF ================================
# -> self.alguma_coisa
# -> def alguma_coisa(self):
# Sempre que um objeto chama seu método, o próprio objeto é passado como o primeiro argumento. 
# Então, objeto.func() se traduz em classe.func(objeto).
# O primeiro argumento da função na classe deve ser o próprio objeto. 
# Isso é convencionalmente chamado de self. Pode ter outro nome, mas é altamente recomendável seguir a convenção.
class A:
  def numero(self, num): # usou-se o self que representa o objeto.
    self.posicao = num # o atributo posicao de self(objeto pasado) recebe num.

a = A() # criacao do objeto
#1 opcao para chamar metodos:
A.numero(a,1)
print(a.posicao) # 1

#2 opcao para chamar metodos:
a.numero(3) # o self fica omitido 
print(a.posicao) # 3

# usa-se metodos e atributos da superclasse sem "super()": 
class A2(A):
  def numero(self, num):
    A.numero(self,num*2) # 

a2 = A2()
a2.numero(3)
print(a2.posicao) # 6

# ======================= HERANCA ==============================
class ClasseBase:
  def metodo1(self):
    print("ClasseBase")
class ClasseBase2:
  def metodo2(self):
    print("ClasseBase2")
class SubClasseHerda1(ClasseBase):
  def metodo3(self):
    print("SubClasse1")
class SubClasseHerda2(SubClasseHerda1,ClasseBase2):
  def metodo4(self):
    print("SubClasse2")

sub_teste = SubClasseHerda2()
sub_teste.metodo1() # ClasseBase
sub_teste.metodo2() # ClasseBase2
sub_teste.metodo3() # SubClasse1
sub_teste.metodo4() # SubClasse2

# ================== Chamando metodos de classes ancestrais sem o super ===========================
class Pessoa:
  nome: str = ...
  altura: float = ...
  def __init__(self, nome):
    self.nome = nome
  def set_altura(self, altura):
    self.altura = altura

class Genero():
  sexo: str = ...
  def __init__(self, sexo):
    self.sexo = sexo

class Homem(Pessoa,Genero):
  def __init__(self, nome, altura):
    Pessoa.__init__(self,nome)
    Genero.__init__(self,"masculino")
    Pessoa.set_altura(self,altura)
  def __repr__(self):
    return "{} e {} e tem {}.".format(self.nome,self.sexo,self.altura)

marcos = Homem("Marcos",1.88)
print(marcos.nome)
print(marcos.sexo)
print(marcos.altura)
print(marcos) # Marcos e masculino e tem 1.88.

#================================= CONSTRUTOR NA HERANÇA ===================================    
# metodo contrutor: __init__ 
class Polygon:
  def __init__(self, no_of_sides): 
      self.n = no_of_sides
      self.sides = [0 for i in range(no_of_sides)]
  def inputSides(self):
      self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
  def dispSides(self):
      for i in range(self.n):
          print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

triangule1 = Triangle()
triangule1.inputSides() #3, 4, 5
triangule1.dispSides()
triangule1.findArea() # 6
print(isinstance(triangule1, Triangle)) # True
print(isinstance(triangule1, Polygon)) # True

# ===================================== ATRIBUTOS DE CLASSE E METODOS =========================
# Lembre-se de que todos os métodos devem ter self como seu primeiro parâmetro.
# Esses métodos são acessados usando a mesma sintaxe de pontos que os atributos.
# As classes também podem ter atributos de classe, criados pela atribuição de variáveis no corpo da classe. 
# Eles podem ser acessados a partir de instâncias da classe ou da própria classe.
class Dog43:
  LEGS = 4 # <- Atributo de classe 
  def __init__(self, name, color):
    self.name = name
    self.color = color

print(Dog43.LEGS) # 4
print(Dog43("Jack","white").LEGS) # 4

# ===================================== SUPER =======================================
# A função super é uma função relacionada à herança útil que se refere à classe pai. 
# Pode ser usado para encontrar o método com um determinado nome na superclasse de um objeto.
class H:
  def spam(self):
    print("H")

class I:
  def spam(self):
    print("I")

# com uma heranca:
class J(I): 
  def spam(self):
    print("J")
    super().spam()
            
J().spam() # J, I

# duas ou mais herancas:
# o super so pega a referencia da primeira heranca, se houver nomes iguais.
# para pegar as outras referencias, usa-se diretamente a classe ancestral. 
class K(I,H):
  def spam(self):
    print("K")
    super().spam() 
    H.spam(self) # usa-se diretamente a classe ancestral com o self.

K().spam()

# ================================= OVERRIDE ========================================
# Se uma classe herda de outra com os mesmos atributos ou métodos, ela as substitui.
class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog5(Wolf):
  def bark(self):
    print("Woof")
        
husky = Dog5("Max", "grey")
husky.bark() # Woof

# ============================= METODOS MAGICOS ===========================
# Métodos mágicos são métodos especiais que têm sublinhados duplos no início e no final de seus nomes.
# Eles também são conhecidos como dunders.
# Até agora, o único que encontramos é __init__, mas existem vários outros.
# Eles são usados para criar funcionalidades que não podem ser representadas como um método normal.

# OTHER -> representa o segundo objeto passado como parametro.

# ---------- Metodos Contrutores e de Inicializacao ---------------
# O método __new__ é chamado com a classe como seu primeiro argumento; 
# sua responsabilidade é retornar uma nova instância dessa classe. 
# Primeiro, o método __new__ da classe é chamado, passando a própria classe como primeiro argumento, 
# seguido por qualquer argumento (posicional e de palavra-chave) recebido pela chamada original. 
# Isso retorna uma nova instância. 
# Em seguida, o método __init__ dessa instância é chamado para inicializá-lo ainda mais. 
# (Tudo isso é controlado pelo método __call__ da metaclasse, a propósito.)
# __new__ é um método estático. 
# Ao defini-lo, você não precisa (mas pode!) Usar a frase "__new__ = staticmethod (__ new__)", 
# porque isso está implícito no nome (é especificado pelo construtor da classe).
# Exemplo: 
class Polegada(float):
  "Converte de polegada para metro."
  def __new__(cls, arg=0.0):
    return float.__new__(cls, arg*0.0254)

print(Polegada(1)) # 0.0254

# __init__(self,[...])
  # O inicializador para a classe. 
  # Ele é passado independentemente do nome do construtor primário.
  # Por exemplo, se chamamos x = SomeClass (10, 'foo'), __init__ passaria 10 e 'foo' como argumentos.
  # __Init__ é quase universalmente usado na classe Python definições.

# __del__(self)
# Se __new__ e __init__ formaram o construtor do objeto, __del__ é o destruidor. 
# Ele não implementa o comportamento da instrução del x (para que o código não seja convertido para x .__ del __ ()).
# Em vez disso, define o comportamento para quando um objeto é coletado de lixo. 
# Pode ser bastante útil para objetos que podem exigir limpeza extra após a exclusão, como soquetes ou objetos de arquivo. 
# Entretanto, tenha cuidado, pois não há garantia de que __del__ será executado se o objeto ainda estiver vivo quando o intérprete sair; 
# portanto, __del__ não poderá servir de substituto para boas práticas de codificação (como sempre fechando uma conexão quando você terminar) 
# De fato, __del__ quase nunca deve ser usado por causa das circunstâncias precárias sob as quais é chamado; 
# Use-o com cautela!

# ---------- Metodos Matematicos ----------------------
# __add__ (self, other)
#     Implementa adição.
# __sub__ (self, other)
#     Implementa subtração.
# __mul__ (self, other)
#     Implementa multiplicação.
# __floordiv__ (self, other)
#     Implementa a divisão inteira usando o operador //.
# __div__ (self, other)
#     Implementa a divisão usando o operador /.
# __truediv__ (self, other)
  # Implementa a verdadeira divisão. 
  # Observe que isso só funciona quando a divisão de importação __future__ está em vigor.
# __mod__ (self, other)
#     Implementa o módulo usando o operador%.
# __divmod__ (self, other)
#     Implementa o comportamento para divisão longa usando a função incorporada divmod ().
# __pow__
#     Implementa o comportamento de expoentes usando o operador **.
# __lshift __ (self, other)
#     Implementa o deslocamento bit a bit esquerdo usando o operador <<.
# __rshift __ (self, other)
#     Implementa o deslocamento bit a bit à direita usando o operador >>.
# __and__ (self, other)
#     Implementa bit a bit e usando o operador &.
# __or__ (self, other)
#     Implementa bit a bit ou usando o | operador.
# __xor__ (self, other)
#     Implementa bit a bit xor usando o operador ^.

# Trocar os operandos:
# some_object + other
# Essa foi a adição "normal". O equivalente refletido é a mesma coisa, exceto com os operandos trocados:
# other + some_object
# Deve-se acrescentar "r" antes do nome:
# Exemplo:
# __radd__(self, other)
class SomaTeste():
  def __init__(self,num):
    self.num = float(num)
  def __add__(self,other):
    print(self.num + other)
  def __radd__(self,other):
    print(self.num * other)

n1 = SomaTeste(2)
n1 + 4 # 6
4 + n1 # 8

# ----------- Metodos comparativos -----------------------
# __cmp__ é o mais básico dos métodos mágicos de comparação. 
#   Na verdade, ele implementa o comportamento para todos os operadores de comparação (<, ==,! =, Etc.)
# __eq__(self, other)
#     Define o comportamento para o operador de igualdade, ==.
# __ne__(self, other)
#     Define o comportamento para o operador de diferenca, !=.
# __lt__(self, other)
#     Define o comportamento para o operador de menor, <.
# __gt__(self, other)
#     Define o comportamento para o operador de maior, >.
# __le__(self, other)
#     Define o comportamento para o operador de menor igual, <=.
# __ge__(self, other)
#     Define o comportamento para o operador de maior igual, >=.

# -------------- Metodos Unarios -----------------------
# Operadores e funções unários têm apenas um operando, por exemplo negação, valor absoluto, etc.
# __pos__(self)
#      Implementa o comportamento para positivo unário (por exemplo, + some_object)
# __neg__(self)
#      Implementa o comportamento de negação (por exemplo, -some_object)
# __abs__(self)
#      implementa o comportamento da função abs () incorporada.
# __invert__(self)
#      Implementa o comportamento para inversão usando o operador ~. 
# __round__(self, n)
#      Implementa o comportamento da função round () incorporada. n é o número de casas decimais para arredondar.
# __floor__(self)
#      Implementa o comportamento de math.floor (), ou seja, arredondar para o número inteiro mais próximo.
# __ceil__(self)
#      Implementa o comportamento de math.ceil (), ou seja, arredondando para o número inteiro mais próximo.
# __trunc__(self)
#      Implementa o comportamento de math.trunc (), ou seja, truncando para uma integral.

# ------------ Metodos de operacoes de atribubuicao -------------------

# __iadd__ (self, other)
#     Implementa adição com atribuição.
# __isub__ (self, other)
#     Implementa subtração com atribuição.
# __imul__ (self, other)
#     Implementa multiplicação com atribuição.
# __ifloordiv__ (self, other)
#     Implementa divisão inteira com atribuição usando o operador // =.
# __idiv__ (self, other)
#     Implementa a divisão com atribuição usando o operador / =.
# __itruediv__ (self, other)
#     Implementa verdadeira divisão com atribuição. 
#     Observe que isso só funciona quando a divisão de importação __future__ está em vigor.
# __imod__ (self, other)
#     Implementa o módulo com atribuição usando o operador% =.
# __ipow__
#     Implementa o comportamento de expoentes com atribuição usando o operador ** =.
# __ilshift__ (self, other)
#     Implementa deslocamento à esquerda bit a bit com atribuição usando o operador << =.
# __irshift__ (self, other)
#     Implementa o deslocamento bit a direita com atribuição usando o operador >> =.
# __iand__ (self, other)
#     Implementa bit a bit e com atribuição usando o operador & =.
# __ior__ (self, other)
#     Implementa bit a bit ou com atribuição usando o operador | =.
# __ixor__ (self, other)
#     Implementa bit a bit xor com atribuição usando o operador ^ =.

# ------------- Metodos de conversao de tipo -------------------
# __int__ (self)
#      Implementa a conversão de tipo em int.
# __long__ (self)
#      Implementa a conversão de tipo para longa.
# __float__ (self)
#      Implementa a conversão de tipo para flutuar.
# __complex __ (self)
#      Implementa a conversão de tipos em complexo.
# __oct__ (self)
#      Implementa a conversão de tipo em octal.
# __hex__ (self)
#      Implementa a conversão de tipo em hexadecimal.
# __index__ (self)
#      Implementa a conversão de tipo em int quando o objeto é usado em uma expressão de fatia. 
#      Se você definir um tipo numérico personalizado que pode ser usado no fatiamento, defina __index__.
# __trunc__ (self)
#      Chamado quando math.trunc (self) é chamado. __trunc__ deve retornar o valor de `self truncado para 
#      um tipo integral (geralmente um longo).
# __coerce__ (self, other)
#      Método para implementar aritmética de modo misto. __coerce__ deve retornar None se a conversão de tipo for impossível. 
#      Caso contrário, ele deve retornar um par (2-tupla) de si e de other, manipulado para ter o mesmo tipo.