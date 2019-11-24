# Excecoes no Python

# =================================================================================================
# TRY/EXCEPT
# Mesmo se uma declaracao ou expressao estiver sintaticamente correta,
# podera causar um erro quando for feita uma tentativa de executa-la. 
# Os erros detectados durante a execucao sao chamados de excecoes 
# e nao sao incondicionalmente fatais: voce aprendera em breve como lidar com eles em programas Python. 

# No Python, as excecoes podem ser tratadas usando uma instrucao try.
# Uma operacao critica que pode gerar uma excecao e colocada dentro da clausula try e o 
# codigo que manipula a excecao e gravado na clausula exceto.
# Cabe a nos quais operacoes realizamos depois de capturarmos a excecao. 
# Aqui esta um exemplo simples:
import sys
randomList = ['a', 0, ...]
for entry in randomList:
  try:
    r = 1/int(entry)
  except:
    print("Erro: ",sys.exc_info()[0])

# Erro:  <class 'ValueError'>
# Erro:  <class 'ZeroDivisionError'>
# Erro:  <class 'TypeError'>

# =================================================================================================
# TRY/EXCEPT
# Uma clausula try pode ter qualquer numero de excecao, para manipula-las de maneira diferente, 
# mas apenas uma sera executada caso ocorra uma excecao.
# Exemplo:
for entry in randomList:
  try:
    n = 1/int(entry)
  # as -> para apelidar o erro
  except (ValueError, TypeError) as erro: 
    print(erro) 
    # invalid literal for int() with base 10: 'a'
    # int() argument must be a string, a bytes-like object or a number, not 'ellipsis'
  except ZeroDivisionError as erro:
    print(erro) # division by zero

# =================================================================================================
# TRY/EXCEPT/FINALLY
# A instrucao try no Python pode ter uma clausula finalmente opcional. 
# Esta clausula e executada independentemente do que for e geralmente e usada para liberar recursos externos.
f: "arquivo" = ...
try:
    f = open("test.txt",encoding = 'utf-8')
    # perform file operations
except FileNotFoundError as erro:
  print(erro) # [Errno 2] No such file or directory: 'test.txt'
finally:
  try:
    f.close()
  except:
    print("Arquivo nao pode ser fechado porque nao foi criado.")

# =================================================================================================
# raise classe_de_erro("mensagem")
# Na programacao Python, as excecoes sao geradas quando erros correspondentes ocorrem no tempo de execucao, 
# mas podemos chama-las a forca usando a palavra-chave raise.
# Exemplo:

try:
  raise Exception
except:
  print("Um erro ocorreu com sucesso!")

# =================================================================================================
# assert (condition),("mensagem")
# O Python possui uma declaracao de declaracao interna para usar a condicao de declaracao no programa. 
# A declaracao assert tem uma condicao ou expressao que deveria ser sempre verdadeira. 
# Se a condicao for falsa, a declaracao interrompe o programa e fornece um AssertionError.
# Exemplo:

x = 1
try: 
  assert (x == 0),("Um erro ocorreu.")
except:
  print("Um AssertionError ocorreu.")

# =================================================================================================
# Arvore de erros abrangidos pelo Python:
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


# =================================================================================================
# Criando uma classe de erro:
class ErroDeDivisaoPorZero (ZeroDivisionError):
  pass

try:
  raise ErroDeDivisaoPorZero
except ErroDeDivisaoPorZero:
  print("ErroDeDivisaoPorZero ocorreu.")

try:
  raise ErroDeDivisaoPorZero("argumento")
except ErroDeDivisaoPorZero as erro_zero:
  print(erro_zero.args)
  print(erro_zero.with_traceback(print(44)))


# =================================================================================================
# TRY/EXCEPT/ELSE/FINALLY

try:
  div = int(0)
  print("Inicio da divisao.")
  print(100/div)
except TypeError:
  print("Erro de tipo.")
except ValueError:
  print("Erro de valor.")
except BaseException:
  print("Erro desconhecido.")
else:
  #se nenhuma excecao ocorrer.
  print("Nenhum erro ocorreu.")
finally:
  print("Fim da divisao.")



