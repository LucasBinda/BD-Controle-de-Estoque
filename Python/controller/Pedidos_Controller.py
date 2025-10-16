from typing import List, Optional
from connection.oracle_query import OracleQuery
from model.Pedidos import Pedido
from model.Produtos import Produto
import pandas as pd

class PedidosController:
    def __init__(self):
        self.query = OracleQuery()

    def criar_pedido(self, id_pedido: int, data: str, tipo: str, quantidade: int,
                     id_produto: int, id_fornecedor: int = None, id_comprador: int = None) -> Optional[Pedido]:
        """Cria um novo pedido"""
        try:
            # Primeiro busca o produto
            produtos_ctrl = ProdutosController()
            produto = produtos_ctrl.buscar_produto_por_id(id_produto)

            if not produto:
                print("❌ Produto não encontrado")
                return None

            # Prepara dados do pedido
            pedido_data = {
                'id_pedido': id_pedido,
                'data': data,
                'tipo': tipo,
                'quantidade': quantidade,
                'id_produto': id_produto,
                'id_fornecedor': id_fornecedor,
                'id_comprador': id_comprador
            }

            # Insere o pedido
            resultado = self.query.inserir_pedido(pedido_data)
            if resultado > 0:
                # Atualiza estoque do produto
                if tipo.upper() == 'ENTRADA':
                    novo_estoque = produto.get_estoque_atual() + quantidade
                else:  # SAIDA
                    novo_estoque = produto.get_estoque_atual() - quantidade

                produtos_ctrl.atualizar_estoque(id_produto, novo_estoque)

                # Retorna o pedido criado
                return self.buscar_pedido_por_id(id_pedido)

            return None

        except Exception as e:
            print(f"❌ Erro ao criar pedido: {e}")
            return None

    def buscar_pedido_por_id(self, pedido_id: int) -> Optional[Pedido]:
        """Busca um pedido pelo ID"""
        try:
            df = self.query.buscar_pedido_por_id(pedido_id)
            if not df.empty:
                row = df.iloc[0].to_dict()

                # Cria o objeto Produto
                produto_data = {
                    'ID_PRODUTO': row['ID_PRODUTO'],
                    'NOME_PRODUTO': row['NOME_PRODUTO'],
                    'DESCRICAO': row['DESCRICAO'],
                    'PRECO': row['PRECO'],
                    'ESTOQUE_ATUAL': row['ESTOQUE_ATUAL']
                }
                produto = Produto.from_dict(produto_data)

                # Cria o Pedido com o Produto
                return Pedido.from_dict(row, produto)
            return None
        except Exception as e:
            print(f"❌ Erro ao buscar pedido: {e}")
            return None

    def listar_pedidos(self) -> List[Pedido]:
        """Lista todos os pedidos"""
        try:
            df = self.query.buscar_pedidos()
            pedidos = []

            for _, row in df.iterrows():
                row_dict = row.to_dict()

                # Cria o objeto Produto
                produto_data = {
                    'ID_PRODUTO': row_dict['ID_PRODUTO'],
                    'NOME_PRODUTO': row_dict['NOME_PRODUTO'],
                    'DESCRICAO': row_dict['DESCRICAO'],
                    'PRECO': row_dict['PRECO'],
                    'ESTOQUE_ATUAL': row_dict['ESTOQUE_ATUAL']
                }
                produto = Produto.from_dict(produto_data)

                # Cria o Pedido com o Produto
                pedido = Pedido.from_dict(row_dict, produto)
                pedidos.append(pedido)

            return pedidos
        except Exception as e:
            print(f"❌ Erro ao listar pedidos: {e}")
            return []

    def buscar_pedidos_por_tipo(self, tipo: str) -> List[Pedido]:
        """Busca pedidos por tipo (ENTRADA/SAIDA)"""
        try:
            df = self.query.buscar_pedidos_por_tipo(tipo)
            pedidos = []

            for _, row in df.iterrows():
                row_dict = row.to_dict()

                # Cria o objeto Produto
                produto_data = {
                    'ID_PRODUTO': row_dict['ID_PRODUTO'],
                    'NOME_PRODUTO': row_dict['NOME_PRODUTO'],
                    'DESCRICAO': row_dict['DESCRICAO'],
                    'PRECO': row_dict['PRECO'],
                    'ESTOQUE_ATUAL': row_dict['ESTOQUE_ATUAL']
                }
                produto = Produto.from_dict(produto_data)

                # Cria o Pedido com o Produto
                pedido = Pedido.from_dict(row_dict, produto)
                pedidos.append(pedido)

            return pedidos
        except Exception as e:
            print(f"❌ Erro ao buscar pedidos por tipo: {e}")
            return []

    def buscar_pedidos_por_produto(self, id_produto: int) -> List[Pedido]:
        """Busca pedidos por produto"""
        try:
            df = self.query.buscar_pedidos_por_produto(id_produto)
            pedidos = []

            for _, row in df.iterrows():
                row_dict = row.to_dict()

                # Cria o objeto Produto
                produto_data = {
                    'ID_PRODUTO': row_dict['ID_PRODUTO'],
                    'NOME_PRODUTO': row_dict['NOME_PRODUTO'],
                    'DESCRICAO': row_dict['DESCRICAO'],
                    'PRECO': row_dict['PRECO'],
                    'ESTOQUE_ATUAL': row_dict['ESTOQUE_ATUAL']
                }
                produto = Produto.from_dict(produto_data)

                # Cria o Pedido com o Produto
                pedido = Pedido.from_dict(row_dict, produto)
                pedidos.append(pedido)

            return pedidos
        except Exception as e:
            print(f"❌ Erro ao buscar pedidos por produto: {e}")
            return []

    def atualizar_pedido(self, pedido: Pedido) -> bool:
        """Atualiza um pedido existente"""
        try:
            linhas_afetadas = self.query.atualizar_pedido(pedido.to_dict())
            return linhas_afetadas > 0
        except Exception as e:
            print(f"❌ Erro ao atualizar pedido: {e}")
            return False

    def excluir_pedido(self, id_pedido: int) -> bool:
        """Exclui um pedido"""
        try:
            linhas_afetadas = self.query.excluir_pedido(id_pedido)
            return linhas_afetadas > 0
        except Exception as e:
            print(f"❌ Erro ao excluir pedido: {e}")
            return False