class Fornecedores:
    def __init__(self, nome, cidade, UF, logitude, latitude, preco_km):
        self.nome = nome
        self.cidade = cidade
        self.UF = UF
        self.logitude = logitude
        self.latitude = latitude
        self.preco_km = preco_km


nome = input("Digite o nome")
cidade = input("Digite a cidade")
p1 = Fornecedores(nome, cidade, "MG", -88569525, -85426592, 25.50)

print(p1.nome)
print(p1.cidade)
print(p1.UF)
print(p1.logitude)
print(p1.latitude)
print(p1.preco_km)
