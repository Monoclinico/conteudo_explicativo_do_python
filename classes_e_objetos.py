# Programacao Orientada a Objetos
# O conceito da programacao orientada a objetos esta focado na criacao de codigo que possa ser reusado.
# Esse conceito e tambem conhecido como DRY (Nao repete o mesmo)

# ========================== CLASSE ======================
# Objeto e simplesmente uma colecao de dados (variaveis) e metodos (funcoes) que atuam sobre esses dados. 
# E classe e um modelo para o objeto.
class MinhaNovaClasse:
  """Minha classe de exemplo."""
  atributo_x = 45.50 # atributo
  def metodo_y(self): # metodo
    pass
print(MinhaNovaClasse.atributo_x) # 45.50
print(MinhaNovaClasse.metodo_y) # <function MinhaNovaClasse.metodo_y at 0x0000000001EB78C8>

# ====================== OBJETO ====================================
# Um objeto tambem e chamado de instancia de uma classe e o 
# processo de criacao desse objeto e chamado de instanciacao.
objeto = MinhaNovaClasse()
objeto.numero_qualquer = 77
print(objeto) # <__main__.MinhaNovaClasse object at 0x00000000020C4438>
print(objeto.numero_qualquer) # 77

# ====================== SELF ================================
# -> self.alguma_coisa
# -> def alguma_coisa(self):
# Sempre que um objeto chama seu metodo, o proprio objeto e passado como o primeiro argumento. 
# Entao, objeto.func() se traduz em classe.func(objeto).
# O primeiro argumento da funcao na classe deve ser o proprio objeto. 
# Isso e convencionalmente chamado de self. Pode ter outro nome, mas e altamente recomendavel seguir a convencao.
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

#================================= CONSTRUTOR NA HERANcA ===================================    
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
# Lembre-se de que todos os metodos devem ter self como seu primeiro parametro.
# Esses metodos sao acessados usando a mesma sintaxe de pontos que os atributos.
# As classes tambem podem ter atributos de classe, criados pela atribuicao de variaveis no corpo da classe. 
# Eles podem ser acessados a partir de instancias da classe ou da propria classe.
class Dog43:
  LEGS = 4 # <- Atributo de classe 
  def __init__(self, name, color):
    self.name = name
    self.color = color

print(Dog43.LEGS) # 4
print(Dog43("Jack","white").LEGS) # 4

# ===================================== SUPER =======================================
# A funcao super e uma funcao relacionada a heranca util que se refere a classe pai. 
# Pode ser usado para encontrar o metodo com um determinado nome na superclasse de um objeto.
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

# ================================ SUPER COM PARAMETROS ===========================
# No Python 3, a chamada super (Square, self) e equivalente a chamada super () sem parametros. 
# O primeiro parametro refere-se a subclasse. 
# enquanto o segundo parametro refere-se a um objeto  que, nesse caso, e proprio. 
class Janela:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class JanelaQuadrada(Janela):
    def __init__(self, length):
        super(JanelaQuadrada, self).__init__(length, length)


# =========================== SUPER COM HERANCA MULTIPLA ==========================
class Primeiro():
    def __init__(self):
        super().__init__() # chama Segundo que esta abaixo na hirarquia 
        print("Primeiro")

class Segundo():
    def __init__(self):
        super().__init__() # chama Terceiro que esta abaixo na hirarquia
        print("Segundo")

class Terceiro():
    def __init__(self):
        super().__init__() # chama object que esta abaixo na hirarquia
        print("Terceiro")

class Quarto(Primeiro,Segundo,Terceiro):
    def __init__(self):
        super().__init__() # chama Primeiro que esta abaixo na hirarquia
        print("Quarto")

print(Quarto.mro())
# <class '__main__.Quarto'>, 
# <class '__main__.Primeiro'>,
# <class '__main__.Segundo'>, 
# <class '__main__.Terceiro'>, 
# <class 'object'>

q = Quarto()
# Terceiro
# Segundo
# Primeiro
# Quarto

# ================================= OVERRIDE ========================================
# Se uma classe herda de outra com os mesmos atributos ou metodos, ela as substitui.

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
# Metodos magicos sao metodos especiais que tem sublinhados duplos no inicio e no final de seus nomes.
# Eles tambem sao conhecidos como dunders.
# Ate agora, o unico que encontramos e __init__, mas existem varios outros.
# Eles sao usados para criar funcionalidades que nao podem ser representadas como um metodo normal.

# OTHER -> representa o segundo objeto passado como parametro.

# ---------- Metodos Contrutores e de Inicializacao ---------------
# O metodo __new__ e chamado com a classe como seu primeiro argumento; 
# sua responsabilidade e retornar uma nova instancia dessa classe. 
# Primeiro, o metodo __new__ da classe e chamado, passando a propria classe como primeiro argumento, 
# seguido por qualquer argumento (posicional e de palavra-chave) recebido pela chamada original. 
# Isso retorna uma nova instancia. 
# Em seguida, o metodo __init__ dessa instancia e chamado para inicializa-lo ainda mais. 
# (Tudo isso e controlado pelo metodo __call__ da metaclasse, a proposito.)
# __new__ e um metodo estatico. 
# Ao defini-lo, voce nao precisa (mas pode!) Usar a frase "__new__ = staticmethod (__ new__)", 
# porque isso esta implicito no nome (e especificado pelo construtor da classe).
# Exemplo: 
class Polegada(float):
  "Converte de polegada para metro."
  def __new__(cls, arg=0.0):
    return float.__new__(cls, arg*0.0254)

print(Polegada(1)) # 0.0254

# __init__(self,[...])
  # O inicializador para a classe. 
  # Ele e passado independentemente do nome do construtor primario.
  # Por exemplo, se chamamos x = SomeClass (10, 'foo'), __init__ passaria 10 e 'foo' como argumentos.
  # __Init__ e quase universalmente usado na classe Python definicoes.

# __del__(self)
# Se __new__ e __init__ formaram o construtor do objeto, __del__ e o destruidor. 
# Ele nao implementa o comportamento da instrucao del x (para que o codigo nao seja convertido para x .__ del __ ()).
# Em vez disso, define o comportamento para quando um objeto e coletado de lixo. 
# Pode ser bastante util para objetos que podem exigir limpeza extra apos a exclusao, como soquetes ou objetos de arquivo. 
# Entretanto, tenha cuidado, pois nao ha garantia de que __del__ sera executado se o objeto ainda estiver vivo quando o interprete sair; 
# portanto, __del__ nao podera servir de substituto para boas praticas de codificacao (como sempre fechando uma conexao quando voce terminar) 
# De fato, __del__ quase nunca deve ser usado por causa das circunstancias precarias sob as quais e chamado; 
# Use-o com cautela!

# ---------- Metodos Matematicos ----------------------
# __add__ (self, other)
#     Implementa adicao.
# __sub__ (self, other)
#     Implementa subtracao.
# __mul__ (self, other)
#     Implementa multiplicacao.
# __floordiv__ (self, other)
#     Implementa a divisao inteira usando o operador //.
# __div__ (self, other)
#     Implementa a divisao usando o operador /.
# __truediv__ (self, other)
  # Implementa a verdadeira divisao. 
  # Observe que isso so funciona quando a divisao de importacao __future__ esta em vigor.
# __mod__ (self, other)
#     Implementa o modulo usando o operador%.
# __divmod__ (self, other)
#     Implementa o comportamento para divisao longa usando a funcao incorporada divmod ().
# __pow__
#     Implementa o comportamento de expoentes usando o operador **.
# __lshift __ (self, other)
#     Implementa o deslocamento bit a bit esquerdo usando o operador <<.
# __rshift __ (self, other)
#     Implementa o deslocamento bit a bit a direita usando o operador >>.
# __and__ (self, other)
#     Implementa bit a bit e usando o operador &.
# __or__ (self, other)
#     Implementa bit a bit ou usando o | operador.
# __xor__ (self, other)
#     Implementa bit a bit xor usando o operador ^.

# Trocar os operandos:
# some_object + other
# Essa foi a adicao "normal". O equivalente refletido e a mesma coisa, exceto com os operandos trocados:
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
# __cmp__ e o mais basico dos metodos magicos de comparacao. 
#   Na verdade, ele implementa o comportamento para todos os operadores de comparacao (<, ==,! =, Etc.)
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
# Operadores e funcoes unarios tem apenas um operando, por exemplo negacao, valor absoluto, etc.
# __pos__(self)
#      Implementa o comportamento para positivo unario (por exemplo, + some_object)
# __neg__(self)
#      Implementa o comportamento de negacao (por exemplo, -some_object)
# __abs__(self)
#      implementa o comportamento da funcao abs () incorporada.
# __invert__(self)
#      Implementa o comportamento para inversao usando o operador ~. 
# __round__(self, n)
#      Implementa o comportamento da funcao round () incorporada. n e o numero de casas decimais para arredondar.
# __floor__(self)
#      Implementa o comportamento de math.floor (), ou seja, arredondar para o numero inteiro mais proximo.
# __ceil__(self)
#      Implementa o comportamento de math.ceil (), ou seja, arredondando para o numero inteiro mais proximo.
# __trunc__(self)
#      Implementa o comportamento de math.trunc (), ou seja, truncando para uma integral.

# ------------ Metodos de operacoes de atribuicao -------------------
# __iadd__ (self, other)
#     Implementa adicao com atribuicao.
# __isub__ (self, other)
#     Implementa subtracao com atribuicao.
# __imul__ (self, other)
#     Implementa multiplicacao com atribuicao.
# __ifloordiv__ (self, other)
#     Implementa divisao inteira com atribuicao usando o operador // =.
# __idiv__ (self, other)
#     Implementa a divisao com atribuicao usando o operador / =.
# __itruediv__ (self, other)
#     Implementa verdadeira divisao com atribuicao. 
#     Observe que isso so funciona quando a divisao de importacao __future__ esta em vigor.
# __imod__ (self, other)
#     Implementa o modulo com atribuicao usando o operador% =.
# __ipow__
#     Implementa o comportamento de expoentes com atribuicao usando o operador ** =.
# __ilshift__ (self, other)
#     Implementa deslocamento a esquerda bit a bit com atribuicao usando o operador << =.
# __irshift__ (self, other)
#     Implementa o deslocamento bit a direita com atribuicao usando o operador >> =.
# __iand__ (self, other)
#     Implementa bit a bit e com atribuicao usando o operador & =.
# __ior__ (self, other)
#     Implementa bit a bit ou com atribuicao usando o operador | =.
# __ixor__ (self, other)
#     Implementa bit a bit xor com atribuicao usando o operador ^ =.

# ------------- Metodos de conversao de tipo -------------------
# __int__ (self)
#      Implementa a conversao de tipo em int.
# __long__ (self)
#      Implementa a conversao de tipo para longa.
# __float__ (self)
#      Implementa a conversao de tipo para flutuar.
# __complex __ (self)
#      Implementa a conversao de tipos em complexo.
# __oct__ (self)
#      Implementa a conversao de tipo em octal.
# __hex__ (self)
#      Implementa a conversao de tipo em hexadecimal.
# __index__ (self)
#      Implementa a conversao de tipo em int quando o objeto e usado em uma expressao de fatia. 
#      Se voce definir um tipo numerico personalizado que pode ser usado no fatiamento, defina __index__.
# __trunc__ (self)
#      Chamado quando math.trunc (self) e chamado. __trunc__ deve retornar o valor de `self truncado para 
#      um tipo integral (geralmente um longo).
# __coerce__ (self, other)
#      Metodo para implementar aritmetica de modo misto. __coerce__ deve retornar None se a conversao de tipo for impossivel. 
#      Caso contrario, ele deve retornar um par (2-tupla) de si e de other, manipulado para ter o mesmo tipo.

# -------------------- Metodos para representar as classes ------------------------------
# __str__(self)
#     Define o comportamento para quando str () e chamado em uma instancia da sua classe.
# __repr__(self)
#     Define o comportamento para quando repr () e chamado em uma instancia da sua classe. 
#     A principal diferenca entre str () e repr () e o publico-alvo. 
#     repr () tem como objetivo produzir uma saida que e mais legivel por maquina 
#     (em muitos casos, pode ate ser um codigo Python valido), enquanto str () se destina a ser legivel por humanos.
# __unicode__(self)
#     Define o comportamento para quando unicode () e chamado em uma instancia da sua classe. 
#     unicode () e como str (), mas retorna uma string unicode. 
#     Cuidado: se um cliente chamar str () em uma instancia da sua classe e voce tiver definido apenas __unicode __ (), ele nao funcionara. 
#     Voce deve sempre tentar definir __str __ () tambem para o caso de alguem nao se dar ao luxo de usar unicode.
# __format__ (self, formato_str)
#     Define o comportamento para quando uma instancia da sua classe e usada na formatacao de seqüencia de caracteres com novo estilo. 
#     Por exemplo, "Ola, {0: abc}!". Format (a) levaria a chamada um formato .__ __ ("abc"). 
#     Isso pode ser util para definir seus self tipos numericos ou de sequencia que voce deseja fornecer opcoes especiais de formatacao.
# __hash__(self)
#     Define o comportamento para quando o hash () e chamado em uma instancia da sua classe. 
#     Ele precisa retornar um numero inteiro e seu resultado e usado para comparacao rapida de teclas em dicionarios. 
#     Observe que isso geralmente implica em implementar __eq__ tambem. Ative a seguinte regra: a == b implica hash (a) == hash (b).
# __nonzero__(self)
#     Define o comportamento para quando bool () e chamado em uma instancia da sua classe. 
#     Deve retornar True ou False, dependendo se voce deseja considerar a instancia como True ou False.
# __dir__(self)
#     Define o comportamento para quando dir () e chamado em uma instancia da sua classe. 
#     Este metodo deve retornar uma lista de atributos para o usuario. 
#     Normalmente, implementar __dir__ e desnecessario, mas pode ser de vital importancia para o uso interativo de suas classes, 
#     se voce redefinir __getattr__ ou __getattribute__ (que voce vera na proxima secao) ou gerar atributos dinamicamente.
# __sizeof__(self)
#     Define o comportamento para quando sys.getsizeof () e chamado em uma instancia da sua classe. 
#     Isso deve retornar o tamanho do seu objeto, em bytes. 
#     Isso geralmente e mais util para classes Python implementadas em extensoes C, mas ajuda a estar ciente disso.

# -------------- Metodos de Controle de acesso a atributos ----------------------
# __getattr__(self, nome)
#     Voce pode definir o comportamento para quando um usuario tentar acessar um atributo que nao existe 
#     (de maneira alguma ou ainda). Isso pode ser util para capturar e redirecionar erros de ortografia comuns, 
#     emitir avisos sobre o uso de atributos obsoletos (voce ainda pode optar por calcular e retornar esse atributo, 
#     se desejar) ou entregar habilmente um AttributeError. 
#     Porem, ele so e chamado quando um atributo inexistente e acessado, portanto, nao e uma solucao de encapsulamento verdadeira.
# __setattr__(self, nome, valor)
#     Ao contrario de __getattr__, __setattr__ e uma solucao de encapsulamento. 
#     Ele permite definir o comportamento para atribuicao a um atributo, 
#     independentemente de esse atributo existir ou nao, 
#     o que significa que voce pode definir regras personalizadas para quaisquer alteracoes nos valores dos atributos. No entanto, voce deve ter cuidado com o uso de __setattr__, como o exemplo no final da lista mostrara.
# __delattr__(self, nome)
#     e exatamente o mesmo que __setattr__, mas para excluir atributos em vez de defini-los. 
#     As mesmas precaucoes precisam ser tomadas como no __setattr__, 
#     a fim de impedir a recursao infinita 
#     (chamar del self.name na implementacao de __delattr__ causaria recursao infinita).
# __getattribute__(self, nome)
#     Depois de tudo isso, __getattribute__ se encaixa muito bem com seus companheiros __setattr__ e __delattr__. 
#     No entanto, eu nao recomendo que voce o use. __getattribute__ so pode ser usado com classes de novo estilo, 
#     todas as classes sao de novo estilo nas versoes mais recentes do Python, 
#     e nas versoes mais antigas voce pode criar uma classe de novo estilo subclassificando o objeto. 
#     Ele permite definir regras sempre que um atributo for e acessado. 
#     Ele sofre de alguns problemas de recursao infinita semelhantes aos de seus parceiros no crime 
#     (desta vez, voce chama o metodo __getattribute__ da classe base para evitar isso). 
#     Tambem evita principalmente a necessidade de __getattr__, que, quando __getattribute__ e implementado, 
#     so e chamado se for chamado explicitamente ou se um AttributeError for gerado.Este metodo pode ser usado 
#     (afinal, e sua escolha), mas eu nao o recomendo porque tem um pequeno caso de uso 
#     (e muito mais raro precisarmos comportamento especial para recuperar um valor do que atribuir a ele) 
#     e porque pode ser realmente dificil de implementar sem erros.

# ----------------------- Metodos de Containers (Colecoes) ---------------------
# __len__(self)
#     Retorna o comprimento do conteiner. Parte do protocolo para recipientes imutaveis ​​e mutaveis.
# __getitem__ (self, chave)
#     Define o comportamento para quando um item e acessado, usando a notacao:
#     -> self[key] 
#     Isso tambem faz parte dos protocolos de conteineres mutaveis ​​e imutaveis. 
#     Ele tambem deve gerar excecoes apropriadas: 
#     TypeError se o tipo da chave estiver errado e KeyError se nao houver um valor correspondente para a chave.
# __setitem__ (self, chave, valor)
#     Define o comportamento para quando um item e atribuido, usando a notacao self [nkey] = value. 
#     Isso faz parte do protocolo de conteiner mutavel. 
#     Novamente, voce deve aumentar KeyError e TypeError quando apropriado.
# __delitem__ (slef, chave)
#     Define o comportamento para quando um item e excluido (por exemplo, del self [chave]). 
#     Isso e apenas parte do protocolo de conteiner mutavel. 
#     Voce deve gerar as excecoes apropriadas quando uma chave invalida for usada.
# __iter__ (self)
#     Deve retornar um iterador para o conteiner. 
#     Os iteradores sao retornados em varios contextos, principalmente pela funcao integrada iter () 
#     e quando um conteiner e repetido usando o formulario para x no conteiner :. 
#     Os iteradores sao seus self objetos e tambem devem definir um metodo __iter__ que retorne self.
# __reversed__ (self)
#     Chamado para implementar o comportamento da funcao incorporada reversed ().
#     Deve retornar uma versao invertida da sequencia. 
#     Implemente isso apenas se a classe de sequencia estiver ordenada, como lista ou tupla.
# __contains__(self, item)
#     __contains__ define o comportamento dos testes de associacao usando in e nao in. 
#     Por que isso nao faz parte de um protocolo de sequencia, voce pergunta? 
#     Como quando __contains__ nao esta definido, 
#     o Python apenas repete a sequencia e retorna True se encontrar o item que esta procurando.
# __missing__(self, chave)
#     __missing__ e usado nas subclasses de dict. 
#     Ele define o comportamento para sempre que uma chave e acessada que nao existe em um dicionario 
#     (por exemplo, se eu tivesse um dicionario d e dissesse d ["george"] 
#     quando "george" nao e uma chave no ditado, d. __missing__ ("george") seria chamado).

# Exemplo:
class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    def __init__(self, values:list=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)
    def head(self):
        # get the first element
        return self.values[0]
    def tail(self):
        # get all elements after the first
        return self.values[1:]
    def init(self):
        # get elements up to the last
        return self.values[:-1]
    def last(self):
        # get last element
        return self.values[-1]
    def drop(self, n):
        """get all elements except first n"""
        return self.values[n:]
    def take(self, n):
        # get first n elements
        return self.values[:n]

lista_personalizada = FunctionalList([0,1,2,3,4,5,6,7,8,9])
print(lista_personalizada.drop(5)) # [5, 6, 7, 8, 9]
for n in lista_personalizada:
  print(n)

# ---------------------- Metodos de checagem ------------------------------
# Voce tambem pode controlar como a reflexao usando as funcoes internas isinstance () e issubclass () 
# se comporta definindo metodos magicos. Os metodos magicos sao:

# __instancecheck__ (self, instancia)
#      Verifica se uma instancia e uma instancia da classe que voce definiu (por exemplo, isinstance (instancia, classe).
# __subclasscheck__ (self, subclasse)
#      Verifica se uma classe subclasse a classe que voce definiu (por exemplo, issubclass (subclasse, classe)).  
  
  
# ---------------------- Metodos de contexto -------------------------------
# Os gerenciadores de contexto permitem que acoes de configuracao e limpeza sejam executadas para objetos 
# quando sua criacao e agrupada com uma instrucao with. 
# O comportamento do gerenciador de contexto e determinado por dois metodos magicos:
  
# __enter__(self)
#      Define o que o gerenciador de contexto deve fazer no inicio do bloco criado pela instrucao with. 
#      Observe que o valor de retorno de __enter__ esta vinculado ao destino da instrucao with ou ao nome apos o as.
# __exit__(self, tipo de excecao, valor de excecao, retorno)
#      Define o que o gerenciador de contexto deve fazer depois que seu bloco for executado (ou finalizado). 
#      Pode ser usado para lidar com excecoes, executar limpeza ou fazer algo sempre feito imediatamente apos a acao no bloco. 
#      Se o bloco for executado com sucesso, exception_type, exception_value e traceback serao None. 
#      Caso contrario, voce pode optar por manipular a excecao ou deixar que o usuario a manipule; 
#      se voce quiser lidar com isso, certifique-se de que __exit__ retorne True depois que tudo estiver dito e feito. 
#      Se voce nao deseja que a excecao seja tratada pelo gerenciador de contexto, deixe acontecer.
  
# ---------------------- Metodos descritores -----------------------------------------
# 
# __get__ (self, instancia, proprietario)
#      Defina o comportamento para quando o valor do descritor e recuperado. 
#       instance e a instancia do objeto do proprietario. owner e a propria classe do proprietario.
# __set__ (self, instancia, valor)
#      Defina o comportamento para quando o valor do descritor e alterado. 
#      instance e a instancia da classe do proprietario e value e o valor para definir o descritor.
# __delete__ (self, instancia)
#      Defina o comportamento para quando o valor do descritor e excluido. 
#      instance e a instancia do objeto do proprietario. 
  

class Metros():
    cem = 100
    def __get__(self, instance, owner):
        return instance.cm / self.cem
  
class Distance():
    cm = 10
    m = Metros()
  
print(Distance().m) # 0.1
b1 = Distance()
print(b1.m) # 0.1

# ------------------------ Metodos de Copia ----------------------------------
# __copy__ (self)
#      Define o comportamento de copy.copy () para instancias da sua classe. 
#      copy.copy () retorna uma copia superficial do seu objeto.
#      isso significa que, enquanto a instancia em si e uma nova instancia, todos os seus dados sao referenciados.
#      ou seja, o proprio objeto e copiado, mas seus dados ainda sao referenciados 
#      ( e, portanto, alteracoes nos dados em uma copia superficial podem causar alteracoes no original).
# __deepcopy__ (self, memodict = {})
#      Define o comportamento de copy.deepcopy () para instancias da sua classe. 
#      copy.deepcopy () retorna uma copia profunda do seu objeto - o objeto e seus dados sao copiados. 
#      memodict e um cache de objetos copiados anteriormente.
#      isso otimiza a copia e evita a recursao infinita ao copiar estruturas de dados recursivas. 
#      Quando desejar copiar em profundidade um atributo individual, 
#      chame copy.deepcopy () nesse atributo com memodict como o primeiro argumento.

# -------------------- Metodos de pickling -------------------------------
# Vamos mergulhar em decapagem. Digamos que voce tenha um dicionario que deseja armazenar e recuperar mais tarde. 
# Voce pode escrever seu conteudo em um arquivo, certificando-se cuidadosamente de escrever a sintaxe correta 
# e recupera-lo usando exec () ou processando a entrada do arquivo. 
# Mas isso e precario, na melhor das hipoteses: se voce armazenar dados importantes em texto sem formatacao, 
# eles poderao ser corrompidos ou alterados de varias maneiras para causar uma falha no programa 
# ou pior execucao de codigos maliciosos no seu computador.
# Exemplo:
# import pickle
# data = {'foo': [1, 2, 3],
#         'bar': ('Hello', 'world!'),
#         'baz': True}
# jar = open('data.pkl', 'wb')
# pickle.dump(data, jar) # write the pickled data to the file jar
# jar.close()

# __getinitargs__(self)
#     Se desejar que __init__ seja chamado quando sua classe nao for escolhida, defina __getinitargs__, 
#     que retornara uma tupla dos argumentos que voce gostaria de passar para __init__. 
#     Observe que esse metodo funcionara apenas para classes de estilo antigo.
# __getnewargs__(self)
#     Para classes de novo estilo, voce pode influenciar quais argumentos sao passados ​​para __new__ ao cancelar a selecao. 
#     Esse metodo tambem deve retornar uma tupla de argumentos que serao passados ​​para __new__.
# __getstate__(self)
#     Em vez de o atributo __dict__ do objeto ser armazenado, voce pode retornar um estado personalizado a ser 
#     armazenado quando o objeto e selecionado. Esse estado sera usado por __setstate__ quando o objeto nao for escolhido.
# __setstate__ (self, estado)
#     Quando o objeto e retirado, se __setstate__ for definido, o estado do objeto sera passado a ele em vez de diretamente aplicado ao __dict__ do objeto. Isso anda de maos dadas com __getstate__: quando ambos sao definidos, voce pode representar o estado de pickled do objeto da maneira que desejar com o que quiser.
# __reduce__(self)
#     Ao definir tipos de extensao (ou seja, tipos implementados usando a API C do Python), voce deve informar ao Python como seleciona-los, se desejar que eles os selecionem. __reduce __ () e chamado quando um objeto que o define e decapado. Ele pode retornar uma string que representa um nome global que o Python procurara e pickle, ou uma tupla. A tupla contem entre 2 e 5 elementos: um objeto que pode ser chamado para recriar o objeto, uma tupla de argumentos para esse objeto que pode ser chamado, estado a ser passado para __setstate__ (opcional), um iterador que gera itens da lista a serem selecionados (opcional) e um iterador que produz itens de dicionario a serem selecionados (opcional).
# __reduce_ex __(self)
#     __reduce_ex__ existe para compatibilidade. Se definido, __reduce_ex__ sera chamado sobre __reduce__ na decapagem. __reduce__ tambem pode ser definido para versoes mais antigas da API de decapagem que nao suportavam __reduce_ex__.


# --------------- Metodo de chamada de funcao ---------------------
# __call __ (self, [args ...])
#     Permite que uma instancia de uma classe seja chamada como uma funcao. 
#     Essencialmente, isso significa que x () e o mesmo que x .__ chama __ (). 
#     Observe que __call__ recebe um numero variavel de argumentos; 
#     isso significa que voce define __call__ como faria com qualquer outra funcao, 
#     assumindo quantos argumentos desejar.
# Exemplo:
class Quadrado:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura
    self.set_area()
  def set_area(self):
    self.area = self.altura * self.largura
  def get_area(self):
    return self.area
  def __call__(self, altura, largura):
    self.altura = altura
    self.largura = largura
    self.set_area()

q1= Quadrado(5,4)
print(q1.get_area()) # 20
q1(9,5)
print(q1.get_area()) # 45

# Exemplos de invocacao dos metodos:
# __new__(cls [,...]) 	            instance = MyClass(arg1, arg2) 	
# __init__(self [,...]) 	          instance = MyClass(arg1, arg2) 	
# __cmp__(self, other) 	            self == other, self > other, etc.
# __pos__(self) 	                  +self 
# __neg__(self) 	                  -self 	
# __invert__(self) 	                ~self 	
# __index__(self) 	                x[self] 	
# __nonzero__(self) 	              bool(self) 	
# __getattr__(self, name)           self.name 
# __setattr__(self, name, val) 	    self.name = val 	
# __delattr__(self, name) 	        del self.name 	
# __getattribute__(self, name) 	    self.name 	
# __getitem__(self, key) 	          self[key] 
# __setitem__(self, key, val) 	    self[key] = val 	
# __delitem__(self, key) 	          del self[key] 	
# __iter__(self) 	                  for x in self 	
# __contains__(self, value) 	      value in self, value not in self 	
# __call__(self [,...]) 	          self(args) 	
# __enter__(self) 	                with self as x: 
# __exit__(self, exc, val, trace)   with self as x: 
# __getstate__(self) 	              pickle.dump(pkl_file, self)	
# __setstate__(self) 	              data = pickle.load(pkl_file)


# DETALHES IMPORTANTES:
#  Como a distincao entre string e unicode foi eliminada no Python 3, __unicode__ desapareceu e 
#  __bytes__ (que se comporta de maneira semelhante a __str__ e __unicode__ na 2.7) 
#  existe para um novo built-in para a construcao de matrizes de bytes.
#  Como o padrao de divisao e a divisao verdadeira no Python 3, __div__ desapareceu no Python 3
#  __coerce__ se foi devido a redundancia com outros metodos magicos e comportamento confuso
#  __cmp__ desapareceu devido a redundancia com outros metodos magicos
#  __nonzero__ foi renomeado para __bool__


# =============================== METODO DE CLASSE ================================
# @classmethod
# Metodos de objetos que examinamos ate agora sao chamados por uma instancia de uma classe, 
# que e entao passada para o auto-parametro do metodo.
# Os metodos de classe sao diferentes - eles sao chamados por uma classe, 
# que e passada para o parametro cls do metodo.
# Um uso comum desses metodos sao os metodos de fabrica, que instanciam uma instancia de uma classe, 
# usando parametros diferentes daqueles geralmente passados para o construtor de classes.
# Os metodos de classe sao marcados com um decorador de metodo de classe.
# CLS -> e a classe construtora
class Massa:
  def __init__(self, g):
    self.gramas = g

  def get_massa(self):
    print(f"Massa: {self.gramas}g")

  @classmethod # --> Com decorator
  def quilos(cls, kg):
    return cls(kg*1000)

  def toneladas(cls,t):
    return  cls(t*(1000**2))
  toneladas = classmethod(toneladas) # Sem decorator

pimenta = Massa(50)
cimento = Massa.quilos(50)
carro = Massa.toneladas(2.5)

pimenta.get_massa() # 50.0g
cimento.get_massa() # 50000.0g
carro.get_massa() # 2500000.0g

# ==================== METODO ESTATICO ====================
# Metodos estaticos sao semelhantes aos metodos de classe, exceto que eles nao recebem argumentos adicionais; 
# eles sao identicos as funcoes normais que pertencem a uma classe.
# Eles sao marcados com o decorador staticmethod ou criados com a classe staticmethod.

class Pizza:
  def __init__(self, sabor):
    self.sabor = sabor

  @staticmethod # --> Com decorator
  def bordas():
    print("Pizza de bordas recheadas.")

  def pedacos():
    print("Pizza de 8 pedacos.")
  pedacos = staticmethod(pedacos) # Sem decorator

pizza_queijo = Pizza("queijo")
pizza_queijo.bordas()
pizza_queijo.pedacos()
Pizza.bordas()
Pizza.pedacos()

# ================================ CLASSE COM DOIS CONSTRUTORES =================
class Quente:
  def __init__(self):
    self.estado = "quente"
class Frio:
  def __init__(self):
    self.estado = "frio"
class Agua(Quente,Frio):
  def __init__(self,estado:bool=True):
    if estado:
      Quente.__init__(self)
    else:
      Frio.__init__(self)
    

agua_com_gas = Agua(False)
agua_com_cafe = Agua(True)
print(agua_com_gas.estado) # frio
print(agua_com_cafe.estado) # quente