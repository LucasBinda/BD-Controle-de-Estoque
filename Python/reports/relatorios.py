from Python.connection.database import DatabaseConnection

class Relatorio :
    def __init__(self):

        with open("sql/relatorio_pedidos.sql") as f: #relatorio de pedidos
            self.query_relatorio_pedidos = f.read()
        with open("sql/relatorio_produtos.sql") as f: #relatorio de produtos
            self.query_relatorio_produtos = f.read()
        with open("sql/relatorio_produtos_por_pedido.sql") as f: #relatorio de produtos
            self.query_relatorio_produtos_por_pedido = f.read()
        with open("sql/relatorio_estoque_baixo.sql") as f:
            self.query_relatorio_estoque_baixo = f.read()


    def get_relatorio_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = DatabaseConnection()
        db.conectar()
        # Recupera os dados transformando em um DataFrame
        print(db.sqlToDataFrame(self.query_relatorio_pedidos))
        input("Pressione Enter para Sair do Relatório de Pedidos")

    def get_relatorio_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = DatabaseConnection()
        db.conectar()
        # Recupera os dados transformando em um DataFrame
        print(db.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para Sair do Relatório de Produtos")

    def get_relatorio_produtos_por_pedido(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = DatabaseConnection()
        db.conectar()
        # Recupera os dados transformando em um DataFrame
        print(db.sqlToDataFrame(self.query_relatorio_produtos_por_pedido))
        input("Pressione Enter para Sair do Relatório de Produtos por Pedidos")

    def get_relatorio_estoque_baixo(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = DatabaseConnection()
        db.conectar()
        # Recupera os dados transformando em um DataFrame
        print(db.sqlToDataFrame(self.query_relatorio_estoque_baixo))
        input("Pressione Enter para Sair do Relatório de estoque baixo")