"""
Módulo do cálculo da otimização.

Esse modoulo fica encarregado de receber os parametros do
modulo cliente e assim realiza as operações de otimização.

Após concluido, retorna a informação ao usuário.
"""
import gurobipy as gp

def otimizacao(produtos, fabricas, clientes, custo, demandas, ofertas):
    """Criando o Modelo"""
    m = gp.Model()

    """
    Variáveis de Decisão
    
    É criada a variável xijk variando o número de produtos,
    número de fabricas e número de clientes
    """
    x = m.addVars(produtos, fabricas, clientes, vtype=gp.GRB.INTEGER)

    """
    Criação da Função Objetivo
    
    Somatório da quantidade de produto xijk pelo valor do produto xijk
    Ambos variando de acordo com o número de produtos, fonecedores e clientes
    """
    m.setObjective(gp.quicksum(x[i, j, k] * custo[i, j, k]
                               for i in range(produtos) for j in range(fabricas) for k in range(clientes)),
                   sense=gp.GRB.MINIMIZE)

    """
    Criação das Restrições de oferta
    
    Restrição de oferta de problema balanceado, fazendo o somatório da
    quantidade de produtos variando pelo número de clientes
    
    É comparado com o valor da oferta variando pela quantidade de produtos e fabricas
    """
    c1 = m.addConstrs(gp.quicksum(x[i, j, k] for k in range(clientes))
                      == ofertas[i, j] for i in range(produtos) for j in range(fabricas))

    """
    Criação das Restrições de demanda
    
    Restrição de demanda de problema balanceado, fazendo o somatório da
    quantidade de produtos variando pelo número de fabricas
    
    É comparado com o valor da demanda variando pela quantidade de produtos e clientes
    """
    c2 = m.addConstrs(gp.quicksum(x[i, j, k] for j in range(fabricas))
                      == demandas[i, k] for i in range(produtos) for k in range(clientes))

    """Executa o modelo"""
    m.optimize()
    valor = m.objval
    return valor
