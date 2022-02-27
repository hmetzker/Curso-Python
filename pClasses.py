# praticar

class Funcionario:
    def __init__(self, nome_ht, valor_ht):
        self.nome = nome_ht
        self.vht = valor_ht
        self.__sal = 0

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, novo_sal):
        raise ValueError("Somente na função calcula_sal")

    def calcula_sal(self):
        self.__sal = self.vht * 100
        return self.__sal

if __name__ == '__main__':
    x = Funcionario('haroldo', 10)
    print(f'nome= {x.nome}; valor da hora = {x.vht}')

    # passando pela função calcula_sal
    print(f'salário (100 horas * valor da hora) = {x.calcula_sal()}')
    print()

    # tentativa de alterar salário
    x.sal=1000
