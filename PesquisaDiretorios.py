import os

def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

if __name__ == '__main__':
    pasta='C:\\Users\\HFBiBru\\PycharmProjects\\Curso-Python\\'
    walk(pasta)

try:
    fin = open('C:\\Users\\HFBiBru\\PycharmProjects\\Curso-Python\\hfbibru.txt')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong.')
