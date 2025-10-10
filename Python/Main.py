

menu_principal()

def menu_principal():
    while True:
        print("\nSistema de Controle de Estoque")
        print("1. Relatórios")
        print("2. Inserir Registros")
        print("3. Remover Registros")
        print("4. Atualizar Registros")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorios()
        elif opcao == "2":
            inserir_registro()
        elif opcao == "3":
            remover_registro()
        elif opcao == "4":
            atualizar_registro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

def relatorios():
    print("\nRelatórios")
    print("1. Sumarização de Estoque")
    print("2. Relatório de Movimentações por Produto")

    opcao = input("Escolha um relatório: ")

    if opcao == "1":
        # Realizar o relatório de sumarização de estoque
        pass
    elif opcao == "2":
        # Realizar o relatório de movimentações por produto
        pass

def inserir_registro():
    # Inserir produto ou movimentação
    pass

def remover_registro():
    # Remover produto ou movimentação
    pass

def atualizar_registro():
    # Atualizar produto ou movimentação
    pass

