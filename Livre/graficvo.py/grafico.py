from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def inserir():
    if variavel_id.get() == "" or variavel_nome.get() == "" or variavel_fone.get() == "":
        messagebox.showinfo(title="Erro", message="Digite todos os dados")
        return
    tv.insert("", "end", values=(variavel_id.get(),variavel_nome.get(), variavel_fone.get()))

    variavel_id.delete(0, END)
    variavel_nome.delete(0, END)
    variavel_fone.delete(0, END)
    variavel_id.focus()


def deletar():
    try:
        item_selecionado = tv.selection()[0]
        tv.delete(item_selecionado)
    except:
        messagebox.showinfo(
            title="ERRO!", message="Não é possivel apagar algo nao selecionado, selecione um elemento a ser deletado")
        return


def obter():
    try:
        item_selecionado = tv.selection()[0]
        valores = tv.item(item_selecionado, "values")
        print("ID......:" + valores[0])
        print("Nome....:" + valores[1])
        print("Telefone:" + valores[2])
    except:
        messagebox.showinfo(
            title="ERRO!", message="Não é possivel selecionado o elemento, selecione um elemento a ser mostrado")


aplicativo = Tk()
aplicativo.title("CFB Curso")
aplicativo.geometry("800x500")

# ----------------------------------------------------------------------------
quadro_organi = LabelFrame(aplicativo, text="Contatos")
quadro_organi.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(quadro_organi, columns=(
    'id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=100)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text='ID')
tv.heading('nome', text='Nome')
tv.heading('fone', text='Telefone')
tv.pack()

# -------------------------------------------------------------------------------
quadro_inserir = LabelFrame(aplicativo, text="Inserir Novos Contatos")
quadro_inserir.pack(fill="both", expand="yes", padx=10, pady=10)

# tv.insert("","end", values= ('10','Bruno','1234'))
# tv.insert("","end", values= (id,nome,fone))

bn_inserir = Button(quadro_inserir, text="Inserir", command=inserir)
bn_deletar = Button(quadro_inserir, text="Deletar", command=deletar)
bn_obter = Button(quadro_inserir, text="Obter", command=obter)

bn_inserir.grid(column=0, row=4)
bn_deletar.grid(column=1, row=4)
bn_obter.grid(column=2, row=4)

# ---------------------------------------------------------------------------------
quadro_escreve = LabelFrame(aplicativo, text="Escreva as variaveis")
quadro_escreve.pack(fill="both", expand="yes", padx=10, pady=10)

lbid = Label(quadro_escreve, text="ID")  # , anchor=W)
variavel_id = Entry(quadro_escreve)

lbnome = Label(quadro_escreve, text="Nome")  # , anchor=W)
variavel_nome = Entry(quadro_escreve)

lbfone = Label(quadro_escreve, text="Telefone")  # , anchor=W)
variavel_fone = Entry(quadro_escreve)


lbid.grid(column=0, row=0, sticky='w')
variavel_id.grid(column=0, row=1)

lbnome.grid(column=1, row=0, sticky='w')
variavel_nome.grid(column=1, row=1)

lbfone.grid(column=2, row=0, sticky='w')
variavel_fone.grid(column=2, row=1, sticky='w')

tv.grid(column=0, row=3, columnspan=3, pady=5)


aplicativo.mainloop()
