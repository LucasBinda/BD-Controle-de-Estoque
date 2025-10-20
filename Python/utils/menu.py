MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Produtos
2 - Relatório de Pedidos
3 - Relatório de Estoque Baixo
4 - Relatório de produtos por pedido
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - PRODUTOS
2 - PEDIDOS
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time: int = 3):
    import os
    from time import sleep
    sleep(wait_time)
    # "nt" → Windows | outros → Linux/macOS
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")