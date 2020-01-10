# O uso do Async, Await e AsyncIO no python
# O AsyncIO é um módulo que chegou no python 3.4 no qual permite que escrevemos códigos assíncronos 
# em uma unica thread utilizando Coroutines.

#  Coroutines
#  São rotinas cooperativas, ou seja, são rotinas (funções, métodos, procedimentos) que concordam em 
#  parar sua execução permitindo que outra rotina possa ser executada naquele momento esperando que 
#  essa rotina secundária devolva a execução para ela em algum momento, portanto uma coopera com a outra.
#  
#  Event Loop
#  O Event loop é um loop que pode registrar tasks para serem executadas, executa-las, pausa-las e 
#  então torna-las em execução a qualquer momento. 
#  Ele é o responsável por gerenciar todos eventos relacionados a isso.
#  No Python o Event Loop é responsável por manter o registro de tarefas (coroutines) e 
#  distribui a carga de execução entre elas.

import time
import asyncio

def numeros_consecutivos(lista_inteiros =[]):
  quantidade_faltante = 0 
  lista_inteiros = list(set(lista_inteiros))
  lista_inteiros.sort()
  for posicao in range(len(lista_inteiros)-1):
    quantidade_faltante += ((abs(lista_inteiros[posicao] - lista_inteiros[posicao+1]))-1)
  return quantidade_faltante

def quantidade_consecutiva_sincrona(lista_original, n):
  print("Calculando quantos numeros faltam para deixar a "+ str(n)+"º lista consecutiva...")
  time.sleep(0.01)
  quantidade_faltante = numeros_consecutivos(lista_original)
  print(quantidade_faltante)
  return quantidade_faltante

async def quantidade_consecutiva_assincrona(lista_original, n):
  print("Calculando quantos numeros faltam para deixar a "+ str(n)+"º lista consecutiva...")
  await asyncio.sleep(0.01)
  quantidade_faltante = numeros_consecutivos(lista_original)
  print(quantidade_faltante)
  return quantidade_faltante

#-----------------------------------------
# Execucao sincrona
def main_sincrona():
  quantidade_consecutiva_sincrona([5,3,9,75,42],1)
  quantidade_consecutiva_sincrona([5,3,-10,7,15],2)
  quantidade_consecutiva_sincrona([0,-20,10,7,12],3)
print("\nSincrona:")
t0 = time.time()
main_sincrona()
t1 = time.time()
print("Tempo da execucao sincrona: "+str(round((t1-t0)*1000,5))+"ms")
#-----------------------------------------

#-----------------------------------------
# Execucao assincrona
async def main_assincrona():
  await asyncio.wait([
  quantidade_consecutiva_assincrona([5,3,9,75,42],1),
  quantidade_consecutiva_assincrona([5,3,-10,7,15],2),
  quantidade_consecutiva_assincrona([0,-20,10,7,12],3)])

print("\nAssincrona:")
t2 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main_assincrona())
t3 = time.time()
print("Tempo da execucao assincrona: "+str(round((t3-t2)*1000,5))+"ms")

#-----------------------------------------
