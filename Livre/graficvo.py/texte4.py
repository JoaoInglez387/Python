import tkinter as tk
from tkinter import messagebox

tarefas = []

def adicionar_tarefa():
    titulo = titulo_entry.get()
    descricao = descricao_entry.get()
    if titulo and descricao:
        tarefa = {"titulo": titulo, "descricao": descricao, "status": "Pendente"}
        tarefas.append(tarefa)
        listar_tarefas()
    else:
        messagebox.showerror("Erro", "Título e descrição são obrigatórios!")

def listar_tarefas():
    tarefas_listbox.delete(0, tk.END)
    for tarefa in tarefas:
        tarefas_listbox.insert(tk.END, f"{tarefa['titulo']} - {tarefa['status']}")

def visualizar_tarefa():
    index = tarefas_listbox.curselection()[0]
    tarefa = tarefas[index]
    messagebox.showinfo(tarefa['titulo'], f"Descrição: {tarefa['descricao']}\nStatus: {tarefa['status']}")

def marcar_concluida():
    index = tarefas_listbox.curselection()[0]
    tarefas[index]['status'] = "Concluída"
    listar_tarefas()

def marcar_pendente():
    index = tarefas_listbox.curselection()[0]
    tarefas[index]['status'] = "Pendente"
    listar_tarefas()

root = tk.Tk()

titulo_label = tk.Label(root, text="numero")
titulo_label.pack()
titulo_entry = tk.Entry(root)
titulo_entry.pack()

descricao_label = tk.Label(root, text="Descrição")
descricao_label.pack()
descricao_entry = tk.Entry(root)
descricao_entry.pack()

adicionar_button = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
adicionar_button.pack()

tarefas_listbox = tk.Listbox(root)
tarefas_listbox.pack()

visualizar_button = tk.Button(root, text="Visualizar Tarefa", command=visualizar_tarefa)
visualizar_button.pack()

concluida_button = tk.Button(root, text="Marcar como Concluída", command=marcar_concluida)
concluida_button.pack()

pendente_button = tk.Button(root, text="Marcar como Pendente", command=marcar_pendente)
pendente_button.pack()

root.mainloop()