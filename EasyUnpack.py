# trabalhando com lista do checkIO

def easy_unpack(elements: tuple) -> tuple:
    result = []
    l = list(elements)
    for i in range(len(l)):
        if i==0 or i==2: result.append(l[i])

    l = l[::-1]
    for i in range(len(l)):
        if i==1: result.append(l[i])

    return result[0], result[1], result[2]

""" result = []
    l = list(elements)
    tamanho=len(l)-2
    for i in range(len(l)):
        if tamanho>=2:
            if i==0 or i==2:
                result.append(l[i])
            if i==1:
                pass
            if i>2:
                result.append(l[tamanho])

            continue
        else:
            if tamanho==1:
                if i==0:
                    result.append(l[i])
                if i==1:
                    result.append(l[i+1])
                    result.append(l[tamanho])
                if i>1:
                    result.append(l[i])
            continue
"""
if __name__ == '__main__':
    print('Examples:')
    x = easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)); print(x)
    x = easy_unpack((6, 2, 9, 4, 3, 9)); print(x)
    x = easy_unpack((1, 1, 1, 1)); print(x)
    x = easy_unpack((6, 3, 7)); print(x)

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
