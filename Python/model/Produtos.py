class Produto:
    def __init__(self, id_produto:int=None, nome_produto:str=None, descricao:str=None, preco:int=None, estoque_atual:int=None):
        self.set_id_produto(id_produto)
        self.set_nome_produto(nome_produto)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque_atual(estoque_atual)


    def get_id_produto(self):
        return self.__id_produto

    def get_nome_produto(self):
        return self.__nome_produto

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def get_estoque_atual(self):
        return self.__estoque_atual


    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto

    def set_nome_produto(self, nome_produto):
        self.__nome_produto = nome_produto

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def set_estoque_atual(self, estoque_atual):
        self.__estoque_atual = estoque_atual


    def to_string(self):
        return (f"ID: {self.get_id_produto()} | "
                f"Nome: {self.get_nome_produto()} | "
                f"Descrição: {self.get_descricao()} | "
                f"Preço: {self.get_preco()} | "
                f"Estoque: {self.get_estoque_atual()}")