class Geladeira: 
  def __init__(self): 
    self.temperatura = -20 
    self.minimo = -2 
    self.maximo = 2 
  def regularTemperatura(self): 
    if self.temperatura < self.minimo: 
      self.temperatura -= 1 
    elif self.temperatura < self.minimo: 
      self.temperatura += 1 
  def mostrarTemperatura(self): 
    print('Atual: {}.'.format(self.temperatura)) 