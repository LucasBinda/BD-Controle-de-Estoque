from Python.connection.database import DatabaseConnection

class Relatorio :
    def __init__(self):
        with open("sql/relatorio_pedidos") as f:
            self.query_relatorio_pedidos = f.read()
        with open("sql/relatorio_produtos") as f:
            self.query_relatorio_produtos = f.read()


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