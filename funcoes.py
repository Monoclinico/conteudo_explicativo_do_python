# -*- coding: utf-8 -*-

#FUNCOES

#com retorno
def colocapimeiraletraemupper(palavra):
  if isinstance(palavra,str):
    return palavra.title()
  else:
    return palavra
nome = "Jeremias"
print(colocapimeiraletraemupper(nome)) # Jeremias

#sem retorno
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil") # Emil Refsnes

#com valor padrao no parametro 
def my_function2(country = "USA"):
  print("I am from " + country)
 
my_function2("Brazil") # I am from Brazil
my_function2() # I am from USA

#lista como parametro
def my_function3(food):
  for x in food:
    print(x,end="+")

fruits = ["apple", "banana", "cherry"]

my_function3(fruits) #apple+banana+cherry+

#como parametros chave-valor
def my_function4(child3, child2, child1):
  print("The youngest child is " + child3)

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #The youngest child is Linus

#com inumeros parametros (lista)
def my_function5(*kids):
  print("The youngest child is " + kids[2])

my_function5("Emil", "Tobias", "Linus") #The youngest child is Linus

#com dicionario como parametro
def my_function2153(**pesssoas):
  print(pesssoas)

my_function2153(Afonso=45,Beatriz=23) # {'Afonso': 45, 'Beatriz': 23}

#recurcao
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    #tri_recursion(3):
    # result = 3+tri_recursion(2) print(6)
    # result = 2+tri_recursion(1) print(3)
    # result = 1+tri_recursion(0) print(1)
    # result = 0
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Example Results")
tri_recursion(3)

#funcao anonima

maisdez = lambda a : a + 10
print(maisdez(5)) # 15

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #13

#retornando uma funcao anonima
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# As anotacoes para parametros assumem a forma de expressoes opcionais que seguem o nome do parametro:
# Os parametros podem ser declarados com: (parametro: expressão = expressão). 
# Ou seja, as anotações sempre precedem o valor padrão de um parametro e as anotações e os 
# valores padrão são opcionais. Assim como os sinais de igual são usados para indicar um valor padrão, 
# dois pontos são usados para marcar anotações. 
# Todas as expressões de anotação são avaliadas quando a definição da função é executada, 
# assim como os valores padrão.
# Usa-se ( -> ) para anotar qual sera o tipo do valor de retorno da funcao. Nao funciona com lambda. 
# Exemplo:  
def alguem(nome: str ,idade: int = 0, humano: bool = ...) -> str:
  """Argumentos -> nome, idade, se e humano True ou False."""
  if humano:
    print(nome +  " tem " + str(idade) + " anos.")
  else:
    print("Nao e humano.")

alguem("Marcos",45)
print(alguem.__annotations__) 
#{'nome': <class 'str'>, 'idade': <class 'int'>, 'humano': <class 'bool'>, 'return': <class 'str'>}
