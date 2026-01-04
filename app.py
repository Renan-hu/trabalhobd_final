import mysql.connector
from datetime import date


#serve para iniciar a conexão entre o python e a tabela no mysql
conexao = mysql.connector.connect( 
    host= 'localhost' ,
    user= 'root' ,
    password= 'Math314159' , 
    database= 'new_schema'
)

cursor = conexao.cursor() #admnistra a conexão, que por sua vez é responsável por criar o cursor

# FUNÇÃO PARA QUE O USUÁRIO SELECIONE O CLIENTE DESEJADO 

def selecionar_cliente(conexao):
    cursor = conexao.cursor()

    # LOOP PARA CONTROLAR A ESCOLHA DE AÇÕES DO USUÁRIO
    while True:  

        try:
            cliente_id = int(input("\nDigite o ID do cliente: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            continue #pergunta novamente por um ID válido
        comando = 'SELECT idclientes, nome, cpf FROM clientes WHERE idclientes = %s'
        cursor.execute(comando, (cliente_id,))
        cliente = cursor.fetchone()
        
        
        if not cliente:
            print("Este cliente não existe. Digite o ID de um cliente existente.")
            continue #pergunta um ID novamente
        print(f"\nCliente selecionado:  {cliente[1]} | CPF: {cliente[2]}")
        return cliente_id


# FUNÇÃO PARA CONFIRMAR A EXCLUSÃO DO CLIENTE
def confirmar_exclusao():
    while True:
        resposta = input("\nVocê tem certeza que deseja excluir este cliente? (s/n): ").lower()

        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Resposta inválida. Digite 's ou 'n'.") 


def deletar_cliente(conexao, cliente_id):
    cursor = conexao.cursor()

    try:

    # DELETA O TELEFONE DO CLIENTE
        acao = 'DELETE FROM cliente_telefones WHERE cliente_id = %s'
        cursor.execute(acao, (cliente_id,))
    # DELETA O CLIENTE
        acao_dois = 'DELETE FROM clientes WHERE idclientes = %s'
        cursor.execute(acao_dois, (cliente_id,))
        conexao.commit()
        print("Cliente excluído com sucesso")

    except Exception as erro:
        conexao.rollback()
        print("Erro ao excluir o cliente: ", erro)

    finally: 
        cursor.close()

# FLUXO PRINCIPAL QUE CONTROLA A SEQUÊNCIA DE EXECUÇÃO

cliente_id = selecionar_cliente(conexao)

if confirmar_exclusao():
    deletar_cliente(conexao, cliente_id)
else:
    print("Exclusão cancelada pelo usuário.")


conexao.close()