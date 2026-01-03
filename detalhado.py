import pymysql

#   FUNÇÃO PARA CONECTAR COM O MYSQL
def conectar():
    try:
        conexao = pymysql.connect(
            host="localhost",
            user="root",
            password="54321",
            database="teste"
        )
        return conexao
    except pymysql.MySQLError as e:
        print("Erro:", e)
        return None
 

#FUNÇÃO PARA ECIXIBIR OS TELEFONES
def AUXtelefones(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT cliente_telefone.numero FROM cliente_telefone WHERE cliente_id = %s', (id,))
        result = cursor.fetchall()
        for i in result:
            print(f"Telefone(s) associado(s): {i[0]}")
        return
    except:
        print("error AUX")





#FUNÇÃO PARA EXIBIR DETALHES DO CLIENTE
def detalhes (): 
    try: 
        conexao = conectar()
        cursor = conexao.cursor()

        id = input("Digite o id do cliente que você quer buscar mais informações: ")
        cursor.execute('SELECT * FROM cliente WHERE id= %s', (id, ))
        resultado = cursor.fetchone() 
        if resultado:
            print ("-----INFORMAÇÕES DETALHADAS-----")
            
            #PRINTA O NOME DA COLUNA E O VALOR ARMAZENADO NA VARIAVEL RESULTADO "RESULTADO".
            for col, val in zip(cursor.description, resultado):
                print(f"{col[0]}: {val}")
            
            AUXtelefones(id)
            
            #PERGUNTA SE QUER REALIZAR UMA NOVA CONSULTA
            retry = input("Deseja realizar outra consulta ? s/n: ")
            if retry == "s":
                return detalhes()
            elif retry == "n": 
                print("vlw!")
        else:
            print("Cliente não cadastrado")
            retry = input("Deseja realizar outra consulta ? s/n: ")
            if retry == "s":
                return detalhes()
            elif retry == "n": 
                print("vlw!")

        
        cursor.close()
        conexao.close()
    
    except:
        print ("erro função detalhes")


detalhes()



