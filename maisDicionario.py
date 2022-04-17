# exemplo do gitHUB de Fernando Feltrin

usuarios = {'João': {'Identificador': '0001',
                     'Cargo': 'Porteiro',
                     'Salario': '2000'},
            'Maria': {'Identificador': '0003',
                      'Cargo': 'Aux. Limpeza',
                      'Salario': '1900'},
            'José': {'Identificador': '0002',
                     'Cargo': 'Técnico',
                     'Salario': '2500'}}

for i, j in usuarios.items():
    print(f'Funcionário: {i}')
    for k, l in j.items():
        print(f'\t {k} = {l}')

# exclui o último par <chad0 dicionário>:<valor>
usuarios.popitem()

for i, j in usuarios.items():
    print(f'Funcionário: {i}')
    for k, l in j.items():
        print(f'\t {k} = {l}')

