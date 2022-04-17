# Exemplo de uma class construída coletivamente

import math

class ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_ponto(p):
        print(p.x)
        print(p.y)
        print(int(math.sqrt(p.x**2+p.y**2)))

if __name__ == '__main__':
    a=ponto(100, 200)
    print(a)
    a.print_ponto()

