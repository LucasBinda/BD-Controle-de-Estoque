from datetime import date
from Produtos import Produto

class Pedido:
    def __init__(self, id_pedido:int=None, data:date=None, tipo:str=None, quantidade:int=None, produto:Produto=None, id_fornecedor:int=None, id_comprador:int=None):
        self.set_id_pedido(id_pedido)
        self.set_data(data)
        self.set_tipo(tipo)
        self.set_quantidade(quantidade)
        self.set_produto(produto)     # OBJETO PRODUTO que contem id produto
        self.set_id_fornecedor(id_fornecedor)
        self.set_id_comprador(id_comprador)


    def get_id_pedido(self):
        return self.__id_pedido

    def get_data(self):
        return self.__data

    def get_tipo(self):
        return self.__tipo

    def get_quantidade(self):
        return self.__quantidade

    def get_produto(self):
        return self.__produto

    def get_id_fornecedor(self):
        return self.__id_fornecedor

    def get_id_comprador(self):
        return self.__id_comprador


    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    def set_data(self, data):
        self.__data = data

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def set_produto(self, produto):
        self.__produto = produto

    def set_id_fornecedor(self, id_fornecedor):
        self.__id_fornecedor = id_fornecedor

    def set_id_comprador(self, id_comprador):
        self.__id_comprador = id_comprador

    # to_string
    def to_string(self) -> str:
        return (f"ID Pedido: {self.get_id_pedido()} | "
                f"Data: {self.get_data()} | "
                f"Tipo: {self.get_tipo()} | "
                f"Quantidade: {self.get_quantidade()} | "
                f"Produto: {self.get_produto()} | "
                f"ID Fornecedor: {self.get_id_fornecedor()} | "
                f"ID Comprador: {self.get_id_comprador()}")
