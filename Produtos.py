listProdutos = []


class Produtos:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome


p = Produtos('Morango')
listProdutos.append(p)
