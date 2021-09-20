import gurobipy as gp


def otimizacao(produtos, fabricas, clientes, custo, demandas, ofertas):
    # Criando o Modelo
    m = gp.Model()
    # Variáveis de Decisão
    x = m.addVars(produtos, fabricas, clientes, vtype=gp.GRB.INTEGER)

    # Função Objetivo
    m.setObjective(gp.quicksum(x[i, j, k] * custo[i, j, k]
                               for i in range(produtos) for j in range(fabricas) for k in range(clientes)),
                   sense=gp.GRB.MINIMIZE)

    # Restrições de oferta
    c1 = m.addConstrs(gp.quicksum(x[i, j, k] for k in range(clientes))
                      == ofertas[i, j] for i in range(produtos) for j in range(fabricas))

    # Restrições de demanda
    c2 = m.addConstrs(gp.quicksum(x[i, j, k] for j in range(fabricas))
                      == demandas[i, k] for i in range(produtos) for k in range(clientes))

    # Executa o modelo
    m.optimize()
    valor = m.objval
    return valor