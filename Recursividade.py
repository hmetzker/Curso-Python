def countdown(n):
    if n>0:
        print(n)
        countdown(n-1)

if __name__ == '__main__':
    while True:
        n_max=input('Digite o número máximo: \n')
        if n_max.isnumeric():
            countdown(int(n_max))
            print('Acabou'); break
