import gurobipy as gp
# armazenar produtos, clientes e fabricas em dicionarios
# pesquisar produtos, clientes e fabricas pelo indice deles
# jogar em produtos pesquisados
# jogar em clientes pesquisados
# jogar em fabricas pesquisadas

# clientes, produtos e fabricas. Armazenando
produtos_cadastrados = {0: 'Telha1', 1: 'Telha2', 2: 'Telha3'}
clientes_cadastrados = {0: 'Minas Novas', 1: 'Turmalina'}
fabricas_cadastradas = {0: 'Precom', 1: 'Brasilit', 2: 'Imbralit'}

# clientes, produtos e fabricas. Verificando quantidades
print(produtos_cadastrados, '\n')
while True:
    num_prod = int(input('Digite a quantidade de produtos: '))

    if num_prod > len(produtos_cadastrados) or num_prod < 0:
        print('O código informado é zero, negativo ou superior a quantidade de produtos, tente novamente.')
        continue
    else:
        break

print('\n', fabricas_cadastradas, '\n')
while True:
    num_fab = int(input('Digite a quantidade da fabricas: '))

    if num_fab > len(fabricas_cadastradas) or num_fab < 0:
        print('O código informado é zero, negativo ou superior a quantidade de fabricas, tente novamente.')
        continue
    else:
        break

print('\n', clientes_cadastrados, '\n')
while True:
    num_cli = int(input('Digite a quantidade de cliente: '))

    if num_cli > len(clientes_cadastrados) or num_cli < 0:
        print('O código informado é zero, negativo ou superior a quantidade de fabricas, tente novamente.')
        continue
    else:
        break

# Adicionando produtos a lista de pesquisa
print('\n', produtos_cadastrados, '\n')
produto_pesquisado = list()
for produto in range(num_prod):
    while True:
        codigo_produto = int(input('Informe o código do produto cadastrado: '))
        if codigo_produto not in produtos_cadastrados.keys():
            print('Erro: Produto não esta no estoque!')
            continue
        else:
            produto_pesquisado.append(produtos_cadastrados.get(codigo_produto))
        break

# Adicionando Fabrica a lista de pesquisa
print('\n', fabricas_cadastradas, '\n')
fabrica_pesquisada = list()
for fab in range(num_fab):
    while True:
        codigo_fabrica = int(input('Informe o código da fabrica cadastrada: '))
        if codigo_fabrica not in fabricas_cadastradas.keys():
            print('Erro: Fábrica Inexistente!')
        else:
            fabrica_pesquisada.append(fabricas_cadastradas.get(codigo_fabrica))
        break

# Adicionando Clientes a lista de pesquisa
print('\n', clientes_cadastrados, '\n')
cliente_pesquisado = list()
for cliente in range(num_cli):
    while True:
        codigo_cliente = int(input('Informe o código da loja cadastrada: '))
        if codigo_cliente not in clientes_cadastrados.keys():
            print('Erro: Cliente não registrado!')
        else:
            cliente_pesquisado.append(clientes_cadastrados.get(codigo_cliente))
        break

print('\n')
print(f'Produtos Pesquisados: {produto_pesquisado}')
print(f'Fabricas Pesquisadas: {fabrica_pesquisada}')
print(f'Clientes Pesquisados: {cliente_pesquisado}')
print('\n')

# cadastro de ofertas
vet_ofertas = list()
for i in range(num_prod):
    ofertas = list()
    for j in range(num_fab):
        qtd_oferta = int(input(f'Quantidade ofertada do produto {produto_pesquisado[i]} '
                                f'pela fabrica {fabrica_pesquisada[j]}: '))
        ofertas.append(qtd_oferta)
    vet_ofertas.append(ofertas)
    print('\n')

# cadastro de demandas
vet_demandas = list()
for i in range(num_prod):
    demandas = list()
    for j in range(num_cli):
        qtd_demanda = int(input(f'Quantidade demandada do produto { produto_pesquisado[i] } '
                                f'pelo cliente { cliente_pesquisado[j]}: '))
        demandas.append(qtd_demanda)
    vet_demandas.append(demandas)
    print('\n')

# cadastro de produtos
vet_custos = list()
for i in range(num_prod):
    fab_cli = list()
    for j in range(num_fab):
        cli = list()
        for k in range(num_cli):
            custo = float(input(f'Digite o preço do produto { produto_pesquisado[i] } '
                                f'da fabrica { fabrica_pesquisada[j] } para o cliente { cliente_pesquisado[k]}: '))
            cli.append(custo)
        fab_cli.append(cli)
    vet_custos.append(fab_cli)
    print('\n')

# Impressão de dados
for i in range(num_prod):
    for j in range(num_fab):
            print(f'A oferta do produto { produto_pesquisado[i] } '
                                f'na fabrica { fabrica_pesquisada[j] } e: { vet_ofertas[i][j]} ')
    print('\n')

for i in range(num_prod):
    for j in range(num_cli):
        print(f'A demanda do produto { produto_pesquisado[i] }'
              f' na fabrica { cliente_pesquisado[j] } e: { vet_demandas[i][j]} ')
    print('\n')

for i in range(num_prod):
    for j in range(num_fab):
        for k in range(num_cli):
            print(f'O preço do produto { produto_pesquisado[i] } '
                  f'da fabrica { fabrica_pesquisada[j] } para o '
                  f'cliente { cliente_pesquisado[k] } e: { vet_custos[i][j][k]}')
    print('\n')

# Parametros do problema
qtd_produtos = len(produto_pesquisado)
qtd_fabricas = len(fabrica_pesquisada)
qtd_clientes = len(cliente_pesquisado)

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
            total[rot_pro, rot_fab, rot_cli] = vet_custos[i][j][k]

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

print("")

#Impressão das informações
for i in produtos:
    print("Produto: ",i  )
    for j in fabricas:
        for k in clientes:
            qtd = round(x[i, j, k].X)
            if qtd > 0:
                print("Transportar {} unidade(s) da fabrica {} para o cliente {}.".format(qtd, j, k))
    print("")