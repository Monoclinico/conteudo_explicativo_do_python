#SETS

#Os conjuntos nao podem ter itens repetidos.

#Construtor de conjuntos/sets:
thisset = set(("apple", "banana", "cherry"))
print(thisset) #{'banana', 'apple', 'cherry'}

#Comprimento dos conjuntos:
conjunto = {1,2,3,4,5}
print(len(conjunto)) #5


# add()	Adds an element to the set.
# add() Adiciona um elemento no conjunto.
conjunto_1 = {5,4,3,1} 
conjunto_1.add(7)
print(conjunto_1) # {1, 3, 4, 5, 7}

# clear()	Removes all the elements from the set.
# clear() Remove todos os elementos do conjunto.
conjunto_1 = {6,4,1,8,7}
conjunto_1.clear()
print(conjunto_1) # set()

# copy() Returns a copy of the set.
# copy() Retorna uma copia do conjunto.
conjunto_1 = {6,4,1,8,7}
conjunto_2 = conjunto_1.copy()
print(conjunto_2) #{1, 4, 6, 7, 8}

# difference() Returns a set containing the difference between two or more sets.
# difference() Retorna um conjunto contendo a diferenca entre dois ou mais conjuntos.
conjunto_1 = {6,4,1,8,7}
conjunto_2 = {6,4,5,8,7}
conjunto_3 = conjunto_1.difference(conjunto_2)
print(conjunto_3) #{1}

# difference_update()	Removes the items in this set that are also included in another, specified set.
# difference_update() Remove os itens no conjunto atual que estao tambem no outro. 
conjunto_1 = {6,4,1,8,7}
conjunto_2 = {9,3,5,8,7}
conjunto_1.difference_update(conjunto_2)
print(conjunto_1) #{1,4,6}

# discard()	Remove the specified item.
# discard() Remove o item especificado.
conjunto_1 = {6,4,1,8,7}
conjunto_1.discard(4)
print(conjunto_1) #{1, 6, 7, 8}

# intersection() Returns a set, that is the intersection of two other sets.
# intersection() Retorna um conjunto, que e a interseccao de outros dois conjuntos.
conjunto_1 = {6,4,1,8,7}
conjunto_2 = {9,3,5,8,7}
conjunto_3 = conjunto_1.intersection(conjunto_2)
print(conjunto_3) #{8,7}

# intersection_update()	Removes the items in this set that are not present in other, specified set(s).
# intersection_update() Remove os itens no conjunto que nao estao no outro.
conjunto_1 = {6,4,1,8,7}
conjunto_2 = {9,3,5,8,7}
conjunto_1.intersection_update(conjunto_2)
print(conjunto_1) # {8,7}

# isdisjoint() Return True if two sets have a null intersection.
# isdisjoint() Retorna True se dois conjuntos nao tem interseccao.

conjunto_1 = {6,4,1,8,7}
conjunto_2 = {9,3,5,8,7}
print(conjunto_1.isdisjoint(conjunto_2)) #False

# issubset() Returns whether another set contains this set or not.
# issubset() Retorna se o conjunto e um subconjunto de outro.
conjunto_1 = {6,8,7}
conjunto_2 = {8,7,6,9}
print(conjunto_1.issubset(conjunto_2)) # True

# issuperset() Returns whether this set contains another set or not.
# issuperset() Retorna se o conjunto tem um subconjunto especificado incluido nele.
conjunto_1 = {6,8,7,9}
conjunto_2 = {8,7,6}
print(conjunto_1.issuperset(conjunto_2)) # True

# pop()	Removes an random element from the set.
# pop() Remove um elemento aleatorio de um conjunto, mas se for numero, remove o menor.
conjunto_1 = {0,1,2,3}
conjunto_1.pop()
print(conjunto_1) # {1,2,3}

# remove() Removes the specified element.
# remove() Remove o elemento especificado.
conjunto_1 = {0,1,2,3}
conjunto_1.remove(2)
print(conjunto_1) # {0,1,3}

# symmetric_difference() Returns a set with the symmetric differences of two sets.
# symmetric_difference() Retorna um conjunto com a simetrica diferenca de dois conjuntos.
conjunto_1 = {6,8,7,9,2}
conjunto_2 = {8,7,6,1}
print(conjunto_1.symmetric_difference(conjunto_2)) #{1,2,9}

# symmetric_difference_update()	inserts the symmetric differences from this set and another.
# symmetric_difference_update() insere a diferenca simetrica no conjunto atual.
conjunto_1 = {6,8,7}
conjunto_2 = {8,7,6,5,1}
conjunto_1.symmetric_difference_update(conjunto_2)
print(conjunto_1) # {1,5}

# union()	Return a set containing the union of sets.
# union() Retorna um conjunto contendo a uniao entre conjuntos.
conjunto_1 = {6,8,7}
conjunto_2 = {8,7,6,5,1}
conjunto_3 = conjunto_1.union(conjunto_2)
print(conjunto_3) # {1, 5, 6, 7, 8}
conjunto_4 = conjunto_3.union("9")
print(conjunto_4) #{1, 5, 6, 7, 8,'9'}

# update() Update the set with the union of this set and others.
# update() Atualiza o conjunto com a uniao do conjunto atual com outros.
conjunto_1 = {6,8,7}
conjunto_2 = {8,7,6,5,1}
conjunto_1.update(conjunto_2)
print(conjunto_1) # {1, 5, 6, 7, 8}
