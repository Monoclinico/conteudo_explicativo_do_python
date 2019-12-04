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

# ================================ SUPER COM PARAMETROS ===========================
# No Python 3, a chamada super (Square, self) é equivalente à chamada super () sem parâmetros. 
# O primeiro parâmetro refere-se à subclasse. 
# enquanto o segundo parâmetro refere-se a um objeto  que, nesse caso, é próprio. 
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

# ------------ Metodos de operacoes de atribuicao -------------------
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

# -------------------- Metodos para representar as classes ------------------------------
# __str__(self)
#     Define o comportamento para quando str () é chamado em uma instância da sua classe.
# __repr__(self)
#     Define o comportamento para quando repr () é chamado em uma instância da sua classe. 
#     A principal diferença entre str () e repr () é o público-alvo. 
#     repr () tem como objetivo produzir uma saída que é mais legível por máquina 
#     (em muitos casos, pode até ser um código Python válido), enquanto str () se destina a ser legível por humanos.
# __unicode__(self)
#     Define o comportamento para quando unicode () é chamado em uma instância da sua classe. 
#     unicode () é como str (), mas retorna uma string unicode. 
#     Cuidado: se um cliente chamar str () em uma instância da sua classe e você tiver definido apenas __unicode __ (), ele não funcionará. 
#     Você deve sempre tentar definir __str __ () também para o caso de alguém não se dar ao luxo de usar unicode.
# __format__ (self, formato_str)
#     Define o comportamento para quando uma instância da sua classe é usada na formatação de seqüência de caracteres com novo estilo. 
#     Por exemplo, "Olá, {0: abc}!". Format (a) levaria à chamada um formato .__ __ ("abc"). 
#     Isso pode ser útil para definir seus self tipos numéricos ou de sequência que você deseja fornecer opções especiais de formatação.
# __hash__(self)
#     Define o comportamento para quando o hash () é chamado em uma instância da sua classe. 
#     Ele precisa retornar um número inteiro e seu resultado é usado para comparação rápida de teclas em dicionários. 
#     Observe que isso geralmente implica em implementar __eq__ também. Ative a seguinte regra: a == b implica hash (a) == hash (b).
# __nonzero__(self)
#     Define o comportamento para quando bool () é chamado em uma instância da sua classe. 
#     Deve retornar True ou False, dependendo se você deseja considerar a instância como True ou False.
# __dir__(self)
#     Define o comportamento para quando dir () é chamado em uma instância da sua classe. 
#     Este método deve retornar uma lista de atributos para o usuário. 
#     Normalmente, implementar __dir__ é desnecessário, mas pode ser de vital importância para o uso interativo de suas classes, 
#     se você redefinir __getattr__ ou __getattribute__ (que você verá na próxima seção) ou gerar atributos dinamicamente.
# __sizeof__(self)
#     Define o comportamento para quando sys.getsizeof () é chamado em uma instância da sua classe. 
#     Isso deve retornar o tamanho do seu objeto, em bytes. 
#     Isso geralmente é mais útil para classes Python implementadas em extensões C, mas ajuda a estar ciente disso.

# -------------- Metodos de Controle de acesso a atributos ----------------------
# __getattr__(self, nome)
#     Você pode definir o comportamento para quando um usuário tentar acessar um atributo que não existe 
#     (de maneira alguma ou ainda). Isso pode ser útil para capturar e redirecionar erros de ortografia comuns, 
#     emitir avisos sobre o uso de atributos obsoletos (você ainda pode optar por calcular e retornar esse atributo, 
#     se desejar) ou entregar habilmente um AttributeError. 
#     Porém, ele só é chamado quando um atributo inexistente é acessado, portanto, não é uma solução de encapsulamento verdadeira.
# __setattr__(self, nome, valor)
#     Ao contrário de __getattr__, __setattr__ é uma solução de encapsulamento. 
#     Ele permite definir o comportamento para atribuição a um atributo, 
#     independentemente de esse atributo existir ou não, 
#     o que significa que você pode definir regras personalizadas para quaisquer alterações nos valores dos atributos. No entanto, você deve ter cuidado com o uso de __setattr__, como o exemplo no final da lista mostrará.
# __delattr__(self, nome)
#     É exatamente o mesmo que __setattr__, mas para excluir atributos em vez de defini-los. 
#     As mesmas precauções precisam ser tomadas como no __setattr__, 
#     a fim de impedir a recursão infinita 
#     (chamar del self.name na implementação de __delattr__ causaria recursão infinita).
# __getattribute__(self, nome)
#     Depois de tudo isso, __getattribute__ se encaixa muito bem com seus companheiros __setattr__ e __delattr__. 
#     No entanto, eu não recomendo que você o use. __getattribute__ só pode ser usado com classes de novo estilo, 
#     todas as classes são de novo estilo nas versões mais recentes do Python, 
#     e nas versões mais antigas você pode criar uma classe de novo estilo subclassificando o objeto. 
#     Ele permite definir regras sempre que um atributo for é acessado. 
#     Ele sofre de alguns problemas de recursão infinita semelhantes aos de seus parceiros no crime 
#     (desta vez, você chama o método __getattribute__ da classe base para evitar isso). 
#     Também evita principalmente a necessidade de __getattr__, que, quando __getattribute__ é implementado, 
#     só é chamado se for chamado explicitamente ou se um AttributeError for gerado.Este método pode ser usado 
#     (afinal, é sua escolha), mas eu não o recomendo porque tem um pequeno caso de uso 
#     (é muito mais raro precisarmos comportamento especial para recuperar um valor do que atribuir a ele) 
#     e porque pode ser realmente difícil de implementar sem erros.

# ----------------------- Metodos de Containers (Colecoes) ---------------------
# __len__(self)
#     Retorna o comprimento do contêiner. Parte do protocolo para recipientes imutáveis ​​e mutáveis.
# __getitem__ (self, chave)
#     Define o comportamento para quando um item é acessado, usando a notação:
#     -> self[key] 
#     Isso também faz parte dos protocolos de contêineres mutáveis ​​e imutáveis. 
#     Ele também deve gerar exceções apropriadas: 
#     TypeError se o tipo da chave estiver errado e KeyError se não houver um valor correspondente para a chave.
# __setitem__ (self, chave, valor)
#     Define o comportamento para quando um item é atribuído, usando a notação self [nkey] = value. 
#     Isso faz parte do protocolo de contêiner mutável. 
#     Novamente, você deve aumentar KeyError e TypeError quando apropriado.
# __delitem__ (slef, chave)
#     Define o comportamento para quando um item é excluído (por exemplo, del self [chave]). 
#     Isso é apenas parte do protocolo de contêiner mutável. 
#     Você deve gerar as exceções apropriadas quando uma chave inválida for usada.
# __iter__ (self)
#     Deve retornar um iterador para o contêiner. 
#     Os iteradores são retornados em vários contextos, principalmente pela função integrada iter () 
#     e quando um contêiner é repetido usando o formulário para x no contêiner :. 
#     Os iteradores são seus self objetos e também devem definir um método __iter__ que retorne self.
# __reversed__ (self)
#     Chamado para implementar o comportamento da função incorporada reversed ().
#     Deve retornar uma versão invertida da sequência. 
#     Implemente isso apenas se a classe de sequência estiver ordenada, como lista ou tupla.
# __contains__(self, item)
#     __contains__ define o comportamento dos testes de associação usando in e não in. 
#     Por que isso não faz parte de um protocolo de sequência, você pergunta? 
#     Como quando __contains__ não está definido, 
#     o Python apenas repete a sequência e retorna True se encontrar o item que está procurando.
# __missing__(self, chave)
#     __missing__ é usado nas subclasses de dict. 
#     Ele define o comportamento para sempre que uma chave é acessada que não existe em um dicionário 
#     (por exemplo, se eu tivesse um dicionário d e dissesse d ["george"] 
#     quando "george" não é uma chave no ditado, d. __missing__ ("george") seria chamado).

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
# Você também pode controlar como a reflexão usando as funções internas isinstance () e issubclass () 
# se comporta definindo métodos mágicos. Os métodos mágicos são:

# __instancecheck__ (self, instância)
#      Verifica se uma instância é uma instância da classe que você definiu (por exemplo, isinstance (instância, classe).
# __subclasscheck__ (self, subclasse)
#      Verifica se uma classe subclasse a classe que você definiu (por exemplo, issubclass (subclasse, classe)).  
  
  
# ---------------------- Metodos de contexto -------------------------------
# Os gerenciadores de contexto permitem que ações de configuração e limpeza sejam executadas para objetos 
# quando sua criação é agrupada com uma instrução with. 
# O comportamento do gerenciador de contexto é determinado por dois métodos mágicos:
  
# __enter__(self)
#      Define o que o gerenciador de contexto deve fazer no início do bloco criado pela instrução with. 
#      Observe que o valor de retorno de __enter__ está vinculado ao destino da instrução with ou ao nome após o as.
# __exit__(self, tipo de exceção, valor de exceção, retorno)
#      Define o que o gerenciador de contexto deve fazer depois que seu bloco for executado (ou finalizado). 
#      Pode ser usado para lidar com exceções, executar limpeza ou fazer algo sempre feito imediatamente após a ação no bloco. 
#      Se o bloco for executado com sucesso, exception_type, exception_value e traceback serão None. 
#      Caso contrário, você pode optar por manipular a exceção ou deixar que o usuário a manipule; 
#      se você quiser lidar com isso, certifique-se de que __exit__ retorne True depois que tudo estiver dito e feito. 
#      Se você não deseja que a exceção seja tratada pelo gerenciador de contexto, deixe acontecer.
  
# ---------------------- Metodos descritores -----------------------------------------
# 
# __get__ (self, instância, proprietário)
#      Defina o comportamento para quando o valor do descritor é recuperado. 
#       instance é a instância do objeto do proprietário. owner é a própria classe do proprietário.
# __set__ (self, instância, valor)
#      Defina o comportamento para quando o valor do descritor é alterado. 
#      instance é a instância da classe do proprietário e value é o valor para definir o descritor.
# __delete__ (self, instância)
#      Defina o comportamento para quando o valor do descritor é excluído. 
#      instance é a instância do objeto do proprietário. 
  

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
#      Define o comportamento de copy.copy () para instâncias da sua classe. 
#      copy.copy () retorna uma cópia superficial do seu objeto.
#      isso significa que, enquanto a instância em si é uma nova instância, todos os seus dados são referenciados.
#      ou seja, o próprio objeto é copiado, mas seus dados ainda são referenciados 
#      ( e, portanto, alterações nos dados em uma cópia superficial podem causar alterações no original).
# __deepcopy__ (self, memodict = {})
#      Define o comportamento de copy.deepcopy () para instâncias da sua classe. 
#      copy.deepcopy () retorna uma cópia profunda do seu objeto - o objeto e seus dados são copiados. 
#      memodict é um cache de objetos copiados anteriormente.
#      isso otimiza a cópia e evita a recursão infinita ao copiar estruturas de dados recursivas. 
#      Quando desejar copiar em profundidade um atributo individual, 
#      chame copy.deepcopy () nesse atributo com memodict como o primeiro argumento.

# -------------------- Metodos de pickling -------------------------------
# Vamos mergulhar em decapagem. Digamos que você tenha um dicionário que deseja armazenar e recuperar mais tarde. 
# Você pode escrever seu conteúdo em um arquivo, certificando-se cuidadosamente de escrever a sintaxe correta 
# e recuperá-lo usando exec () ou processando a entrada do arquivo. 
# Mas isso é precário, na melhor das hipóteses: se você armazenar dados importantes em texto sem formatação, 
# eles poderão ser corrompidos ou alterados de várias maneiras para causar uma falha no programa 
# ou pior execução de códigos maliciosos no seu computador.
# Exemplo:
# import pickle
# data = {'foo': [1, 2, 3],
#         'bar': ('Hello', 'world!'),
#         'baz': True}
# jar = open('data.pkl', 'wb')
# pickle.dump(data, jar) # write the pickled data to the file jar
# jar.close()

# __getinitargs__(self)
#     Se desejar que __init__ seja chamado quando sua classe não for escolhida, defina __getinitargs__, 
#     que retornará uma tupla dos argumentos que você gostaria de passar para __init__. 
#     Observe que esse método funcionará apenas para classes de estilo antigo.
# __getnewargs__(self)
#     Para classes de novo estilo, você pode influenciar quais argumentos são passados ​​para __new__ ao cancelar a seleção. 
#     Esse método também deve retornar uma tupla de argumentos que serão passados ​​para __new__.
# __getstate__(self)
#     Em vez de o atributo __dict__ do objeto ser armazenado, você pode retornar um estado personalizado a ser 
#     armazenado quando o objeto é selecionado. Esse estado será usado por __setstate__ quando o objeto não for escolhido.
# __setstate__ (self, estado)
#     Quando o objeto é retirado, se __setstate__ for definido, o estado do objeto será passado a ele em vez de diretamente aplicado ao __dict__ do objeto. Isso anda de mãos dadas com __getstate__: quando ambos são definidos, você pode representar o estado de pickled do objeto da maneira que desejar com o que quiser.
# __reduce__(self)
#     Ao definir tipos de extensão (ou seja, tipos implementados usando a API C do Python), você deve informar ao Python como selecioná-los, se desejar que eles os selecionem. __reduce __ () é chamado quando um objeto que o define é decapado. Ele pode retornar uma string que representa um nome global que o Python procurará e pickle, ou uma tupla. A tupla contém entre 2 e 5 elementos: um objeto que pode ser chamado para recriar o objeto, uma tupla de argumentos para esse objeto que pode ser chamado, estado a ser passado para __setstate__ (opcional), um iterador que gera itens da lista a serem selecionados (opcional) e um iterador que produz itens de dicionário a serem selecionados (opcional).
# __reduce_ex __(self)
#     __reduce_ex__ existe para compatibilidade. Se definido, __reduce_ex__ será chamado sobre __reduce__ na decapagem. __reduce__ também pode ser definido para versões mais antigas da API de decapagem que não suportavam __reduce_ex__.


# --------------- Metodo de chamada de funcao ---------------------
# __call __ (self, [args ...])
#     Permite que uma instância de uma classe seja chamada como uma função. 
#     Essencialmente, isso significa que x () é o mesmo que x .__ chama __ (). 
#     Observe que __call__ recebe um número variável de argumentos; 
#     isso significa que você define __call__ como faria com qualquer outra função, 
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
#  Como a distinção entre string e unicode foi eliminada no Python 3, __unicode__ desapareceu e 
#  __bytes__ (que se comporta de maneira semelhante a __str__ e __unicode__ na 2.7) 
#  existe para um novo built-in para a construção de matrizes de bytes.
#  Como o padrão de divisão é a divisão verdadeira no Python 3, __div__ desapareceu no Python 3
#  __coerce__ se foi devido à redundância com outros métodos mágicos e comportamento confuso
#  __cmp__ desapareceu devido a redundância com outros métodos mágicos
#  __nonzero__ foi renomeado para __bool__


# =============================== METODO DE CLASSE ================================
# @classmethod
# Métodos de objetos que examinamos até agora são chamados por uma instância de uma classe, 
# que é então passada para o auto-parâmetro do método.
# Os métodos de classe são diferentes - eles são chamados por uma classe, 
# que é passada para o parâmetro cls do método.
# Um uso comum desses métodos são os métodos de fábrica, que instanciam uma instância de uma classe, 
# usando parâmetros diferentes daqueles geralmente passados para o construtor de classes.
# Os métodos de classe são marcados com um decorador de método de classe.
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
# Métodos estáticos são semelhantes aos métodos de classe, exceto que eles não recebem argumentos adicionais; 
# eles são idênticos às funções normais que pertencem a uma classe.
# Eles são marcados com o decorador staticmethod ou criados com a classe staticmethod.

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