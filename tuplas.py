#TUPLES

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#Um vez criada uma tupla, voce nao pode adicionar itens nele.  Tuplas sao imutaveis. 

#Construtor de tuplas:
tupla = tuple((1,2,5,6))
print(type(tupla)) # <class 'tuple'>

tupla = tuple("tchau",)
print(type(tupla)) # <class 'tuple'>

#Comprimento das tuplas:
tupla = (1,2,3,4,5)
print(len(tupla)) #5

# count()	Returns the number of elements with the specified value.
# count() Retorna o numero de elementos com o valor especificado.
tupla = ("inicio","meio")
numero_meio = tupla.count("meio")
print(numero_meio) #1

# index()	Returns the index of the first element with the specified value.
# index(<elemento>, <indice onde iniciar>,<indice onde terminar>) Retorna o indice do primeiro elemento com o valor especificado. 
numeros = (1,2,5,4,1,2,3)
indice = numeros.index(2) 
print(indice) #1