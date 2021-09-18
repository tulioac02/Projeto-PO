import gurobipy as gp

fabricas = input("Digite nova fabrica")

# Parametros do problema
qtd_fabricas = 3
qtd_clientes = 2
vet_ofertas_prod_01 = [200, 250, 350]
vet_demandas_prod_01 = [300, 500]
vet_custos_prod_01 = [[13.15, 13.10], [12.92, 12.86], [12.64, 12.58]]

vet_ofertas_prod_02 = [150, 90, 60]
vet_demandas_prod_02 = [200, 100]
vet_custos_prod_02 = [[6.97, 6.94],
                      [6.21, 6.18],
                      [6.98, 6.95]]

vet_ofertas_prod_03 = [30, 50, 40]
vet_demandas_prod_03 = [40, 80]
vet_custos_prod_03 = [[22.81, 22.71], [27.04, 26.92], [23.72, 23.60]]

# Rótulos das fábricas e clientes
fabricas = list()
for i in range(qtd_fabricas):
    fabricas.append("Fab_{}".format(i + 1))

clientes = list()
for j in range(qtd_clientes):
    clientes.append("Cli_{}".format(j + 1))


# Dicionário com as ofertas
ofertas_prod_01 = dict()
for idx, valor in enumerate(vet_ofertas_prod_01):
    rotulo = fabricas[idx]
    ofertas_prod_01[rotulo] = valor

ofertas_prod_02 = dict()
for idx, valor in enumerate(vet_ofertas_prod_02):
    rotulo = fabricas[idx]
    ofertas_prod_02[rotulo] = valor

ofertas_prod_03 = dict()
for idx, valor in enumerate(vet_ofertas_prod_03):
    rotulo = fabricas[idx]
    ofertas_prod_03[rotulo] = valor

# Dicionário com as demandas
demandas_prod_01 = dict()
for idx, valor in enumerate(vet_demandas_prod_01):
    rotulo = clientes[idx]
    demandas_prod_01[rotulo] = valor

demandas_prod_02 = dict()
for idx, valor in enumerate(vet_demandas_prod_02):
    rotulo = clientes[idx]
    demandas_prod_02[rotulo] = valor

demandas_prod_03 = dict()
for idx, valor in enumerate(vet_demandas_prod_03):
    rotulo = clientes[idx]
    demandas_prod_03[rotulo] = valor

# Dicionário de custos
custos_prod_01 = dict()
for i in range(qtd_fabricas):
    for j in range(qtd_clientes):
        rot_fab = fabricas[i]
        rot_cli = clientes[j]
        custos_prod_01[rot_fab, rot_cli] = vet_custos_prod_01[i][j]

custos_prod_02 = dict()
for i in range(qtd_fabricas):
    for j in range(qtd_clientes):
        rot_fab = fabricas[i]
        rot_cli = clientes[j]
        custos_prod_02[rot_fab, rot_cli] = vet_custos_prod_02[i][j]

custos_prod_03 = dict()
for i in range(qtd_fabricas):
    for j in range(qtd_clientes):
        rot_fab = fabricas[i]
        rot_cli = clientes[j]
        custos_prod_03[rot_fab, rot_cli] = vet_custos_prod_03[i][j]

#print(fabricas)
#print(clientes)

print("Ofertas do produto 01:", ofertas_prod_01)
print("Demanda do produto 01:", demandas_prod_01)
print("Custos do produto 01:", custos_prod_01)

print("Ofertas do produto 02:", ofertas_prod_02)
print("Demanda do produto 02:", demandas_prod_02)
print("Custos do produto 02:", custos_prod_02)

print("Ofertas do produto 03:", ofertas_prod_03)
print("Demanda do produto 03:", demandas_prod_03)
print("Custos do produto 03:", custos_prod_03)

# Criando modelo
m = gp.Model()

# Variáveis de Decisão
x = m.addVars(fabricas, clientes, vtype=gp.GRB.INTEGER)
y = m.addVars(fabricas, clientes, vtype=gp.GRB.INTEGER)
z = m.addVars(fabricas, clientes, vtype=gp.GRB.INTEGER)

# Função objetivo
m.setObjective(gp.quicksum(x[i, j] * custos_prod_01[i, j] for i in fabricas for j in clientes) +
               gp.quicksum(y[i, j] * custos_prod_02[i, j] for i in fabricas for j in clientes) +
               gp.quicksum(z[i, j] * custos_prod_03[i, j] for i in fabricas for j in clientes), sense=gp.GRB.MINIMIZE)

# Restrições de oferta
c1 = m.addConstrs(gp.quicksum(x[i, j] for j in clientes) == ofertas_prod_01[i] for i in fabricas)
c2 = m.addConstrs(gp.quicksum(y[i, j] for j in clientes) == ofertas_prod_02[i] for i in fabricas)
c3 = m.addConstrs(gp.quicksum(z[i, j] for j in clientes) == ofertas_prod_03[i] for i in fabricas)

# Restrições de demanda
c4 = m.addConstrs(gp.quicksum(x[i, j] for i in fabricas) == demandas_prod_01[j] for j in clientes)
c5 = m.addConstrs(gp.quicksum(y[i, j] for i in fabricas) == demandas_prod_02[j] for j in clientes)
c6 = m.addConstrs(gp.quicksum(z[i, j] for i in fabricas) == demandas_prod_03[j] for j in clientes)

# Executa o modelo
m.optimize()
