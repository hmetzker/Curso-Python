from tkinter import *

def valores():
    vartexto.set(text_ano1.get())

root = Tk()
root.title('Titulo da app')
root.geometry('200x100')
vartexto=StringVar()
label_ano1 = Label(root, textvariable=vartexto)
text_ano1 = Entry(root)
button1 = Button(root, text='Executar', command=valores)
#button2 = Button(root, text='fim', command=root.quit)
label_ano1.grid()
text_ano1.grid()
button1.grid()
root.mainloop()