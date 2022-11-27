from tkinter import *
from tkinter import ttk
from controller import ControllerCadastro, ControllerLogin

root = Tk()

class Saida():
    def __init__(self):
        self.root = root

    def widget_saida(self): 
        self.frame2 = Frame(self.root, bd=4, bg='#4682B4')
        self.frame2.place(relx=0.04, rely=0.68, relheight=.3, relwidth=.9)

        # label saida
        self.lb_saida = Label(self.frame2, text='github joaoreider', bg='#4682B4', fg='#000000',
                                font=('verdana', 12, 'bold'))
        self.lb_saida.place(relx=.28, rely=0.02)

class Funcs(Saida):

    def variaveis(self):
        self.email = self.entry_email.get()
        self.senha = self.entry_senha.get()
    
    def limpa_tela(self):
        self.entry_email.delete(0, END)
        self.entry_senha.delete(0, END)
    
    def cadastrar(self):
        self.variaveis()

        resultado = ControllerCadastro.cadastrar('nomeExemplo', self.email, self.senha)

        if resultado == 3:
            self.lb_saida["text"] = 'Email muito grande'
            root.update_idletasks()
        elif resultado == 4:
            self.lb_saida["text"] = 'Senha muito curta'
            root.update_idletasks()
        elif resultado == 5:
            self.lb_saida["text"] = 'Email já cadastrado'
            root.update_idletasks()
        elif resultado == 6:
            self.lb_saida["text"] = 'Erro no sistema'
            root.update_idletasks()
        elif resultado == 1:
            self.lb_saida["text"] = 'Cadastro efetuado'
            root.update_idletasks()

        self.limpa_tela()
    
    def login(self):
        self.variaveis()

        resultado = ControllerLogin.login(self.email, self.senha)

        if not resultado:
            self.lb_saida["text"] = 'Email ou senha incorretos'
            root.update_idletasks()
        else:
            self.lb_saida["text"] = f'{resultado}'
            root.update_idletasks()

        self.limpa_tela()

class App(Funcs, Saida):

    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widget_saida()
        root.mainloop()

    def tela(self):
        self.root.title('Tela de login')
        self.root.configure(background='#4169E1')
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        self.root.maxsize(width=400, height=300)
        self.root.minsize(width=400, height=300)

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg='#4682B4',
                            highlightbackground='#B8860B', highlightthickness=2)
        self.frame1.place(relx=0.02, rely=0.02, relheight=.96, relwidth=.96)

    def widgets_frame1(self):
        
        # botão entrar
        self.bt_entrar = Button(self.frame1, text='Entrar', command=self.login, bd=3, bg='#4169E1', fg='white',
                                activebackground='#D2691E', activeforeground='white',
                                font=('verdana', 9, 'bold'))
        self.bt_entrar.place(relx=0.28, rely=0.45, relheight=.15, relwidth=.2)

        # botão cadastrar
        self.bt_cadastrar= Button(self.frame1, text='Cadastrar', command= self.cadastrar, bd=3, bg='#4169E1', fg='white',
                                activebackground='#D2691E', activeforeground='white',
                                font=('verdana', 9, 'bold'))
        self.bt_cadastrar.place(relx=0.5, rely=0.45, relheight=.15, relwidth=.23)

        
        
        # label e entrada email
        self.lb_email = Label(self.frame1, text='Email', bg='#F5DEB3', fg='#8B4513',
                             font=('verdana', 9, 'bold'))
        self.lb_email.place(relx=.44, rely=0.05)

        self.entry_email = Entry(self.frame1, bg='#DEB887', fg='#8B4513',
                                font=('verdana', 8, 'bold'))
        self.entry_email.place(relx=0.28, rely=0.14, relwidth=.45)


        # label e entrada senha
        self.lb_senha = Label(self.frame1, text='senha', bg='#F5DEB3', fg='#8B4513',
                               font=('verdana', 9, 'bold'))
        self.lb_senha.place(relx=.44, rely=0.23)

        self.entry_senha = Entry(self.frame1, bg='#DEB887', fg='#8B4513',
                                  font=('verdana', 8, 'bold'))
        self.entry_senha.place(relx=0.28, rely=0.32, relwidth=.45)


App()