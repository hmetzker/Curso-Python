def split_pairs(a):
    lista=[]; tam=len(a)
    if (tam % 2 != 0):
        tam+=1; a=a+'_'

    for i in range(tam):
        if i<tam-1:
            lista.append(a[i:i+2])

    for i in range(len(lista)):
        if i<(len(lista)-1):
            lista.pop(i+1)

    return lista

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")