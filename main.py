import gurobipy as gp

# Parametros do problema
qtd_fabricas = 3
qtd_clientes = 2
qtd_produtos = 3

vet_ofertas = [[200, 250, 350], [150, 90, 60], [30, 50, 40]]

vet_demandas = [[300, 500], [200, 100], [40, 80]]

vet_custos = [[[12.12, 12.12], [10.90, 10.90], [10.35, 10.35]],
              [[6.45, 6.45], [5.2, 5.2], [5.83, 5.83]],
              [[20.75, 20.75], [23, 23], [19.14, 19.14]]]

vet_fretes = [[[1.03, 0.98], [2.02, 1.96], [2.29, 2.23]],
              [[0.52, 0.49], [1.10, 0.98], [1.15, 1.12]],
              [[2.06, 1.96], [4.04, 3.92], [4.58, 4.46]]]

# Rótulos das fábricas, clientes e produtos
produtos = list()
for i in range(qtd_produtos):
    produtos.append("Pro_{}".format(i + 1))

fabricas = list()
for j in range(qtd_fabricas):
    fabricas.append("Fab_{}".format(j + 1))

clientes = list()
for k in range(qtd_clientes):
    clientes.append("Cli_{}".format(k + 1))

# Dicionário com as Ofertas
ofertas = dict()
for i in range(qtd_produtos):
    for j in range(qtd_fabricas):
        rot_fab = fabricas[j]
        rot_pro = produtos[i]
        ofertas[rot_pro, rot_fab] = vet_ofertas[i][j]

#Dicionário com a Demandas
demandas = dict()
for i in range(qtd_produtos):
    for j in range(qtd_clientes):
        rot_pro = produtos[i]
        rot_cli = clientes[j]
        demandas[rot_pro, rot_cli] = vet_demandas[i][j]

# Associando Fabricas com Clientes com Preço Total
total = dict()
for i in range(qtd_produtos):
    for j in range(qtd_fabricas):
        for k in range(qtd_clientes):
            rot_pro = produtos[i]
            rot_fab = fabricas[j]
            rot_cli = clientes[k]
            total[rot_pro, rot_fab, rot_cli] = vet_custos[i][j][k] + vet_fretes[i][j][k]

#print("Produtos: ", produtos)
#print("Fabricas: ", fabricas)
#print("Clientes: ", clientes)
#print("Ofertas: ", ofertas)
#print("Demandas: ", demandas)
#print("Custos dos Produtos: ", custos)
#print("Custos dos Fretes: ", fretes)
#print("Custos dos Produtos com Frete: ", total)

# Criando o Modelo
m = gp.Model()

# Variáveis de Decisão
x = m.addVars(produtos, fabricas, clientes, vtype=gp.GRB.INTEGER)

# Função Objetivo
m.setObjective(gp.quicksum(x[i, j, k] * total[i, j, k] for i in produtos for j in fabricas for k in clientes),
               sense=gp.GRB.MINIMIZE)

# Restrições de oferta
c1 = m.addConstrs(gp.quicksum(x[i, j, k] for k in clientes)
                  == ofertas[i, j] for i in produtos for j in fabricas)

# Restrições de demanda
c2 = m.addConstrs(gp.quicksum(x[i, j, k] for j in fabricas)
                  == demandas[i, k] for i in produtos for k in clientes)

#Executa o modelo
m.optimize()

print(x)