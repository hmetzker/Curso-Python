from collections import defaultdict
from lists_generator import generate

def concatenar_dicts(*args):
    # Update method retorna None, mas modifica o objeto
    # o asterisco transforma args numa lista, podendo receber variado números de inputs:  0, 1, 3, ...
    # https://www.geeksforgeeks.org/args-kwargs-python/
    d = dict()
    for j in args:
        d.update(j)
    return d

def exemplos_default_dict():
    l1, l2 = generate(3), generate(10)

    # list1
    d_list = defaultdict(list)
    d_list[0] += l1
    d_list[0] += l2

    # list2
    for j in l1:
        # NOTE QUE A KEY 1 NÃO EXISTE AINDA NESSE DICIONÁRIO
        d_list[1].append(j)

    # int
    d_int = defaultdict(int)
    for j in l1:
        d_int[1] += j ** 2
    return d_list, d_int

if __name__ == '__main__':
    # basics
    d1 = dict()
    d1['primeira_key'] = 'primeiro valor'
    print(d1)

    d2 = {'segunda': 'segundo'}

    # KEYS
    d4 = {'key1': 100, 'key2': 'vinte e três', 'key3': [11, 10, 54, 43]}
    d4['key_diferente'] = 'nao vai imprimir, se estiver iterando com inteiro'

    print(f"{'key3' in d4}")

    for i in range(5):
        if f'key{i}' in d4:
            print(f'key{i} presente')

    # VALUES
    print(d4['key3'])

    for i in range(5):
        if f'key{i}' in d4:
            print(f"{d4[f'key{i}']}")

    # SIMPLE ITERATION sobre um dicionário, cujo padrão é sua lista de chaves
    for i in d4:
        print(f'esta é uma key: {i}')

    # Iterando e produzindo valores
    for key in d4:
        print(d4[key])

    # ITERATING A DICTIONARY
    for key, value in d4.items():
        print(f'k é a key: {key}')
        print(f'v é o value: {value}')

    for v in d4.values():
        print(v)
        if type(v) == list:
            print(f'Isso é a uma lista, o primeiro elemento é {v[0]}')
            print(f'O último é {v[-1]}')
            print('vou tentar, somar, se for de inteiros ou strings, ok...')
            print(f'a soma da lista é: {sum(v)}')
        else:
            print(f'{v} não é uma lista')
        print('--------')

    # UPDATE
    d3 = concatenar_dicts(d1, d2)
    print(d3)

    # ZIP examples
    names = ['john', 'mary', 'leopold']
    ages = [45, 67, 93]

    d_zip = dict()
    for name, age in zip(names, ages):
        d_zip[name] = age

    print(d_zip)

    # Calcule a média das idades
    m = sum(d_zip.values()) / len(d_zip)
    print(f'{m:.2f}')

    # DEFAULTDICT
    d5, d6 = exemplos_default_dict()
    print(d5)
    print(d6)
