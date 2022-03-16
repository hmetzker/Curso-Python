import os

def geraArq(s1, s2, a1, a2):
    try:
        with open(arquivo1, 'w') as f:
            f.write(f'{s1}\n')
    except:
        print("Erro geraArq: arquivo1")

    try:
        with open(arquivo2, 'w') as g:
           g.write(f'{s2}\n')
    except:
        print("Erro geraArq: arquivo2")

def addArq(s1, s2, a1, a2):
    try:
        with open(arquivo1, 'a') as f:
            f.write(f'{s2}\n')
    except:
        print("Erro addArq: arquivo1")

    try:
        with open(arquivo2, 'a') as g:
            g.write(f'{s1}\n')
    except:
        print("Erro addArq: arquivo2")

def alteraArq(s1, s2, a1, a2):
    s3=s1.split()
    try:
        with open(arquivo1, 'r') as f:
            lida = f.read()
    except:
        print("Erro alteraArq: arquivo1")

    try:
        with open(arquivo2, 'a') as g:
            for i in range(len(s3)):
                g.write(f'{s3[i]}\n')

            g.write(s2)
    except:
        print("Erro alteraArq: arquivo2")

if __name__ == '__main__':
    string1='haroldo fátima bianca bruna'
    string2='HFBiBru'
    arquivo1='C:\\Users\\HFBiBru\\PycharmProjects\\Curso-Python\\hfbibru.txt'
    arquivo2='C:\\Users\\HFBiBru\\PycharmProjects\\Curso-Python\\2286.txt'
    geraArq(string1, string2, arquivo1, arquivo2)
    addArq(string1, string2, arquivo1, arquivo2)
    alteraArq(string1, string2, arquivo1, arquivo2)


