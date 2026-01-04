import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Fer01100892*",
        database = "db_bonneti"
    )

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
        return None 
    elif cliente:
        messagebox.showinfo(
        "Cliente",
        f"ID: {cliente[0]}\nNome: {cliente[1]}\nCPF: {cliente[2]}\nEmail: {cliente[3]}"
    )

def deleta_cliente():
    cliente = cliente_selecionado()
    if not cliente:
        messagebox.showwarning("Por favor, selecione algum cliente antes de prosseguir ")
        return 

    if messagebox.askyesno("Confirmar", "Deseja realmente deletar este cliente?"):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente[0],))
        conexao.commit()
        cursor.close()
        conexao.close()
        listar_clientes()

def editar_clientes():
    cliente = cliente_selecionado()
    if not cliente:
        messagebox.showwarning("Por favor, selecione algum cliente antes de prosseguir")
        return 

    janela_editar = tk.Toplevel(janela)
    janela_editar.title("Edição")
    janela_editar.geometry("300x200")
    
    
    entrada_nome = tk.Entry(janela_editar)
    entrada_nome.pack()
    entrada_nome.insert(0, cliente[1])

    entrada_email = tk.Entry(janela_editar)
    entrada_email.pack()
    entrada_email.insert(0, cliente[3])

    def salvar():
        a_nome = entrada_nome.get()
        a_email = entrada_email.get()
    
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("UPDATE clientes SET nome =%s, email = %s WHERE id = %s", (a_nome, a_email, cliente[0]))
    
        conexao.commit()
        cursor.close()
        conexao.close()

        listar_clientes()
        janela_editar.destroy()
        messagebox.showinfo("Sucesso", "Cliente alterado com sucesso")
    tk.Button(janela_editar, text="Salvar", command = salvar).pack(pady = 10) 

frame_butoes = tk.Frame(janela)
frame_butoes.pack(pady = 5)

botao_Vizualizar = tk.Button( frame_butoes, text="vizualizar cliente", command= visualizar_cliente).pack(side = "left",padx = 5)
botao_editar = tk.Button(frame_butoes, text="Editar", command = editar_clientes).pack(side = "left", padx = 5)
botao_deletar = tk.Button(frame_butoes, text= "Deletar", command = deleta_cliente).pack(side = "left", padx = 5)

listar_clientes()
janela.mainloop()