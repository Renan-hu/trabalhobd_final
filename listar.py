import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user ='root',
    password ="Fer01100892*", 
    database ="db_bonneti",
)

cursor = conexao.cursor()







cursor.close()
conexao.close()