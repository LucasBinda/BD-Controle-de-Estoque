from utils.restart_tables import createTables

if __name__ == "__main__":
    x = createTables() # objeto da classe que contem o script para recriar as tables do 0, ja com os dados padrões inseridos
    x.run()