# trabalhando com lista do checkIO

def easy_unpack(elements: tuple) -> tuple:
    result = []
    l = list(elements)
    for i in range(len(l)):
        if i==0 or i==2:
            result.append(l[i])
        else:
            continue

    l = l[::-1]
    for i in range(len(l)):
        if i==1:
            result.append(l[i])
        else:
            continue

    res = result[0], result[1], result[2]
    return res

if __name__ == '__main__':
    print('Examples:')
    x = easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
    print(x)

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
