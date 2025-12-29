import pymysql

def conectar():
    try:
        conexao = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="gestao_clientes"
        )
        print("Conexão realizada com sucesso!")
        return conexao
    except pymysql.MySQLError as e:
        print("erro:", e)
        return None

conexao = conectar()