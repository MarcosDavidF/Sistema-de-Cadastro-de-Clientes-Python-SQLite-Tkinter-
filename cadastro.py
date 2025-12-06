# cadastro.py
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, StringVar, END, N, S, E, W

class Gui:
    """Classe da Interface Gráfica"""
    def __init__(self):
 # Janela principal
        self.window = Tk()
        self.window.wm_title('PYSQL versão 2.0 - Cadastro de Usuários')

        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        # Variáveis (textvariable)
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels
        self.lblNome = Label(self.window, text='Nome')
        self.lblSobrenome = Label(self.window, text='Sobrenome')
        self.lblEmail = Label(self.window, text='Email')
        self.lblCPF = Label(self.window, text='CPF')

        # Entries
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        # Listbox + Scrollbar
        self.listClientes = Listbox(self.window, width=80, height=15)
        self.scrollClientes = Scrollbar(self.window)

        # Buttons (nomes esperados pelo app)
        self.btnViewALL = Button(self.window, text='Ver Todos')
        self.btnBuscar = Button(self.window, text='Buscar')
        self.btnInserir = Button(self.window, text='Inserir')
        self.btnUpdate = Button(self.window, text='Atualizar Selecionados')
        self.btnDel = Button(self.window, text='Deletar Selecionados')
        self.btnClose = Button(self.window, text='Fechar')

        # Posicionamento com grid
        self.lblNome.grid(row=0, column=0, padx=self.x_pad, pady=self.y_pad, sticky=E)
        self.entNome.grid(row=0, column=1, padx=self.x_pad, pady=self.y_pad, sticky=W)

        self.lblSobrenome.grid(row=1, column=0, padx=self.x_pad, pady=self.y_pad, sticky=E)
        self.entSobrenome.grid(row=1, column=1, padx=self.x_pad, pady=self.y_pad, sticky=W)

        self.lblEmail.grid(row=2, column=0, padx=self.x_pad, pady=self.y_pad, sticky=E)
        self.entEmail.grid(row=2, column=1, padx=self.x_pad, pady=self.y_pad, sticky=W)

        self.lblCPF.grid(row=3, column=0, padx=self.x_pad, pady=self.y_pad, sticky=E)
        self.entCPF.grid(row=3, column=1, padx=self.x_pad, pady=self.y_pad, sticky=W)

        self.listClientes.grid(row=0, column=2, rowspan=8, padx=self.x_pad, pady=self.y_pad, sticky=N+S+E+W)
        self.scrollClientes.grid(row=0, column=3, rowspan=8, sticky=N+S)

        self.btnViewALL.grid(row=8, column=0, columnspan=2, sticky=E+W, padx=self.x_pad, pady=self.y_pad)
        self.btnBuscar.grid(row=9, column=0, columnspan=2, sticky=E+W, padx=self.x_pad, pady=self.y_pad)
        self.btnInserir.grid(row=10, column=0, columnspan=2, sticky=E+W, padx=self.x_pad, pady=self.y_pad)
        self.btnUpdate.grid(row=11, column=0, columnspan=2, sticky=E+W, padx=self.x_pad, pady=self.y_pad)
        self.btnDel.grid(row=12, column=0, columnspan=2, sticky=E+W, padx=self.x_pad, pady=self.y_pad)
        self.btnClose.grid(row=13, column=0, columnspan=2, sticky=E+W, padx=self.x_pad, pady=self.y_pad)

        # Conectar scrollbar
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Ajustes visuais: torna botões esticáveis
        for child in self.window.winfo_children():
            try:
                widget_class = child.winfo_class()
            except Exception:
                widget_class = ""
            if widget_class == 'Button':
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif widget_class == 'Listbox':
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == 'Scrollbar':
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                # labels and entries
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        self.window.mainloop()
