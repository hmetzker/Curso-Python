# teste de senha
import random
import sys

def senha(parametro):
    while True:
        x=input('Digite a senha ')
        if x=='fim':
            sys.exit()

        if x.isnumeric():
            if int(x)==parametro:
                break
            elif int(x)>parametro:
                print('A senha é menor... ')
            else:
                print('A senha é maior... ')
        else:
            print('A senha tem que ser numérica... ')

if __name__ == '__main__':
    parametro=random.randint(0, 100)
    senha(parametro)
    print('A senha está correta')
