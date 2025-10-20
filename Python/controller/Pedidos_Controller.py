from Python.connection.database import DatabaseConnection





class PedidosController:
    def __init__(self):
        pass


    def verifica_pedido_id(self, db: DatabaseConnection, id_pedido: int) -> bool:
        try:
            query = "SELECT ID_PEDIDO FROM PEDIDOS WHERE ID_PEDIDO = :id_pedido"
            oracle=db.conectar()
            oracle.execute(query, {"id_pedido": id_pedido})
            return oracle.fetchone() is not None
        except Exception as e:
            print(f"Erro ao verificar existência do pedido: {e}")
            return False

    def inserir_pedido(self, db: DatabaseConnection) -> bool:
        try:
            from Python.reports.relatorios import Relatorio
            Relatorio().get_relatorio_produtos()


            id_produto = int(input("Digite o ID do produto: "))

            while True: # valida o tipo do tipo
                tipo = input("Digite o tipo do pedido (COMPRA/VENDA): ").strip().upper()
                if tipo in ["COMPRA", "VENDA"]:
                    break
                print("Tipo inválido! Digite 'COMPRA' ou 'VENDA'.")

            while True:
                try:
                    quantidade = int(input("Digite a quantidade: "))
                    if quantidade >= 0:
                        break
                    print("A quantidade deve ser maior que 0.")
                except ValueError:
                    print("Digite um número válido para a quantidade.")

            # Converter data para objeto date (Oracle aceita string no formato 'YYYY-MM-DD' também)
            from datetime import datetime
            data = datetime.now()


            # query usando SEQUENCE do oracle
            query = """ 
            BEGIN
                INSERT INTO PEDIDOS (ID_PEDIDO, ID_PRODUTO, DATA, TIPO, QUANTIDADE)
                VALUES (PEDIDOS_ID_PEDIDO_SEQ.NEXTVAL, :id_produto, :data, :tipo, :quantidade);
            END;
            """
            oracle=db.conectar()


            dados = { # id_pedido não explicito, é adicionado pela SEQUENCE
                "id_produto": id_produto,
                "data": data,
                "tipo": tipo,
                "quantidade": quantidade
            }

            oracle.execute(query, dados)
            oracle.connection.commit()
            print(f"Pedido inserido com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao inserir pedido: {e}")
            return False

    def atualizar_pedido(self, db: DatabaseConnection) -> bool:
        try:
            from datetime import datetime
            id_pedido = int(input("Digite o ID do pedido que deseja atualizar: ")) # Pede o ID do pedido a ser atualizado


            if not self.verifica_pedido_id(db, id_pedido): # Verifica se o pedido existe
                print(f"Pedido com ID {id_pedido} não existe.")
                return False

            query_select = """
                SELECT 
                    P.ID_PEDIDO,
                    P.ID_PRODUTO,
                    P.DATA,
                    P.TIPO,
                    P.QUANTIDADE
                FROM PEDIDOS P
                JOIN PRODUTOS PR ON PR.ID_PRODUTO = P.ID_PRODUTO
                WHERE P.ID_PEDIDO = :id_pedido
                """
            oracle = db.conectar()
            oracle.execute(query_select, {"id_pedido": id_pedido})
            pedido_atual = oracle.fetchone()
            if not pedido_atual:
                print("erro: não foi possivel recuperar os dados do pedido")
                return False

            id_pedido, id_produto, data_atual, tipo_atual, quantidade_atual = pedido_atual

            print("\nPressione ENTER para manter o valor atual.\n")

            while True:
                novo_tipo = input(f"Tipo do pedido (COMPRA/VENDA) [{tipo_atual}]: ").strip().upper()
                if novo_tipo == "":
                    novo_tipo = tipo_atual
                    break
                elif novo_tipo in ["COMPRA", "VENDA"]:
                    break
                else:
                    print("Tipo inválido! Digite 'COMPRA' ou 'VENDA'.")


            while True:
                nova_quantidade = input(f"Quantidade [{quantidade_atual}]: ").strip()
                if nova_quantidade == "":
                    nova_quantidade = quantidade_atual
                    break
                try:
                    nova_quantidade = int(nova_quantidade)
                    if nova_quantidade >= 0:
                        break
                    print("a quantidade deve ser maior que 0.")
                except ValueError:
                    print("digite um número válido para a quantidade.")


            nova_data = datetime.now() # Atualiza data/hora para agora

            # Query SQL para atualizar
            query = """
            UPDATE PEDIDOS
            SET ID_PRODUTO = :id_produto,
                DATA = :data,
                TIPO = :tipo,
                QUANTIDADE = :quantidade
            WHERE ID_PEDIDO = :id_pedido
            """

            dados = {
                "id_pedido": id_pedido,
                "id_produto": id_produto,
                "data": nova_data,
                "tipo": novo_tipo,
                "quantidade": nova_quantidade
            }

            # Executa atualização no banco
            oracle.execute(query, dados)
            oracle.connection.commit()
            print(f"Pedido ID {id_pedido} atualizado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao atualizar pedido: {e}")
            return False

    def excluir_pedido(self, db:DatabaseConnection) -> bool :

        try:
            from Python.reports.relatorios import Relatorio
            from datetime import datetime

            id_pedido = int(input("Digite o ID do pedido que deseja excluir: ")) # Solicita o ID do pedido

            # Verifica se o pedido existe
            query_select = """ 
                SELECT 
                    P.ID_PEDIDO,
                    PR.NOME_PRODUTO,
                    P.TIPO,
                    P.QUANTIDADE,
                    P.DATA
                FROM PEDIDOS P
                JOIN PRODUTOS PR ON PR.ID_PRODUTO = P.ID_PRODUTO
                WHERE P.ID_PEDIDO = :id_pedido
            """

            oracle = db.conectar()
            oracle.execute(query_select, {"id_pedido": id_pedido})
            resultado = oracle.fetchone()

            if not resultado:
                print(f"Pedido com ID {id_pedido} não encontrado.")
                return False

            id_pedido, nome_produto, tipo, quantidade, data = resultado

            # Mostra resumo do pedido antes de excluir
            print("\n" + "#"*10 + "Resumo do pedido a ser excluído:"+ 10 * "#")
            print(f"ID: {id_pedido}")
            print(f"Produto: {nome_produto}")
            print(f"Tipo: {tipo}")
            print(f"Quantidade: {quantidade}")
            print(f"Data: {data}")
            print("#" * 30)


            confirmar = input("Tem certeza que deseja excluir este pedido? (S/N): ").strip().upper() # Confirmação do usuário
            if confirmar != "S":
                print("Operação cancelada pelo usuário.")
                return False


            query_delete = "DELETE FROM PEDIDOS WHERE ID_PEDIDO = :id_pedido" # Excluir o pedido
            oracle.execute(query_delete, {"id_pedido": id_pedido})
            oracle.connection.commit()

            print(f"Pedido ID {id_pedido} excluído com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao excluir pedido: {e}")
            return False