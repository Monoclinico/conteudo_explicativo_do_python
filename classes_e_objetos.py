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
  # Bloco da superclasse.
  pass
class ClasseBase2:
  # Bloco da superclasse.
  pass
class SubClasseHerda1(ClasseBase):
  # Bloco da subclasse.
  pass
class SubClasseHerda2(ClasseBase,ClasseBase2):
  # Bloco da subclasse.
  pass

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