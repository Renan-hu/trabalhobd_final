import mysql.connector 
# ADENDO: ESTE CÓDIGO ESTÁ SENDO IMPLEMENTADO MESMO QUE SUA FUNÇÃO JÁ SEJA COMPRIDA EM
# "lISTAR.PY" POIS FOI ESCRITO POR UM DOS INTEGRANTES DA EQUIPE, ASSIM PARA QUE NÃO TENHA
# SIDO UM TRABALHO EM VÃO, ELE VEIO A VERSÃO FINAL.


def detalhar():
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


    #FUNÇÃO PARA ECIXIBIR OS TELEFONES
    def AUXtelefones(id):
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute('SELECT cliente_telefones.numero FROM cliente_telefones WHERE cliente_id = %s', (id,))
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
            cursor.execute('SELECT * FROM clientes WHERE id= %s', (id, ))
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
        
        except Exception as e:
            print (f"Deu erro {e}") 


    detalhes()