import mysql.connector 
import gestao
import listar

continuar = "s"

# INTERFACE QUE VAI APARECER AO FINAL DE CADA FUNCIONALIDADE
def interface_continuar ():
     continuar = "s"
     while continuar == "s" or (continuar != "s" and continuar != "n") :
          continuar = input ("Deseja efetuar mais algum processo no sistema? (s/n) ") 
               
          if continuar != "n" and continuar != "s" :
               print("Resposta inválida, tente novamente.")
          
          elif continuar == "n" :
               break 

          else :
               opcao = input ("1. Listar clientes\n2. Adicionar dados de clientes \n3. Deletar dados de clientes \nQual opção você escolhe?")
               if opcao == "1":
                    listar.listar_func()
               elif opcao == "2" :
                    gestao.adicionar_cliente()
     
     print("Obrigado por usar nosso sistema!")

# INTERFACE INICIAL DO CÓDIGO

interface_inicial = input("Olá! Seja bem vindo ao sistema de gerenciamento de banco de dados. \nO sistema tem 3 opções, escolha uma delas: \n1. Listar clientes \n 2. Adicionar dados de clientes \n3. Deletar dados de clientes \nQual opção você escolhe?")
if interface_inicial == "1":
     listar.listar_func()

elif interface_inicial == "2" :
    gestao.adicionar_cliente()

interface_continuar()
