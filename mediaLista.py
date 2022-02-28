# trabalhando com lista do checkIO

def easy_unpack(elements: tuple) -> tuple:
    result = []
    l = list(elements)
    for i in range(len(l)):
        result=sum(l)
        result=result/len(l)

    return result

if __name__ == '__main__':
    print('Examples:')
    x = easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)); print(x)
    x = easy_unpack((6, 2, 9, 4, 3, 9)); print(x)
    x = easy_unpack((1, 1, 1, 1)); print(x)
    x = easy_unpack((6, 3, 7)); print(x)

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == 4.625
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == 5.5
    assert easy_unpack((1, 1, 1, 1)) == 1.0
    assert easy_unpack((6, 3, 7)) == 5.333333333333333
    print('Done! Go Check!')
