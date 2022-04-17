from tkinter import *

root = Tk()
root.title('Login')

# definir geometry
largura = 300
altura = 110
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = (largura_screen - largura) / 2
posy = (altura_screen - altura) / 2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

# Labels, grid manager
label_usuario = Label(root, text='Usuário:', padx=20, pady=20).grid(row=0, stick=W)
label_senha = Label(root, text='Senha:', padx=20).grid(row=1, stick=W)
label_nada = Label(root, text='     ').grid(row=1, column=2)
text_usuario = Entry(root).grid(row=0, column=1)
text_senha = Entry(root).grid(row=1, column=1)
cmd_Login = Button(root, text='Login').grid(row=1, column=3)

root.mainloop()