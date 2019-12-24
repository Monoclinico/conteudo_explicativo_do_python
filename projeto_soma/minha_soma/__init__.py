def soma(args):
  assert (isinstance(args,(list,tuple))),"Argumento invalido"
  total = 0
  for n in args:
    total += n
  return total