# backward string

def backward_string(name):
    b = list()
    for i in name:
        b.append(i)

#    print(b)

    c = list()
    for i in range(len(b)):
        c.append(b.pop())

#    print(c)
    return ''.join(c)

if __name__ == '__main__':
    print("Example:")
    result = input()
    print(backward_string(result))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")