import mysql.connector 



#   FUNÇÃO PARA CONECTAR COM O MYSQL
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="gestao_clientes"
        )
        print("Conexão realizada com sucesso!")
        return conexao
    except mysql.MySQLError as e:
        print("erro:", e)
        return None


#   FUNÇÃO PARA CADASTRAR NOVO CLIENTE NO BD
def cadastrar_cliente(conexao, nome, idade, cpf, email, endereco, localidade, data_nasc, status):
   try:
        #   TRANSFORMA A ENTRADA DO PARAMETRO STATUS, QUE ESTÁ EM STRING, PARA O FORMATO BOOLEAN, QUE É O ACEITO NA TABELA DO MYSQL
        if status == "ativo":
            status = True
            statusnovo = status
        elif status == "inativo":
            status = False
            statusnovo = status
        else:
            print("Entrada inválida")

        cursor = conexao.cursor()
        query = "INSERT INTO clientes(nome, idade, cpf, email, endereco, localidade, data_nascimento, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (nome, idade, cpf, email, endereco, localidade, data_nasc, statusnovo)
        cursor.execute(query, dados)
        conexao.commit()

   except mysql.connector.Error as e:
       print("Deu erro: ", e)

#   FUNÇÃO PARA CADASTRAR NUMERO(S) DE TELEFONE DE UM CLIENTE ANTES DE SAIR DA CHAMADA DA FUNÇÃO CADASTRAR_CLIENTE
def cadastrar_telefone1(conexao, cpf, tipo, numero):
    cursor = conexao.cursor()

    #   COMANDO PARA ADICIONAR O ID_CLIENTE NA TABELA
    initial = "INSERT INTO cliente_telefones(cliente_id) SELECT id FROM clientes WHERE cpf = %s"
    #   COMANDO PARA ADICIONAR O RESTO DAS INFORMAÇÕES NA TABELA
    second = "UPDATE cliente_telefones SET numero = %s, tipo = %s WHERE id = last_insert_id()"
    
    cursor.execute(initial, (cpf,))
    cursor.execute(second, (numero, tipo))
    conexao.commit()
    print("Cadastro realizado com sucesso!")
#   FUNÇÃO CADASTRAR NUMERO(S) APÓS SAIR DA CHAMADA DA FUNÇÃO CADASTRAR_CLIENTE
def cadastrar_tefefone2(conexao, cliente_id, tipo, numero):
    cursor = conexao.cursor()

    #   COMANDO PARA ADICIONAR O ID_CLIENTE NA TABELA
    initial = "INSERT INTO cliente_telefones(cliente_id) VALUES (%s)"
    #   COMANDO PARA ADICIONAR O RESTO DAS INFORMAÇÕES NA TABELA
    second = "UPDATE cliente_telefones SET numero = %s, tipo = %s WHERE id = last_insert_id()"

    cursor.execute(initial, (cliente_id,))
    cursor.execute(second, (numero, tipo))
    conexao.commit()
    print("Cadastro realizado com sucesso!")

def adicionar_cliente() :
    conexao = conectar()
    if conexao: 
        if input("Quer adicionar algum cliente (s/n)?") == "s":
            nome = input("Nome: ") 
            idade = input("Idade: ") 
            cpf = input("cpf:" )
            email = input("Email: ")
            endereco = input("endereço (Rua e Numero): ") 
            localidade = input("Localidade (Cidade/UF): ") 
            data_nasc = input("Data de Nascimento (ano/mês/dia): ")
            estado = input("Estado da Conta (ativo/inativo): ")

            cadastrar_cliente(conexao, nome, idade, cpf, email, endereco, localidade, data_nasc, estado)
            print("Cadastro realizado com sucesso!")

            if input("Deseja cadastrar um numero de telefone para esse cliente (s/n)?: ") == "s":
                i = "sim"
                while i == "sim":
                    cadastrar_telefone1(conexao, cpf, input("Telefone de qual tipo(Fixo, WhatsApp, Celular)?: "), input("Digite seu numero: ") )
                    i = input("Cadastrar outro numero(sim/não)?: ")
                print("Cadastro realizado com sucesso!")
                
                    
            else:
                print("Vlw!")
    
    