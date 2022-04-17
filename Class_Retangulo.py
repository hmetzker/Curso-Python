import Classe

class retangulo:
    def __init__(self, x, y, z, w):
        self.altura = x
        self.largura = y
        self.canto = Classe.ponto(z, w)

# atributo r ou self
    def centro(self):
        print(self.f_altura())
        print(self.f_largura())

# atributo r ou self
    def f_altura(r):
        rx = r.canto.x + r.altura/2
        ry=0
        return int(ry), int(rx)

# atributo r ou self
    def f_largura(r):
        rx=0
        ry = r.canto.y + r.largura/2
        return int(rx), int(ry)

if __name__ == '__main__':
    box=retangulo(100, 200, 10, 20)
    box.centro()
