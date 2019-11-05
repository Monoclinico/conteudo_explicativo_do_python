#importar todo o modulo
import platform

print(platform.python_version())
print(platform.system())

#importar uma parte especifica
from math import sqrt
print(sqrt(4)) #2

#com apelido (outro nome)
from math import pow as potencia
print(potencia(8,2)) #64

#importar todas as partes diretamente
from random import *
print(choice([5,6,4]))


