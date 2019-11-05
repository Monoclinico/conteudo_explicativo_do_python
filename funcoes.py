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

#com inumeros parametros
def my_function5(*kids):
  print("The youngest child is " + kids[2])

my_function5("Emil", "Tobias", "Linus") #The youngest child is Linus

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
