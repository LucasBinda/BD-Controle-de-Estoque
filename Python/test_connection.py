from Main import relatorio
from Create_Tables import createTables
import sys
import os

# Adiciona a pasta raiz do projeto ao path, para poder executar de dentro da pasta Python do projeto, sem mexer nos imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == '__main__': # teste de conexãos
    try:
        relatorio.get_relatorio_estoque_baixo()

        print("Conexão realizada com sucesso")
    except Exception as e:
        # Converte o erro pra string pra facilitar testes
        error_msg = str(e)

        # Verifica se é erro de tabela inexistente (ORA-00942)
        if "ORA-00942" in error_msg:
            print("\nERRO: Tabelas necessárias não foram encontradas no banco de dados.")
            resposta = input("Deseja criar as tabelas agora? (s/n): ").strip().lower()

            if resposta == 's':
                try:
                    ct=createTables()  # Executa a função que cria todas as tabelas
                    ct.run()
                    print("Tabelas criadas com sucesso! Tente novamente executar o relatório.")
                except Exception as create_error:
                    print(f"Erro ao criar as tabelas: {create_error}")
            else:
                print("Operação cancelada. Nenhuma tabela foi criada.")
        else:
            # Outro erro qualquer: exibe normalmente
            print(f"Erro ao gerar relatório: {e}")