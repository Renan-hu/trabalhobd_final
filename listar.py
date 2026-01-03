import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "gestao_clientes"
    )
def listar_func () :
    janela = tk.Tk()
    janela.title("Listar Clientes")
    janela.geometry("800x400")

    colunas = ("id", "nome", "cpf", "email")

    tabela = ttk.Treeview(janela, columns = colunas, show= "headings")
    tabela.heading("id", text = "ID")
    tabela.heading("nome", text="nome")
    tabela.heading("cpf", text="cpf")
    tabela.heading("email", text= "email")

    tabela.column("id", width=50, anchor = "center")
    tabela.column("nome", width = 200)
    tabela.column("cpf", width=150)
    tabela.column("email", width=250)

    tabela.pack(expand = True, fill = "both", pady = 10)


    def listar_clientes():
        tabela.delete(*tabela.get_children())
            
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT ID, nome, cpf, email FROM clientes")

        for linha in cursor.fetchall():
            tabela.insert("", tk.END, values = linha)
            
        cursor.close()
        conexao.close()

    def cliente_selecionado():
        item = tabela.focus()
        if not item:
            return None
        return tabela.item(item)["values"]
        
    def visualizar_cliente():
        cliente = cliente_selecionado()
        if not cliente:
            messagebox.showwarning("Aviso","Selecione um cliente")
            return messagebox.showinfo(
            "Cliente",
            f"ID: {cliente[0]}\nNome: {cliente[1]}\nCPF: {cliente[2]}\nEmail: {cliente[3]}"
        )


    listar_clientes()
    janela.mainloop()