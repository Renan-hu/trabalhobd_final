
from colorama import Fore # PARA CONSEGUIR USAR ESSA BIBLIOTECA, USE "pip install colorama" NO TERMINAL
import gestao
import listar
import detalhado
import deletar

continuar = "s"

# INTERFACE QUE VAI APARECER AO FINAL DE CADA FUNCIONALIDADE
def interface_continuar ():
     continuar = "s"
     while continuar == "s" or (continuar != "s" and continuar != "n") :
          print("")
          continuar = input (Fore.YELLOW + "Deseja efetuar mais algum processo no sistema? (s/n) " + Fore.WHITE) 
               
          if continuar != "n" and continuar != "s" :
               print(Fore.RED + "Resposta inválida, tente novamente." + Fore.WHITE)
          
          elif continuar == "n" :
               break 

          else :
               opcao = input ("1. Listar clientes \n2. Detalhar dados do cliente \n3. Adicionar dados de clientes \n4. Deletar dados de clientes \nQual opção você escolhe?")
               print("")
               if opcao == "1":
                    listar.listar_func()
               elif opcao == "2":
                    detalhado.detalhar()
               elif opcao == "3" :
                    gestao.adicionar_cliente()
               elif opcao == "4":
                    deletar.delete()
               else :
                    print(Fore.RED + "Opção inválida. Tente novamente" + Fore.WHITE)


     
     print(Fore.GREEN + "Obrigado por usar nosso sistema!" + Fore.WHITE)

# INTERFACE INICIAL DO CÓDIGO

def interface_inicial() :
     interface = input(f"Olá! Seja bem vindo ao sistema de gerenciamento de banco de dados. \nO sistema tem 4 opções, escolha uma delas: \n1. Listar clientes \n2. Detalhar dados de cliente \n3. Adicionar dados de clientes \n4. Deletar dados de clientes {Fore.YELLOW}\nQual opção você escolhe?{Fore.WHITE} ")
     print("")
     if interface == "1":
          listar.listar_func()

     elif interface == "2":
          detalhado.detalhar()


     elif interface == "3" :
          gestao.adicionar_cliente()

     elif interface == "4":
          deletar.delete()
     else:
          print(Fore.RED + "Resposta inválida. Tente novamente: " + Fore.WHITE)
          interface_inicial()
     
    
interface_inicial() 
interface_continuar()
