import random

def generate():
    lista = list()
    a=random.randint(0, 1); print(a)
    b=range(a); print(b)
    for i in b:
        lista.append(random.randint(0, 10))
        print(i)
        print(lista)
    return lista

if __name__ == '__main__':
  x=generate(); print(x)
  if len(x) == 0:
      print('a lista está vazia')
  else:
      print('a lista não está vazia')
