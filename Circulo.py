import math


def area_circle(r):
    area = math.pi * r ** 2
    return area


if __name__ == '__main__':
    print(' ESTA PARTE ESTA RODANDO ? só quando eu chamo/rodo/executo o arquivo function5.py ')
    raio = 10
    result = area_circle(raio)
    print(f'A área é: {result:.2f}')