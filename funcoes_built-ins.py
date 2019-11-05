#coding: utf-8

#retorna o valor absoluto do número.
print(abs((-1)**(1/2))) # 1
print(abs(-352)) #352

#retorna "True" se todos os valores do iterável são verdadeiros, se não, retorna "False".
print(all([True,True,True])) #True
print(all([False,True,True])) #False

#retorna "True" se algum dos valores do iterável são verdadeiros, se não, retorna "False".
print(any([True,False,True])) #True

#retorna a um código representando um símbolo especial ('á') da tabela ascii, se o símbolo não estiver contido, retorna \x, \u ou \U.
print(ascii('á')) #'\xe1'

#retorna uma representação binária de um número inteiro
print(bin(10)) #'0b1010'

#Converte o valor passado em True ou False
print(bool('')) #False
print(bool(5)) #True

#O método bytearray () retorna um objeto bytearray que é uma sequência mutável (pode ser modificada) de inteiros no intervalo 0 <= x <256.
print(bytearray('a','ascii','ignore'))
#O método bytes() retorna um objeto bytes que é uma sequência imutável (não pode ser modificada) de inteiros no intervalo 0 <= x <256.
print(bytes('a','ascii','ignore'))
# string - texto. 'a'
# codificação - o tipo de codificação uma string tem que ser codificada. 'ascii'
# erros - resposta quando a codificação falha. Existem seis tipos de resposta de erro
#   -strict - resposta padrão que gera uma exceção UnicodeDecodeError em caso de falha
#   -ignore - ignora o unicod unencodable do resultado
#   -replace - substitui o unicode unencodível por um ponto de interrogação ?
#   -xmlcharrefreplace - insere referência de caracteres XML em vez de unicode unencodable
#   -backslashreplace - insere uma sequência de espace \ uNNNN em vez de unicode unencodable
#   -namereplace - insere uma seqüência de escape \ N {...} em vez de unicode unencodable

#verifica se um objeto é chamavel
print(callable(print)) #True

#retorna um caractere (uma string) de um inteiro (representa o ponto de código unicode do caractere).
print(chr(50)) # 2
print(chr(60)) # <

#O método classmethod () retorna um método de classe para a função especificada.
# ou
# @classmethod
# def xxx(cls):
class Person:
    age = 25

    @classmethod
    def printAge(cls):
        print('a idade é:', cls.age)

Person.printAge()

#O método compile () retorna um objeto de código Python da origem (cadeia normal, uma cadeia de bytes ou um objeto AST).
#compile (fonte, nome do arquivo, mode, flags = 0, dont_inherit = False, otimizar = -1)

x = 'k=4\nj=10\nprint(k*j)'
n = compile(x,'','exec')
exec(n)
# source - uma cadeia normal, uma cadeia de bytes ou um objeto AST
# filename- arquivo do qual o código foi lido. Se não foi lido de um arquivo, você pode dar um nome a si mesmo
# mode- Ou execou evalou single.
# eval - aceita apenas uma única expressão.
# exec - Pode pegar um bloco de código que tenha instruções, classes e funções do Python e assim por diante.
# single - se consistir em uma única instrução interativa
# flags(opcional) e dont_inherit(opcional) - controla quais declarações futuras afetam a compilação da fonte. Valor padrão: 0
# optimize(opcional) - nível de otimização do compilador. Valor padrão -1.

#O método complex () retorna um número complexo quando partes reais e imaginárias são fornecidas
# ou converte uma string em um número complexo.O método complex () retorna um número complexo quando
# partes reais e imaginárias são fornecidas ou converte uma string em um número complexo.
z = complex(8,1)
print(z)

#O delattr () exclui um atributo do objeto (se o objeto permitir).
class F:
    exemplo_1 = 5
    exemplo_2 = 6
delattr(F,'exemplo_2')

#O construtor dict () cria um dicionário no Python.
numbers1 = dict([('x', 5), ('y', -5)],z = 5.0)
print(numbers1)

#O método dir () tenta retornar uma lista de atributos válidos do objeto.
class Pessoa:
  def __dir__(self):
    return ['age', 'name', 'salary']
teacher = Person()
print(dir(teacher))#['age', 'name', 'salary']

#O método divmod () usa dois números e retorna um par de números (uma tupla) que consiste em seu quociente e resto.
print(divmod(5, 5)) #(1, 0)
print(divmod(8.0, 3)) #(2.0, 2.0)

#O método enumerate () adiciona um contador a um iterável e o retorna (o objeto enumerado).
comidas = ['bread', 'milk', 'butter']
enumerate_comidas = enumerate(comidas)
print(list(enumerate_comidas)) #[(0, 'bread'), (1, 'milk'), (2, 'butter')]

#O método eval () analisa a expressão passada para este método e executa a expressão (código) do python dentro do programa.
#eval (expressão, globals = None, locals = None)
# expressão - essa string é analisada e avaliada como uma expressão Python
# globals (opcional) - um dicionário
# locals (opcional) - um objeto de mapeamento. Dicionário é o tipo de mapeamento padrão e comumente usado no Python.
expressao = '6+2'
print(eval(expressao, {}, {})) #8

#O método exec () executa o programa criado dinamicamente, que é uma string ou um objeto de código.
#exec (objeto, globals, locals)
expressao_2 = 'print(6+2)'
exec(expressao_2, {}, {}) #8
#eval() retorna valores e exec() executa instruções diretamente.

#O método filter () constrói um iterador a partir de elementos de um iterável para o qual uma função retorna true.
#filter(função, iterável)
# função - função que testa se os elementos de um iterável retornam verdadeiro ou falso
# Se nenhum, a função padroniza a função Identidade - que retorna falso se algum elemento for falso
# iterável - iterável que deve ser filtrado, pode ser conjuntos , listas , tuplas ou contêineres de quaisquer iteradores
so_um = list(filter(lambda x:x,[1,0,1,1,1,0,0]))
print(so_um) #[1, 1, 1, 1]

#O método float () retorna um número de ponto flutuante de um número ou uma string.
print(float('5.1')) #5.1
print(float(77)) #77.0

#O método format () interno retorna uma representação formatada do valor fornecido controlado pelo especificador de formato.
#format(valor [, formato_espec])
#formato_espec:
# [[preencher] alinhar] [assinar] [#] [0] [largura] [,] [. precisão] [tipo]
# onde, as opções são
# preenchidas :: = qualquer caractere
# alinhar :: = "<" | ">" | "=" | "^"
# assinar :: = "+" | "-" | ""
# largura :: =
# precisão inteira :: =
# tipo inteiro :: = "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
# '<' - Left aligns the result (within the available space)
# '>' - Right aligns the result (within the available space)
# '^' - Center aligns the result (within the available space)
# '=' - Places the sign to the left most position (Força o preenchimento após o sinal (se houver),
#  mas antes dos dígitos. Isso é usado para imprimir campos no formato '+000000120'. 
# Esta opção de alinhamento é válida apenas para tipos numéricos.)
# '+' - Use a sign to indicate if the result is positive or negative
# '-' - Use a sign for negative values only
# ' ' - Use a leading space for positive numbers
# ',' - Use a comma as a thousand separator
# '_' - Use a underscore as a thousand separator
# 'b' - Binary format
# 'c' - Converts the value into the corresponding unicode character
# 'd' - Decimal format
# 'e' - Scientific format, with a lower case e
# 'E' - Scientific format, with an upper case E
# 'f' - Fix point number format
# 'F' - Fix point number format, upper case
# 'g' - General format
# 'G' - General format (using a upper case E for scientific notations)
# 'o' - Octal format
# 'x' - Hex format, lower case
# 'X' - Hex format, upper case
# 'n' - Number format
# '%' - Percentage format
print(format(123.4567, "^-09.3f")) #0123.4570
print(format("BANCO PYTHON","=^50"))


#O método frozenset () retorna um objeto frozenset imutável inicializado com elementos do iterável fornecido.
#frozenset ([iterável])
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet) #({'a', 'i', 'e', 'u', 'o'})

#O método getattr () retorna o valor do atributo nomeado de um objeto. Se não for encontrado,
#retorna o valor padrão fornecido para a função.
#getattr(objeto, nome [, padrão])
# object - objeto cujo valor do atributo nomeado deve ser retornado
# name - string que contém o nome do atributo
# default (Opcional) - valor que é retornado quando o atributo nomeado não é encontrado
class Pessoa1:
    age = 23
    name = "Adam"

print('The age is:', getattr(Pessoa1, "age"))
print('The age is:', Pessoa1.age)

#O método globals () retorna o dicionário da tabela de símbolos global atual.
# Uma tabela de símbolos é uma estrutura de dados mantida por um compilador que contém todas as informações necessárias sobre o programa.
# Estes incluem nomes de variáveis, métodos, classes, etc.
print(globals())

#O método hasattr () retorna true se um objeto tiver o atributo nomeado dado e false se não tiver.
#hasattr (object, nome)
class Pessoa2:
    age = 23
    name = "Adam"
pes = Pessoa2()
print('The age is:', hasattr(Pessoa2, "age"))
print('The age is:', hasattr(pes,'pay'))

#O método hash () retorna o valor de hash de um objeto, se tiver um.
#hash(objeto)
print(hash(123))#123

#O método help () chama o sistema de ajuda integrado do Python.
print(help()) #ajuda sobre o método

#A função hex () converte um número inteiro na string hexadecimal correspondente.
print(hex(123)) #0x7b

#A função id () retorna identidade (inteiro único) de um objeto.
n= 18
print(id(n)) #521...
# A função id () retorna a identidade do objeto. Este é um inteiro
# que é único para o objeto dado e permanece constante durante sua vida útil.

#O método input () lê uma linha da entrada, converte em uma string e a retorna.
b = input('exemplo')

#O método int () retorna um objeto inteiro de qualquer número ou string.
print(int('5')) #5
print(int(6.88)) #6

#A função isinstance () verifica se o objeto (primeiro argumento) é uma instância
# ou subclasse da classe classinfo (segundo argumento).
#isinstance (object, classinfo)
print(isinstance(7,int)) #True

#A função issubclass () verifica se o argumento do objeto (primeiro argumento)
# é uma subclasse da classe classinfo (segundo argumento).
class Z:
    pass
class M(Z):
    pass
print(issubclass(M,Z)) #True

#O método iter () retorna um iterador para o objeto fornecido.
# iter (objeto [, sentinela])
l = iter([i for i in range(0,10)])

#A função len () retorna o número de itens (comprimento) de um objeto.
print(len('541'))

#O construtor list () cria uma lista em Python.
#list([iterável])
print(list((2,4))) #[2,4]

#O método locals () atualiza e retorna um dicionário da tabela de símbolos local atual.
print(locals())

#A função map () aplica uma função específica a cada item de um iterável (lista, tupla, etc.) e
#  retorna uma lista dos resultados.
#map(função, iterável, ...)
i = list(map(lambda k: k*10, [2,6]))
print(i) #[20,60]

#O método max () retorna o maior elemento em um iterável ou maior de dois ou mais parâmetros.
#max (iterável, * iteráveis ​​[, chave, padrão])
# iterable - sequence ( tuple , string ), collection ( conjunto , dicionário ) ou um objeto iterador cujo maior elemento deve ser encontrado
# * iteráveis ​​(Opcional) - qualquer número de iteráveis ​​cujo maior seja encontrado
# key (Opcional)  - função de chave na qual os iteráveis ​​são passados ​​e a comparação é executada com base em seu valor de retorno
# padrão (Opcional) - valor padrão se o iterável fornecido estiver vazio
print(max([1,4,8])) #8

#O método memoryview () retorna um objeto de visualização de memória do argumento fornecido.
b = bytearray('abcd','ascii')
c = memoryview(b)
c[1] = 100
print(b) #adcd

#O método min () retorna o menor elemento em um iterável ou menor de dois ou mais parâmetros.
print(min([1,4,8])) #1

#A função next () retorna o próximo item do iterador.
# iterator - next () recupera o próximo item do iterador
# default (opcional) - este valor é retornado se o iterador estiver esgotado (nenhum item restante)
g = iter([1,2,3,5])
print(next(g)) #1

#Isso retorna um objeto sem recursos que é uma base para todas as classes.
o = object()

#O método oct () recebe um número inteiro e retorna sua representação octal. Se o número dado for um int,
#  ele deve implementar o método __index __ () para retornar um inteiro.
oct(8)#

#A função open () abre o arquivo (se possível) e retorna um objeto de arquivo correspondente.
#open('arquivo', modo, armazenamento em buffer = -1, codificação = Nenhum, erros = Nenhum, nova linha = Nenhum, closefd = Verdadeiro, abridor = Nenhum)
try:
    f = open("path_to_file", mode = 'r', encoding='utf-8')
except:
    pass

#O método ord () retorna um inteiro representando o ponto de código Unicode para o caractere Unicode fornecido.
print(ord('a')) #97

#O método pow () retorna x à potência de y. Se o terceiro argumento (z) é dado, ele retorna x à potência de y módulo z, isto é, pow (x, y)% z.
print(pow(7, 2, 5)) #4

#A função print () imprime o objeto fornecido para o dispositivo de saída padrão (tela) ou para o arquivo de fluxo de texto.
print('blabla') #blabla

#O método property () a retorna um atributo de propriedade.
#property (fget = Nenhum, fset = Nenhum, fdel = Nenhum, doc = Nenhum)
# fget (Opcional) - função para obter o valor do atributo
# fset (Opcional) - função para definir o valor do atributo
# fdel (Opcional) - função para deletar o valor do atributo
# doc (Opcional) - string que contém a documentação (docstring) para o atributo
f = property()
#@property
# função   
# @name.setter
# função
# @name.deleter
# função

#O tipo range () retorna uma seqüência imutável de números entre o inteiro de início especificado e o inteiro de parada.
x = range(4) #objeto gerador
print(list(x)) #[1,2,3,4]

#O método repr () retorna uma representação imprimível do objeto dado.
#repr(object)
print(repr(pow)) #<built-in function pow>

#O método invertido () retorna o iterador invertido da sequência dada.
#reversed(sequence)
print(list(reversed([1,2,3]))) #[3,2,1]

#O método round () retorna o número de ponto flutuante arredondado para os dígitos ndigits dados após o ponto decimal. 
# Se nenhum ndigits for fornecido, ele arredondará o número para o inteiro mais próximo.
#round (number [, ndigits])
print(round(5.66666,2)) #5.67

#O construtor set () constrói um conjunto Python a partir do iterável fornecido e o retorna.
#set ([iterável])
print(set([1,2,3,4,5,6])) #{1,2,3,4,5,6}

#O método setattr () define o valor do atributo dado de um objeto.
class Exemplo:
    x = 0
setattr(Exemplo,'x',1)

#O construtor slice () cria um objeto de fatia representando o conjunto de índices especificado por intervalo (start, stop, step).

fatia = slice(0,7)
palavra = "mosca volante"
print(palavra[fatia]) #mosca v

#O método sorted () retorna uma lista classificada do iterável fornecido.
#sorted(iterable[, key][, reverse])
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
sortedList = sorted(random, key=takeSecond)
print('Sorted list:', sortedList) # [(4,1),(2,2),(1,3),(3,4)]

#A função interna staticmethod () retorna um método estático para uma determinada função.
#@staticmethod
# O método estático não sabe nada sobre a classe e apenas lida com os parâmetros.
# O método de classe trabalha com a classe, já que seu parâmetro é sempre a própria classe.
class Person_77:
    age = 77
    @staticmethod
    def printAge():
        print('a idade é:', Person_77.age)

#O método str () retorna a representação "informal" ou bem impressa de um determinado objeto.
# object - objeto cuja representação informal deve ser retornada
# encoding  - Padrões de UTF-8. Codificação do objeto fornecido
# erros - resposta quando a decodificação falha. Existem seis tipos de resposta de erro
# strict - resposta padrão que gera uma exceção UnicodeDecodeError em caso de falha
# ignore - ignora o unicod unencodable do resultado
# replace - substitui o unicode unencodível por um ponto de interrogação ?
# xmlcharrefreplace - insere referência de caracteres XML em vez de unicode unencodable
# backslashreplace - insere uma sequência de espace \ uNNNN em vez de unicode unencodable
# namereplace - insere uma seqüência de escape \ N {...} em vez de unicode unencodable
print(str('sucesso')) #sucesso

#A função sum () adiciona os itens de um iterável e retorna a soma.
#sum(iterável, +algum_valor)
print(sum([0,1,2,3,4],2)) #12

#O super () builtin retorna um objeto proxy que permite que você indique a classe pai por 'super'.
# Nos permite evitar o uso explícito da classe base
# Trabalhando com herança múltipla
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName,'é meu nome.')
    
class Dog(Mammal):
  def __init__(self,nome):
    super().__init__(nome)
    
d1 = Dog('REX') # REX é meu nome.

#O built-in tuple () é usado para criar uma tupla no Python.
print(tuple([1,2,3,4])) #(1,2,3,4)

# Se um único argumento (objeto) é passado para o tipo () embutido, ele retorna o tipo do objeto dado. 
# Se três argumentos (name, bases e dict) forem passados, ele retornará um novo objeto de tipo.
# type(object)
# type(name, bases, dict)
class Poo:
    pass
poo = Poo()
print(type(poo)) #<class '__main__.Poo'>

#A função vars () retorna o atributo __dict__ do objeto dado se o objeto tiver o atributo __dict__.
#vars(objeto)
print(vars())

#A função zip () pega iteráveis ​​(pode ser zero ou mais), faz iterador que agrega elementos baseados nos
#  iteráveis ​​passados ​​e retorna um iterador de tuplas.
#zip (*iteráveis)
print(dict(zip(['a','b','c'],[1,2,3]))) # {"a":1,"b":2,"c":3}

#O __import __ () é uma função avançada que é chamada pela declaração de importação.
#__import __ (nome, globals = None, locals = None, fromlist = (), nível = 0)
# nome - nome do módulo que você deseja importar
# globais e locais - determina como interpretar o nome
# fromlist - objetos ou submódulos que devem ser importados pelo nome
# level - especifica se é necessário usar importações absolutas ou relativas
mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5)) #2.5

