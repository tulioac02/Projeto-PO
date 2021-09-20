import gurobipy as gp


def otimizacao(produtos, fabricas, clientes, custo, demandas, ofertas):
    # Criando o Modelo
    m = gp.Model()
    print(produtos, fabricas, clientes, demandas, ofertas, custo)
    # Variáveis de Decisão
    x = m.addVars(produtos, fabricas, clientes, vtype=gp.GRB.INTEGER)

    # # Função Objetivo
    # m.setObjective(gp.quicksum(x[i, j, k] * custo[i] for i in produtos for j in fabricas for k in clientes),
    #                sense=gp.GRB.MINIMIZE)
    # #
    # # Restrições de oferta
    # c1 = m.addConstrs(gp.quicksum(x[i, j, k] for k in clientes)
    #                   == ofertas[i, j] for i in produtos for j in fabricas)
    #
    # # Restrições de demanda
    # c2 = m.addConstrs(gp.quicksum(x[i, j, k] for j in fabricas)
    #                   == demandas[i, k] for i in produtos for k in clientes)
    #
    # # Executa o modelo


    return m.optimize()
