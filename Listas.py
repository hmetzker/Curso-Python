import random

def generate():
    lista = list()
    for i in range(random.randint(0, 1)):
        lista.append(random.randint(0, 10))
    return lista

if __name__ == '__main__':
  a = generate()
  if len(a) == 0:
      print('a lista está vazia')
  else:
      print('a lista não está vazia')
