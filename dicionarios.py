#Construtor de dicionario
#dict()

#It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# clear()	Removes all the elements from the dictionary.
# clear() Remove todos os elemtnos do dicionario.
dicionario = {"um":1,"dois":2}
dicionario.clear()
print(dicionario) #{}

# copy() Returns a copy of the dictionary.
# copy() Retorna uma copia do dicionario.
dicionario = {"um":1,"dois":2}
dicionario2 = dicionario.copy()
print(dicionario2) #{'um': 1, 'dois': 2}

# fromkeys() Returns a dictionary with the specified keys and values.
# fromkeys() Retorna um dicionario das chaves e valores especificados.
nomes = ["um","dois"]
dicionario = dict.fromkeys(nomes,"numero")
print(dicionario) # {'um': 'numero', 'dois': 'numero'}

# get()	Returns the value of the specified key.
# get() Retorna o valor da chave especificada. 
dicionario = {"um":1,"dois":2}
print(dicionario.get("um")) #1

# items()	Returns a list containing a tuple for each key value pair.
# items() Retorna uma lista contendo varias tuplas com cada chave e seu valor.
dicionario = {"um":1,"dois":2}
lista_d = dicionario.items()
print(lista_d) #dict_items([('um', 1), ('dois', 2)])

# keys() Returns a list containing the dictionary's keys
# keys() Retorna um lista contendo as chaves do dicionario.
dicionario = {"um":1,"dois":2,"tres":3}
print(dicionario.keys()) #dict_keys(['um', 'dois', 'tres'])

# pop()	Removes the element with the specified key.
# pop() Remove o elemento com a chave especificada.
dicionario = {"um":1,"dois":2,"tres":3}
dicionario.pop("tres")
print(dicionario) #{'um': 1, 'dois': 2}

# popitem()	Removes the last inserted key-value pair.
# popitem() Remove o ultimo par de chave-valor inserido no dicionario.
dicionario = {"um":1,"dois":2,"tres":3}
dicionario.popitem()
print(dicionario) #{"um":1,"dois":2}

# setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
# setdefault() Retorna o valor da chave especificada. Se a chave nao existir, insere a chave com o valor padrao.
dicionario = {"um":1,"dois":2,"tres":3}
print(dicionario.setdefault("quatro",4)) #4
print(dicionario) #{'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4}

# update() Updates the dictionary with the specified key-value pairs.
# update() Insere no dicionario chave e valores especificados em um iteravel.
dicionario = {"um":1,"dois":2,"tres":3}
dicionario.update([("quatro",4)])
print(dicionario) # {'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4}

# values() Returns a list of all the values in the dictionary.
# values() retorna uma lista de todos os valores do dicionario.
dicionario = {"um":1,"dois":2,"tres":3}
print(dicionario.values()) #dict_values([1, 2, 3])