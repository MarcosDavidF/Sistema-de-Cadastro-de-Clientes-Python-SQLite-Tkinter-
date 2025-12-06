# aplicacao.py
from cadastro import Gui
import backend as core
from tkinter import END

app = None
selected = None  # variável global que armazenará a tupla selecionada

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    global selected
    if not selected:
        return
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    global selected
    if not selected:
        return
    core.delete(selected[0])
    selected = None
    view_command()

def getSelectedRow(event):
    global selected
    try:
        index = app.listClientes.curselection()[0]
    except IndexError:
        return
    selected = app.listClientes.get(index)
    # selected é a tupla (id, nome, sobrenome, email, cpf)
    # Preencher os campos de texto com os valores
    app.txtNome.set(selected[1])
    app.txtSobrenome.set(selected[2])
    app.txtEmail.set(selected[3])
    app.txtCPF.set(selected[4])
    return selected

if __name__ == '__main__':
    app = Gui()
    # liga os eventos/ações
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    app.btnViewALL.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)

    # mostra todos ao iniciar
    view_command()
    app.run()
