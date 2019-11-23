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