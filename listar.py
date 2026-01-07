import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


#----------------- FUNCAO PARA CONECTAR -----------------
def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Fer01100892*",
        database = "db_bonneti"
    )

#----------------- criar o basico da interface -----------------
janela = tk.Tk()# comando pra criar a janela
janela.title("Listar Clientes")
janela.geometry("800x400")




#----------------- Cria as colunas na janela -----------------
colunas = ("id", "nome", "cpf", "email") #var que guarda esses valores que estao relacioandos indiretamente com o mysql

tabela = ttk.Treeview(janela, columns = colunas, show= "headings")#cria as colunas e pede só pra mostras os titulos
tabela.heading("id", text = "ID") #relaciona cada coluna com os valores do array
tabela.heading("nome", text="nome")
tabela.heading("cpf", text="cpf")
tabela.heading("email", text= "email")

tabela.column("id", width=50, anchor = "center") # me so no tamanho das colunas
tabela.column("nome", width = 200)
tabela.column("cpf", width=150)
tabela.column("email", width=250)

tabela.pack(expand = True, fill = "both", pady = 10)# bota a tabela na tela  

#----------------- Função para mostrar os valores do MySql pra interface -----------------
def listar_clientes():
    tabela.delete(*tabela.get_children())
        
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT clientes.id, clientes.nome, clientes.cpf, clientes.email, "
        "clientes.endereco, clientes.localidade, clientes.data_nasc, clientes.status, "
        "GROUP_CONCAT(tabela_telefones.numero SEPARATOR ', ') AS telefones "
        "FROM clientes "
        "LEFT JOIN tabela_telefones ON clientes.id = tabela_telefones.cliente_id "
        "GROUP BY clientes.id, clientes.nome, clientes.cpf, clientes.email, "
        "clientes.endereco, clientes.localidade, clientes.data_nasc, clientes.status"
        )
    for linha in cursor.fetchall():
        tabela.insert("", tk.END, values = linha) 
        
    cursor.close()
    conexao.close()
#----------------- Função que da a opção de selecionar o cliente-----------------
def cliente_selecionado():
    item = tabela.focus()# cria uma variavel linha que armazena (.focus()) tudo relacionado a linha selecionada
    if not item:
        return None
    else:
        return tabela.item(item)["values"]#caso a linha tenha sido selecionada ele vai retornar tudo que foi armazenado na linha e o ["values"] vai querer que retorne apenas o valores que foram salvos

#----------------- Função de vizualizar cliente -----------------
def visualizar_cliente():

    cliente = cliente_selecionado() #cria uma var que tem o valor da func escolhida
    if not cliente: #caso o cliente não tenha sido selecionado ele retorna um box que pede pra ele selecionar algo 
        messagebox.showwarning("Aviso","Selecione um cliente") 
        return None 
    elif cliente: #Caso tenha sido escolhido ele abre uma mini tela que mostra os detalhes 
        messagebox.showinfo(
        "Cliente",#isso aqui é o titulo da caixa
        f"ID: {cliente[0]}\nNome: {cliente[1]}\nCPF: {cliente[2]}\nEmail: {cliente[3]}\nendereço: {cliente[4]}\nlocalidade: {cliente[5]}\nData de nascimento: {cliente[6]}\nstatus: {cliente[7]}\nTelefones: {cliente[8]}"#isso é o resto das info
    )

#----------------- Função que deleta o bixos -----------------
def deleta_cliente():
    cliente = cliente_selecionado()# mesma logica do vizualizar clientes
    if not cliente:
        messagebox.showwarning("Aviso", "Selecione um cliente para processeguir")# mesma logica do vizualizar clientes
        return 


    if messagebox.askyesno("Confirmar", "Deseja realmente deletar este cliente?"): #abre uma box que tem as opção sim ou n (.aksyesno)
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("DELETE FROM tabela_telefones WHERE cliente_id = %s", (cliente[0],))
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente[0],))
        conexao.commit()
        cursor.close()
        conexao.close()
        #faz todo o crud de delete 
        listar_clientes()#reseta a telinha

def editar_clientes():
    cliente = cliente_selecionado()
    if not cliente:
        messagebox.showwarning("Aviso", "Selecione um cliente antes de prosseguir")# mesma logica do vizualizar_clientes()
        return 
    #----- cria uma janelinha que sobrepoe a janela principal -----
    janela_editar = tk.Toplevel(janela) #a func toplevel faz isso ai
    janela_editar.title("Edição")
    janela_editar.geometry("300x200")
    
    
    entrada_nome = tk.Entry(janela_editar)# faz como se fosse uma caixa de input
    entrada_nome.pack()#posiciona automaticamente na tela
    entrada_nome.insert(0, cliente[1]) # serve pra aparecer o bixo dentro da caixa de input, pro caba nao se confudir 

    entrada_email = tk.Entry(janela_editar)# mesma logica do outro so que pro email
    entrada_email.pack()
    entrada_email.insert(0, cliente[3])

    
    def salvar():
        a_nome = entrada_nome.get() #recebe os valores da funcão editar_clientes
        a_email = entrada_email.get()
    
        conexao = conectar()
        cursor = conexao.cursor() #crudzao 

        cursor.execute("UPDATE clientes SET nome =%s, email = %s WHERE id = %s", (a_nome, a_email, cliente[0]))#Faz o comando SQL, que mete o updatezao pro valor que foi mudado no input
    
        conexao.commit()
        cursor.close()
        conexao.close()#crudzão cruel

        listar_clientes()#atualiza o layout da janela
        janela_editar.destroy()# tira a telinha do input
        messagebox.showinfo("Sucesso", "Cliente alterado com sucesso")# ai no final ele so fala que ta deu bom
    tk.Button(janela_editar, text="Salvar", command = salvar).pack(pady = 10) #cria o butão que salva(sem muitos comentatios)

#-Ignora-
# def adicionar_clientes():
#     janela_add = tk.Toplevel(janela)
#     janela_add.pack()
#     janela_add.geometry("500x400")

#     add_nome = tk.Entry(janela_add).pack()
#     add_cpf = tk.Entry(janela_add).pack()
#     add_email = tk.Entry(janela_add)


#----------------- Butao -----------------
#tem a mesma logica do frame da apple
frame_butoes = tk.Frame(janela)
frame_butoes.pack(pady = 5) # ajusta a posição Y do frame

#cria os butão (Acho que não tem muito oq falar)
botao_Vizualizar = tk.Button( frame_butoes, text="vizualizar cliente", command= visualizar_cliente).pack(side = "left",padx = 5)#.pack() serve pra ajustar ele no frame
botao_editar = tk.Button(frame_butoes, text="Editar", command = editar_clientes).pack(side = "left", padx = 5)
botao_deletar = tk.Button(frame_butoes, text= "Deletar", command = deleta_cliente).pack(side = "left", padx = 5)

listar_clientes() #reseta a tabela
janela.mainloop() #faz funcionar toda interface do tk