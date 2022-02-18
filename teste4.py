# String na coluna 70

def print_hi(name, linha70):
    linha70 = (" "*(10-len(name)) + name)
    return linha70

if __name__ == '__main__':
    result = print_hi("Haroldo", "")
    print(len(result),result)

