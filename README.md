<h1 align="center"> Controle de Estoque </h1>

Programa de Controle de estoque usando banco de dados Oracle com SQL e manipulação de Banco de dados com Python



## Pre-requisitos
- Python
- Oracle Database
## Instalação bibliotecas Python
Abra o terminal e acesse o diretorio do programa.

[Python](Python)

instale as  bibliotecas necessarias com o comando:
```
pip install -r requirements.txt
```


## Como executar o programa:

Você pode testar a conexão entre o programa e o Banco de Dados executando o arquivo test_connection.py pelo terminal exemplo abaixo:
```
python test_connection.py
```
Lembre-se você precisa estar dentro da pasta [Python](Python) do projeto no terminal para isso funcionar    


- depois da primeira execução do programa pelo teste ou pelo metodo principal, ele vai dar um "erro" e notificar da criação do arquivo de conexão com o banco de dados.


ele vai pedir para você colocar as credenciais do seu banco de dados em [config](Python/connection/config/config.json):
```
Python/connection/config/config.json
```
Certifique-se de que o usuário do banco possui todos os privilégios para o programa rodar sem nenhum problema.

- E lembre-se de testar a conexão com o banco de dados executando o test_connection.py novamente.



Execute o programa principal pelo terminal de comandos com:
```
python Main.py
```

[Main](Python/Main.py) localização do arquivo principal do programa.


## Organização:

- [Diagrams](Diagrams) Diretorio que contem o diagrama relacional, junto de um script mermaidChart.
- [Python](Python) Diretorio principal.
  * [sql](Python/sql): Diretorio que possui todos os scripts sql.
  * [utils](Python/utils): Diretorio com alguns menus que são usados na classe principal, e também o script restart_tables.py que serve para recriar os dados do Banco do 0.
  * [reports](Python/reports): Diretorio contendo a classe responsavel por gerar todos os relatorios.
  * [model](Python/model): Diretorio que contem as classes das entidades das tabelas do banco de dados.
  * [controller](Python/controller): Diretorio que contem as classes para controle das entidades do banco de dados.
  * [connection](Python/connection): Diretorio que contem a classe de conexão com o banco de
    * [config](Python/connection/config): Diretorio com o arquivo de credenciais da conexão com o banco de dados, é nesse diretorio que você vai precisar colocar as credencias do seu usuario do banco de dados.