from typing import List, Optional
from connection.oracle_query import OracleQuery
from model.Produtos import Produto
import pandas as pd

class ProdutosController:
    def __init__(self):
        self.query = OracleQuery()

    def criar_produto(self, id_produto: int, nome_produto: str, descricao: str, preco: float, estoque_atual: int) -> Optional[Produto]:
        """Cria um novo produto"""
        try:
            produto_data = {
                'id_produto': id_produto,
                'nome_produto': nome_produto,
                'descricao': descricao,
                'preco': preco,
                'estoque_atual': estoque_atual
            }

            resultado = self.query.inserir_produto(produto_data)
            if resultado > 0:
                return self.buscar_produto_por_id(id_produto)
            return None

        except Exception as e:
            print(f"❌ Erro ao criar produto: {e}")
            return None

    def buscar_produto_por_id(self, id_produto: int) -> Optional[Produto]:
        """Busca um produto pelo ID"""
        try:
            df = self.query.buscar_produto_por_id(id_produto)
            if not df.empty:
                return Produto.from_dict(df.iloc[0].to_dict())
            return None
        except Exception as e:
            print(f"❌ Erro ao buscar produto: {e}")
            return None

    def listar_produtos(self) -> List[Produto]:
        """Lista todos os produtos"""
        try:
            df = self.query.buscar_produtos_ativos()
            return [Produto.from_dict(row) for row in df.to_dict('records')]
        except Exception as e:
            print(f"❌ Erro ao listar produtos: {e}")
            return []

    def buscar_produtos_por_nome(self, nome: str) -> List[Produto]:
        """Busca produtos por nome (busca parcial)"""
        try:
            df = self.query.buscar_produtos_por_nome(nome)
            return [Produto.from_dict(row) for row in df.to_dict('records')]
        except Exception as e:
            print(f"❌ Erro ao buscar produtos por nome: {e}")
            return []

    def atualizar_produto(self, produto: Produto) -> bool:
        """Atualiza um produto existente"""
        try:
            linhas_afetadas = self.query.atualizar_produto(produto.to_dict())
            return linhas_afetadas > 0
        except Exception as e:
            print(f"❌ Erro ao atualizar produto: {e}")
            return False

    def atualizar_estoque(self, id_produto: int, novo_estoque: int) -> bool:
        """Atualiza apenas o estoque de um produto"""
        try:
            linhas_afetadas = self.query.atualizar_estoque_produto(id_produto, novo_estoque)
            return linhas_afetadas > 0
        except Exception as e:
            print(f"❌ Erro ao atualizar estoque: {e}")
            return False

    def excluir_produto(self, id_produto: int) -> bool:
        """Exclui um produto"""
        try:
            linhas_afetadas = self.query.excluir_produto(id_produto)
            return linhas_afetadas > 0
        except Exception as e:
            print(f"❌ Erro ao excluir produto: {e}")
            return False

    def produtos_com_estoque_baixo(self, limite: int = 5) -> List[Produto]:
        """Lista produtos com estoque abaixo do limite"""
        try:
            df = self.query.relatorio_estoque_baixo(limite)
            return [Produto.from_dict(row) for row in df.to_dict('records')]
        except Exception as e:
            print(f"❌ Erro ao buscar produtos com estoque baixo: {e}")
            return []