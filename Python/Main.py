import sys
import os

# Adiciona a pasta raiz do projeto ao path, para poder executar de dentro da pasta Python do projeto, sem mexer nos imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Python.utils import menu
from Python.utils.splash_screen import splashScreen
from Python.reports.relatorios import Relatorio
from Python.controller.Produtos_Controller import ProdutosController
from Python.controller.Pedidos_Controller import PedidosController
from Python.connection.database import DatabaseConnection as db

tela_inicial = splashScreen()
relatorio = Relatorio()
ctrl_produto = ProdutosController()
ctrl_pedido = PedidosController()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_produtos()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_pedidos()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_estoque_baixo()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_produtos_por_pedido()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:
        oracle=db()
        ctrl_produto.inserir_produto(oracle)
    elif opcao_inserir == 2:
        oracle=db()
        ctrl_pedido.inserir_pedido(oracle)

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_produtos()
        oracle=db()
        ctrl_produto.atualizar_produto(oracle)

    elif opcao_atualizar == 2:
        relatorio.get_relatorio_pedidos()
        oracle=db()
        ctrl_pedido.atualizar_pedido(oracle)

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_produtos()
        oracle=db()
        ctrl_produto.excluir_produto(oracle)
    elif opcao_excluir == 2:
        relatorio.get_relatorio_pedidos()
        oracle=db()
        ctrl_pedido.excluir_pedido(oracle)

def run():
    print(tela_inicial.get_updated_screen())
    menu.clear_console()

    while True:
        try:
            print(menu.MENU_PRINCIPAL)
            opcao = int(input("Escolha uma opção [1-5]: "))
            menu.clear_console(1)

            if opcao == 1: # Relatórios

                print(menu.MENU_RELATORIOS)
                opcao_relatorio = int(input("Escolha uma opção [0-4]: "))
                menu.clear_console(1)

                reports(opcao_relatorio)

                menu.clear_console(1)

            elif opcao == 2: # Inserir Novos Registros

                print(menu.MENU_ENTIDADES)
                opcao_inserir = int(input("Escolha uma opção [1-2]: "))
                menu.clear_console(1)

                inserir(opcao_inserir=opcao_inserir)

                menu.clear_console()
                print(tela_inicial.get_updated_screen())
                menu.clear_console()

            elif opcao == 3: # Atualizar Registros

                print(menu.MENU_ENTIDADES)
                opcao_atualizar = int(input("Escolha uma opção [1-2]: "))
                menu.clear_console(1)

                atualizar(opcao_atualizar=opcao_atualizar)

                menu.clear_console()

            elif opcao == 4:

                print(menu.MENU_ENTIDADES)
                opcao_excluir = int(input("Escolha uma opção [1-2]: "))
                menu.clear_console(1)

                excluir(opcao_excluir=opcao_excluir)

                menu.clear_console()
                print(tela_inicial.get_updated_screen())
                menu.clear_console()

            elif opcao == 5:

                print(tela_inicial.get_updated_screen())
                menu.clear_console()
                print("Obrigado por utilizar o sistema.")
                exit(0)

            else:
                print("Opção incorreta.")
                exit(1)
        except Exception:
            print(f"Opção incorreta.")
            exit(2)
if __name__ == "__main__":
    run()