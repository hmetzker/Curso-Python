# teste for

def teste_2701():
    periodo=2701-1961+1
    print(f'Período = {periodo} anos'); print()
    for i in range(periodo):
        result1=i%7; result2=i%13
        if result1==0 or result2==0:
            print(f'O número {i} é divisível por 7 ou 13')

def oops_doo():
    for i in range(50):
        if i==0:
            continue
        else:
            result1=i%3; result2=i%5; od=0
            if result1==0 and result2==0:
                od=1
                print(f'i = {i} OopsDoo')
            if od==0 and result1==0:
                print(f'i = {i} Oops')
            if od==0 and result2==0:
                print(f'i = {i} Doo')

def vogal():
    lista_vogal=['a','e','i','o','u']
    x=input('Digite uma letra: ')
    while x!='fim':
        if x.isnumeric():
            print('Você não digitou uma letra')
        else:
            if x in lista_vogal:
                print(f'A letra {x} é vogal')
            else:
                print(f'A letra {x} é consoante')
        x=input('Digite uma letra: ')

def lista_qq():
    lista_num=[2,22,34,4,51,11]
    print(f'Primeiro valor = {lista_num[0]}')
    print(f'Último valor = {lista_num[-1]}')
    print(f'Número de elementos = {len(lista_num)}')
    print(f'Soma = {sum(lista_num)}')
    print(f'Média = {sum(lista_num)/len(lista_num)}')

if __name__ == '__main__':
    print(); teste_2701(); print()
    print(); oops_doo(); print()
    print(); vogal(); print()
    print(); lista_qq(); print(); print('Acabou')
