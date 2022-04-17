
from tkinter import *

def cmd_Click(mensagem):
    print(mensagem)

if __name__ == '__main__':

    menu_inicial = Tk()
    menu_inicial.title('Primeiro GUI')
    menu_inicial.resizable(width=True, height=True)
    menu_inicial.iconbitmap('images/pyd.ico')

# dimensões da janela
    largura = 600
    altura = 400

# resolução da janela
    largura_screen = menu_inicial.winfo_screenwidth()
    altura_screen = menu_inicial.winfo_screenheight()

# posição da janela
    posx = (largura_screen - largura) / 2
    posy = (altura_screen - altura) / 2

# definir geometry
#    menu_inicial.geometry('600x300+300+200')
    menu_inicial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

# diminuir e aumentar a janela
    menu_inicial.minsize(width=500, height=250)
    menu_inicial.maxsize(width=700, height=400)

# maximizar e minimizar a janela
    #    menu_inicial.state('zoomed')
    #    menu_inicial.state('iconic')

#   botões
    btn1 = Button(master=menu_inicial, text = 'Executar', command = lambda: cmd_Click('Nova mensagem'))
    btn2 = Button(master=menu_inicial, text = 'Clicar', command = lambda: print('OK'))

# Labels
    texto = StringVar()
    texto.set('Label 1\nOutro Label\nMais um Label')
    label1 = Label(
        master=menu_inicial,
#        text='Label 1\nOutro Label\nMais um Label',
        bg='#f2e6ff',
        fg='#ff0000',
        font='Times 20 bold italic',
        borderwidth=2,
        relief='solid',
        width=20,
        height=5,
        anchor=CENTER,
        padx=10,
        pady=10,
        justify=LEFT,
        textvariable=texto
    )
    label2 = Label(menu_inicial)
    label2['text'] = 'Label 2'
    label2['font'] = 'Arial 20'
    label2['bd'] = 1
    label2['relief'] = 'solid'
    label2['justify'] = CENTER
#    label2.pack()

# pack
#    label1.pack()
#    label2.pack()
# grid manager
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=1)

    for i in label2.keys():
        print(i, " : ", label2[i])

#    btn1.pack()
#    btn2.pack()
    btn1.grid(row=1, column=0)
    btn2.grid(row=2, column=1)

    menu_inicial.mainloop()
