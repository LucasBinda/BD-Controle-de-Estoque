from connection.database import DatabaseConnection

if __name__ == '__main__': # teste de conexão
    db = DatabaseConnection() # instancia a classe
    db.conectar()             # se conecta ao banco de dados
    print("Conexão com o banco de dados Bem Sucedida!")
    sql_query = ("SELECT * FROM Pedidos")
    db.buscarData(sql_query)
