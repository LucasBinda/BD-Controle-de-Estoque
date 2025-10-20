from contextlib import nullcontext

#from Python.controller.Pedidos_Controller import PedidosController
from Python.connection.database import DatabaseConnection


    #   validação de existencia na tabela (existir ou não) retyrn o caso
    #   inserção    Not existir     | uso de sequence: exbegin
    #                           :codigo := ITENS_PEDIDO_CODIGO_ITEM_SEQ.NEXTVAL;
    #                           insert into itens_pedido values(:codigo, :quantidade, :valor_unitario, :codigo_pedido, :codigo_produto);
    #                            end;
    #   Atualização existir
    #   exclusão    existir
    #   listar produtos
    #


class ProdutosController :
    def __init__(self):
        pass


    def verifica_produto_id(self, db: DatabaseConnection, id_produto: int) -> bool:  # Verifica se o produto já existe pelo ID
        try:
            df = db.sqlToDataFrame(
                f"SELECT id_produto FROM produtos WHERE id_produto = {id_produto}"
            )
            return not df.empty  # True se existe, False se não
        except Exception as e:
            print(f"Erro ao verificar existência do produto: {e}")
            return False

    def verifica_produto_nome(self, db: DatabaseConnection, nome_produto: str) -> bool: # Verifica se o produto já existe pelo nome

        try:
            if not nome_produto: # se for nulo
                return False

            # Padroniza e escapa aspas simples para evitar sql injection
            nome_produto_limpo = nome_produto.strip().lower().replace("'", "''")

            # Monta query concatenando o valor escapado
            query = f"SELECT id_produto FROM produtos WHERE LOWER(nome_produto) = '{nome_produto_limpo}'"

            df = db.sqlToDataFrame(query)

            return not df.empty  # True se existe, False se não
        except Exception as e:
            print(f"Erro ao verificar existência do produto pelo nome: {e}")
            return False

    def inserir_produto(self, db: DatabaseConnection) -> bool:  #recebe um objeto produto, verifica se exista e da return
        try:
            from Python.model.Produtos import Produto

            nome = str(input("Nome do produto que deseja inserir: "))
            descricao = str(input("Descrição do produto que deseja inserir: "))
            preco = float(input("Preço do produto que deseja inserir: "))
            estoque = int(input("Estoque atual do produto que deseja inserir: "))

            #cria objeto produto para manipulação de valor interno usando metodos
            novo_produto = Produto(
                nome_produto=nome,
                descricao=descricao,
                preco=preco,
                estoque_atual=estoque
            )

            # Padroniza o nome: remove espaços e deixa tudo em minúsculas
            nome_produto_limpo = novo_produto.get_nome_produto().strip().lower() if novo_produto.get_nome_produto() else None


            if not nome_produto_limpo:
                print("Erro: nome do produto vazio ou inválido.")
                return False

            # Verifica se já existe produto com o mesmo nome
            if self.verifica_produto_nome(db, nome_produto_limpo):
                print(f"Produto '{nome_produto_limpo}' já existe no banco de dados.")
                return False


            query = """
                INSERT INTO produtos 
                (id_produto, nome_produto, descricao, preco, estoque_atual)
                VALUES (
                    PRODUTOS_ID_PRODUTO_SEQ.NEXTVAL,
                    :nome_produto,
                    :descricao,
                    :preco,
                    :estoque_atual
                )
            """

            dados_produto = {
                "nome_produto": nome_produto_limpo,
                "descricao": novo_produto.get_descricao().strip() if novo_produto.get_descricao() else None,
                "preco": novo_produto.get_preco(),
                "estoque_atual": novo_produto.get_estoque_atual()
            }

            cur = db.conectar()
            #executa o insert com os parametros da query
            cur.execute(query, dados_produto)
            #confirma insert
            cur.connection.commit()
            #fecha cursor
            cur.close()
            print(f"Produto '{nome_produto_limpo}' inserido com sucesso!")
            return True

        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            return False


    def atualizar_produto(self, db:DatabaseConnection) :
        try:
            from Python.model.Produtos import Produto

            # Recebe o identificador do produto (ID ou nome)
            id_input = input("Informe o ID do produto que deseja atualizar: ").strip()
            if id_input is None:
                return False

            if not id_input.isdigit():
                print("ID inválido.")
                return False

            id_produto = int(id_input)

            # Verifica se o produto existe
            query_check = f"SELECT * FROM produtos WHERE id_produto = {id_produto}"
            df = db.sqlToDataFrame(query_check)
            if df.empty:
                print(f"Produto com ID {id_produto} não encontrado.")
                return False

            # Mostra os dados atuais
            print("Dados atuais do produto:")
            print(df)

            # Recebe novos dados do usuário (enter mantém valor atual)
            novo_nome = input("Novo nome do produto (pressione Enter para manter atual): ").strip()
            nova_descricao = input("Nova descrição do produto (pressione Enter para manter atual): ").strip()
            novo_preco = input("Novo preço do produto (pressione Enter para manter atual): ").strip()
            novo_estoque = input("Novo estoque do produto (pressione Enter para manter atual): ").strip()

            # Cria dicionário com valores atualizados
            valores = {}
            if novo_nome:
                valores['nome_produto'] = novo_nome.strip().lower().replace("'", "''")
            if nova_descricao:
                valores['descricao'] = nova_descricao.strip().replace("'", "''")
            if novo_preco:
                valores['preco'] = float(novo_preco)
            if novo_estoque:
                valores['estoque_atual'] = int(novo_estoque)

            if not valores:
                print("Nenhum dado novo informado. Operação cancelada.")
                return False

            # monta query UPDATE dinamicamente
            set_clause = ", ".join([f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {v}" for k, v in valores.items()])
            query_update = f"UPDATE produtos SET {set_clause} WHERE id_produto = {id_produto}"

            # executa atualizacao
            cur = db.conectar()
            cur.execute(query_update)
            cur.connection.commit()
            cur.close()

            print(f"Produto com ID {id_produto} atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            return False


    def excluir_produto(self, db: DatabaseConnection):
            try:

                id_produto = int(input("Digite o ID do produto que deseja excluir: "))
                oracle=db.conectar()
                self.verifica_produto_id(db,id_produto)
                query_select = "SELECT nome_produto FROM produtos WHERE id_produto = :id"  # verifica se o produto existe
                oracle.execute(query_select, {"id": id_produto})
                resultado = oracle.fetchone()

                if not resultado:
                    print(f"\nNenhum produto encontrado com o ID {id_produto}.")
                    return

                nome_produto = resultado[0]

                print(f"\nProduto encontrado: {nome_produto} (ID: {id_produto})")
                confirmar = input("Tem certeza que deseja excluir este produto? (S/N): ").strip().upper() # mostra o nome do produto e pede confirmação final

                if confirmar != "S":
                    print("\nExclusao cancelada pelo usuário.")
                    return

                query_check_pedidos = "SELECT COUNT(*) FROM pedidos WHERE id_produto = :id" # Verifica se há pedidos relacionados
                oracle.execute(query_check_pedidos, {"id": id_produto})
                qtd_pedidos = oracle.fetchone()[0]

                if qtd_pedidos > 0:
                    print(f"\nExistem {qtd_pedidos} pedidos vinculados a este produto.")
                    confirmar_pedidos = input("Deseja excluir também os pedidos relacionados? (S/N): ").strip().upper()

                    if confirmar_pedidos != "S":
                        print("\nExclusão cancelada.")
                        return

                    oracle.execute("DELETE FROM pedidos WHERE id_produto = :id", {"id": id_produto}) # exclui pedidos antes do produto FK
                    oracle.connection.commit()
                    print(f"\n{qtd_pedidos} pedido(s) relacionado(s) excluído(s) com sucesso.")

                    oracle.execute("DELETE FROM produtos WHERE id_produto = :id", {"id": id_produto}) # exclui o produto PK
                    oracle.connection.commit()

                    print(f"\nProduto '{nome_produto}' (ID: {id_produto}) excluído com sucesso!")

            except Exception as e:
                print(f"\nOcorreu um erro ao excluir o produto: {e}")



