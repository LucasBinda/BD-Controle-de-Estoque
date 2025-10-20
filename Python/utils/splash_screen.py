from Python.connection.database import DatabaseConnection
from Python.utils.menu import QUERY_COUNT

class splashScreen :
    def __init__(self) :
        # Consultas de contagem de registros - inicio
        self.qry_total_produtos = QUERY_COUNT.format(tabela="produtos")
        self.qry_total_pedidos = QUERY_COUNT.format(tabela="pedidos")


        # Nome do criador
        self.created_by = "Lucas Binda Santos"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2025/2"





    def get_total_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = DatabaseConnection()
        db.conectar()
        # Retorna o total de registros computado pela query
        return db.sqlToDataFrame(self.qry_total_pedidos)["total_pedidos"].values[0]


    def get_total_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = DatabaseConnection()
        db.conectar()
        # Retorna o total de registros computado pela query
        return db.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]



    def get_updated_screen(self):
        return f"""
            ===========================================================================
            |                  SISTEMA DE CONTROLE DE ESTOQUE                     
            |                                                         
            |  TOTAL DE REGISTROS:                                    
            |      1 - PRODUTOS:         {str(self.get_total_produtos()).rjust(5)}
            |      2 - PEDIDOS           {str(self.get_total_pedidos()).rjust(5)}
            |
            |  CRIADO POR: {self.created_by}
            |
            |  PROFESSOR:  {self.professor}
            |
            |  DISCIPLINA: {self.disciplina}
            |              {self.semestre}                                            
            ===========================================================================
            """