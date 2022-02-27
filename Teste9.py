# coding=utf-8
# teste de try e except value error

try:
    num1 = int(raw_input('Entre um número: '))
    num2 = int(raw_input('Entre outro número: '))

except ValueError:
    print('Você não entrou um número... Por favorzinho, entre com um número inteiro')
    num1 = int(raw_input('Entre um número: '))
    num2 = int(raw_input('Entre outro número: '))

resultado = num1 + num2
print 'A soma é', resultado
