# usando uma função como argumento

def duasVezes(x, y):
    print(x)
    print(y)

def pr_spam(z):
    print(z)

if __name__ == '__main__':
    duasVezes(pr_spam('Haroldo'), 111)
