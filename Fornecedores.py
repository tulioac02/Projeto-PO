listFornecedores = []


class Fornecedores:
    def __init__(self, nome, cidade, UF, frete):
        self.nome = nome
        self.cidade = cidade
        self.UF = UF
        self.frete = frete

    def __repr__(self):
        return '{} - {} - {} - {}'.format(self.nome, self.cidade, self.UF, self.frete)


f1 = Fornecedores('Constrular', 'Minas Novas', 'MG', 5.00)
listFornecedores.append(f1)

f2 = Fornecedores('Constrular', 'Turmalina', 'MG', 5.50)
listFornecedores.append(f2)