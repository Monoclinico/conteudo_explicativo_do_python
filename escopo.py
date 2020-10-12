# Os nomes atribuídos durante a execução de uma chamada de função são considerados nomes locais, com relação a uma chamada de função. 
# Os nomes locais a uma função existem apenas no namespace associado à chamada de função. Eles:
# -São visíveis apenas ao código dentro da função.
# -Não interferem com os nomes definidos fora da função, mesmo que sejam os mesmos.
# -Existem apenas durante a execução da função; eles não existem antes que a função inicie a execução nem depois que a função termina sua execução.


# Como o interpretador Python decide se avaliará um nome como um nome local ou global?
# Sempre que o interpretador Python precisa avaliar um nome (de uma variável, função etc.), ele procura a definição de nome nesta ordem:
# -Primeiro, o namespace da chamada da função delimitadora.
# -Depois, o namespace global (módulo).
# -Por fim, o namespace do módulo builtins.

#ESCOPOS

#ESCOPO LOCAL

def myfunc():
  x = 300 # x e local
  print(x)

myfunc() #300

#ESCOPO GLOBAL

y = 300

def myfunc2():
  print(y)

myfunc2() #300

#Global e Local juntos

z = 300

def myfunc3():
  z = 200
  print(z)

myfunc3() #200

print(z) #300

#palavra global faz com que um variavel tenha escopo global

def myfunc4():
  global a
  a = 900

myfunc4() #900

print(a) #900


#palavra nonlocal faz com que o acesso seja ampliado para o escopo do nivel mais acima.

def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()