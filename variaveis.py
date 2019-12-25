# Variaveis em Python

# ================== NAMES ===============================
# Convencao de regras e nomeacao de variaveis e constantes

# Nomes de variaveis e constantes devem ser uma combinacao de letras minusculas (a-z) ou maiusculas (A-Z) ou 
# digitos(0-9) ou um underscore (_). Os nomes nao podem comecar com digitos.
# Exemplos:
# snake_case
# MACRO_CASE
# camelCase
# CapWords
# _private

# Os nomes de constantes deve ser em maiusculo.
# Exemplos:
# PI
# LIMITE
# VALOR_CONSTANTE


# Para declarar variaveis e constantes com mais de um nome, use (_) para separar os nomes.
# Exemplos:
# valor_total
# DATA_DE_NASCIMENTO
# _nota_do_aluno_1

# ======================== NUMBERS ===============================================
# Tipos numericos sao Integer, Float, and Complex. E possuem varias representacoes. 
# Exemplos: 

# Integer Literal
a = 0b1010  #Binary Literals
b = 100     #Decimal Literal 
c = 0o310   #Octal Literal
d = 0x12c   #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# =================== STRINGS ============================================
# Uma string e uma sequencia de caracteres e deve ser representada dentro de pares 
# de apostrofos, aspas, tres aspas ou tres apostrofos. 
# Os caracteres unicos devem ser envolvidos por um par de aspas ou um par de apostrofos.
# Exemplos: 
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# ================= BOOLEAN ==============================================
# O tipo booleano abrange dois valores, True ou False.
# Exemplo:
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# ================= NONE ==============================================
# None e usado para campos que nao foram criados
# Exemplo:
nenhum = None
print(nenhum)
print(type(nenhum))


# ================ COLLECTIONS =============================================
# Existem quatro colecoes literais diferentes: literais de lista, literais de tupla, 
# literais de ditado e literais de conjunto.
# Exemplo: 
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

# ================ ELLIPSIS ======================================================
# Representa um tipo vazio.
elip = ...
print(type(elip)) # <class 'ellipsis'>
print(elip) # Ellipsis
print(elip.__class__) # <class 'ellipsis'>

# ================ ANNOTATIONS ==================================================
some_number: int      # variavel com a anotacao de tipo inteiro e sem valor inicial.
some_list: list = []  # variavel com a anotacao de tipo lista e com valor inicial.
soma_name: str = ... # variavel iniciada sem qualquer valor.

some_number = 8
some_list.append(1)

print(some_number) #8
print(some_list) # [1]
print(soma_name) # Ellipsis

# ================ DESCOMPACTACAO, ENCURTAMENTOS E TRUQUES ==============================================

# atribuicao para multipla variaveis em uma linha 
a,b,c = 3,4,5
#ou
a,b,c = [3,4,5]

# para trocar os valor de duas variaveis sem ter que criar uma terceira:
x,y = 1,4
y,x = x,y # inverte-se a ordem

# concatenar listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [*lista1,*lista2]
print(lista3)
