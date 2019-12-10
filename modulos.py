#importar todo o modulo
#lento
import platform

print(platform.python_version())
print(platform.system())

#importar uma parte especifica
#mais rapido
from math import sqrt
print(sqrt(4)) #2

#com apelido (outro nome)
from math import pow as potencia
print(potencia(8,2)) #64

#importar todas as partes diretamente
#mais lento
from random import *
print(choice([5,6,4]))

#importar utilizando a funcao __import__()
tempo = __import__('time', globals(), locals(), [])
tempo.sleep(5)