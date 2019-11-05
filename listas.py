#LISTS

#Construtor de lista:
lista = list((1,2,5,6))
print(type(lista)) # <class 'list'>

#Comprimento das listas:
lista = [1,2,3,4,5]
print(len(lista)) #5

#Deletar itens:
lista = [1,5,7]
del lista[0]
print(lista) #[5,7]

#Slices
#Fatias
lista = ["pastel","colorido","e","soberbo"]
print(lista[0:-1]) #['pastel', 'colorido', 'e']
print(lista[-1::]) #['soberbo']
print(lista[-1:0]) #[]
print(lista[::])   #['pastel', 'colorido', 'e', 'soberbo']
print(lista[-4:-1]) #['pastel', 'colorido', 'e']
print(lista[::-1]) #['soberbo', 'e', 'colorido', 'pastel']

# append() Adds an element at the end of the list.
# append() Adiciona um elemento no final da lista.
lista = ["inicio","meio"]
lista.append("fim")
print(lista) # ["inicio", "meio", "fim"]
 
# clear()	Removes all the elements from the list.
# clear() Remove todos os elementos da lista.
lista = ["inicio","meio"]
lista.clear()
print(lista) # []

# copy() Returns a copy of the list.
# copy() Retorna uma copia da lista.
lista = ["inicio","meio"]
copia_lista = lista.copy()
print(copia_lista) # ["inicio","meio"]

# count()	Returns the number of elements with the specified value.
# count() Retorna o numero de elementos com o valor especificado.
lista = ["inicio","meio"]
numero_meio = lista.count("meio")
print(numero_meio) #1

# extend() Add the elements of a list (or any iterable), to the end of the current list.
# extend() Adiciona os elementos da lista ou de um iteravel, para o final da lista atual.
lista = ["inicio","meio"]
lista.extend(["fim"]) 
print(lista) # ["inicio", "meio", "fim"]

# index()	Returns the index of the first element with the specified value.
# index(<elemento>, <indice onde iniciar>,<indice onde terminar>) Retorna o indice do primeiro elemento com o valor especificado. 
numeros = [1,2,5,4,1,2,3]
indice = numeros.index(2) 
print(indice) #1

# insert() Adds an element at the specified position.
# insert(<indice>,<elemento>) Insere um elemento na posicao especificada.
lista = ["inicio","fim"]
lista.insert(1,"meio")
print(lista) # ["inicio", "meio", "fim"]

# pop()	Removes the element at the specified position.
# pop(<indice>[padrao = -1]) Remove o elemento da posicao especificada.
lista = ["inicio","meio","fim"]
lista.pop()
print(lista) # ["inicio","meio"]

# remove() Removes the item with the specified value.
# remove() Remove o primeiro item com o valor especificado.
lista = ["inicio", "meio", "fim"]
lista.remove("meio")
print(lista) # ["inicio", "fim"]

# reverse()	Reverses the order of the list.
# reverse() Inverte a ordem dos elementos da lista.
lista = ["inicio", "meio", "fim"]
lista.reverse()
print(lista) # ["fim","meio","inicio"]

# sort() Sorts the list.
# sort() Ordena a lista.
lista = [8,3,1,5,0]
lista.sort()
print(lista) # [0, 1, 3, 5, 8]

# To determine if a specified item is present in a list use the "in" keyword:
# Para determinar se um elemento especifico esta na lista usa-se a palavra "in":
print(4 in [2,5,4,1]) #True

# You can loop through the list items by using a for loop:
# Voce pode percorrer os elementos de uma lista atraves da palavra "in":
for x in ["C","h","i","l","e"]:
  print(x,end="") #Chile 
