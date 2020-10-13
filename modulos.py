# Quando o interpretador Python executa uma instrução import, ele:
# 1. Procura o arquivo correspondente ao módulo.
# 2. Executa o código do módulo para criar os objetos definidos no módulo.
# 3. Cria um namespace no qual os nomes desses objetos residirão

#Python utiliza um caminho de busca para localizar o módulo. 
# O caminho de busca é simplesmente uma lista de diretórios (ou pastas) onde o Python procurará os módulos. 
# O nome da variável path definido no módulo da Biblioteca Padrão sys refere-se a essa lista.
#import sys
#print(sys.path)

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

# Uma aplicação de computador é um programa que normalmente é dividido em vários arquivos (ou seja, módulos). 
# Em cada programa Python, um dos módulos é especial: ele contém o “programa principal”, significando o código que inicia a aplicação.
# Esse módulo é denominado módulo de alto nível. 
# Os módulos restantes são basicamente módulos de “biblioteca”, importados pelo módulo de alto nível e que contêm funções e classes usadas pela aplicação.

# Já vimos que, quando um módulo é importado, o interpretador Python cria algumas variáveis de “manutenção” no namespace do módulo. Uma destas é a variável _ _name_ _. Python definirá seu valor desta forma:

# -Se o módulo estiver sendo executado como um módulo de alto nível, o atributo _ _name_ _ é definido como a string _ _main_ _.

# -Se o arquivo estiver sendo importado por outro módulo, seja ele de alto nível ou não, o atributo _ _name_ _ é definido como o nome do módulo.