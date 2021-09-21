"""
Módulo principal

Apresenta a interação com usuário, dados armazenados e a opções disponíveis de menu

A partir dele é chamada a função para realizar a operação de otimização pelo Gurobi
"""
import sys
import PySimpleGUI as Sg
import Backend

Sg.theme('DefaultNoMoreNagging')

produtos_cadastrados = {0: 'Telha1', 1: 'Telha2', 2: 'Telha3'}
clientes_cadastrados = {0: 'Minas Novas', 1: 'Turmalina'}
fornecedores_cadastrados = {0: 'Precom', 1: 'Brasilit', 2: 'Imbralit'}

produto_pesquisado = list()
cliente_pesquisado = list()
fornecedor_pesquisado = list()

quantFor = 1
quantPro = 1
quantCli = 1

demanda = dict()
oferta = dict()
custo = dict()

''' Menu '''
menu_opt = [['&Produtos', ['Cadastrar Produtos', 'Produtos Cadastrados']],
            ['&Lojas', ['Cadastrar Lojas', 'Lojas Cadastradas']],
            ['&Fornecedores', ['Cadastrar Fornecedores', 'Fornecedores Cadastrados']],
            ['&Orçamentos', ['Fazer Pedido']],
            ['&Sobre', ['Quem Somos']]
            ]

def home():
    """Função para criar o layout e a janela inicial"""
    layout_home = [
        [Sg.Menu(menu_opt)],
        [Sg.Text('Bem Vindo!', auto_size_text=True, pad=(0, 150))],
        [Sg.Button('Sair', button_color='gray', pad=(0, 30))]
    ]

    my_home = Sg.Window('Inicio', layout=layout_home, element_justification='c',
                        size=(1000, 600), margins=(0, 0), finalize=True)
    return my_home


def cadastrar_produtos():
    """Cria a janela para o cadastro de produtos"""
    layout_cadastrar_produtos = [
        [Sg.Text('Nome do Produto')],
        [Sg.Input(key='nome_produto', size=(47, 5))],
        [Sg.Button('Cadastrar', key='btnCadProduto', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cadastrar_pd = Sg.Window('Cadastrar Produtos', layout=layout_cadastrar_produtos, element_justification='c',
                             size=(1000, 600), margins=(0, 0), finalize=True)
    return cadastrar_pd


def mostrar_produtos():
    """Cria a janela para listar os produtos já cadastrados"""
    layout_mostrar_produtos = [
        [Sg.Listbox(values=[items for items in produtos_cadastrados.values()], key='produtos', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    mostrar_pd = Sg.Window('Lista de Produtos', layout=layout_mostrar_produtos, element_justification='c',
                           size=(1000, 600), margins=(0, 0), finalize=True)
    return mostrar_pd


def cadastrar_loja():
    """Cria a janela para cadastrar as lojas/cliente"""
    layout_cadastrar_lojas = [
        [Sg.Text('Nome da Loja')],
        [Sg.Input(key='nome_loja', size=(47, 5))],
        [Sg.Button('Cadastrar Loja', key='btnCadLoja', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cad_loja = Sg.Window('Cadastrar Loja', layout=layout_cadastrar_lojas, element_justification='c',
                         size=(1000, 600), margins=(0, 0), finalize=True)
    return cad_loja


def lojas_cadastradas():
    """Cria a janela para listar os lojas/cliente já cadastradas"""
    layout_ls_lojas = [
        [Sg.Listbox(values=[items for items in clientes_cadastrados.values()], key='clientes', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15))]
    ]
    ls_loja = Sg.Window('Lojas Cadastradas', layout=layout_ls_lojas, element_justification='c',
                        size=(1000, 600), margins=(0, 0), finalize=True)
    return ls_loja


def cadastrar_fornecedor():
    """Cria a janela para cadastrar os fornecedores"""
    layout_cadastrar_fornecedor = [
        [Sg.Text('Nome do Fornecedor')],
        [Sg.Input(key='nome_fornecedor', size=(20, 10))],
        [Sg.Button('Cadastrar Fornecedor', key='btnCadFornecedor', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cad_fornecedor = Sg.Window('Cadastrar um fornecedor', layout=layout_cadastrar_fornecedor, element_justification='c',
                               size=(1000, 600), margins=(0, 0), finalize=True)
    return cad_fornecedor


def mostrar_fornecedores():
    """"Cria a janela para listar os fornecedores cadastrados"""
    layout_mostrar_fornecedor = [
        [Sg.Text('Nome'), Sg.Text('Cidade'), Sg.Text('UF'), Sg.Text('Preço/KM')],
        [Sg.Listbox(values=[items for items in fornecedores_cadastrados.values()], key='fornecedores', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    ls_fornecedor = Sg.Window('Fornecedores Cadastrados', layout=layout_mostrar_fornecedor, element_justification='c',
                              size=(1000, 600), margins=(0, 0), finalize=True)
    return ls_fornecedor


def cadastrar_pedidos():
    """Cria a janela para selecionar a quantidade de produtos, fornecedores e clientes da consulta"""
    num_produtos = [[Sg.Text('')],
                    [Sg.Text('Digite a quantidade de produtos'),
                     Sg.Spin([j + 1 for j in range(len(produtos_cadastrados))], key='quantPro', size=(5, 1))],
                    [Sg.Text('Digite a quantidade de fornecedores'),
                     Sg.Spin([k + 1 for k in range(len(fornecedores_cadastrados))], key='quantFor', size=(5, 1))],
                    [Sg.Text('Digite a quantidade de clientes'),
                     Sg.Spin([l + 1 for l in range(len(clientes_cadastrados))], key='quantCli', size=(5, 1))],
                    [Sg.Button('Voltar', button_color='gray', pad=(0, 115)),
                     Sg.Button('Next', key='btnContPed', button_color='gray', pad=(0, 115))]]

    pedido = Sg.Window('Cadastrar Pedido', layout=num_produtos, element_justification='c',
                       size=(1000, 600), margins=(0, 0), finalize=True)
    return pedido


# Selecionar produtos
def selecionar_produtos(num_pro):
    """"Cria a janela para escolher os produtos para a consulta"""
    linhas = []
    for idx in range(num_pro):
        linhas.append([Sg.InputCombo(values=[items for items in produtos_cadastrados.values()],
                                     key='linha_pro{}'.format(idx), size=(50, 35))])

    layout_selec_prod = [
        [Sg.Text('')],
        *linhas,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20)),
         Sg.Button('Next', key='btnNextPro', button_color='gray', pad=(0, 115))]
    ]
    selec_prod = Sg.Window('Selecionar Produtos', layout=layout_selec_prod, element_justification='c',
                           size=(1000, 600), margins=(0, 0), finalize=True)
    return selec_prod


def seleciona_fornecedor(num_for):
    """"Cria a janela para escolher os fornecedores para a consulta"""
    linhas = []
    for idx in range(num_for):
        linhas.append([Sg.InputCombo(values=[items for items in fornecedores_cadastrados.values()],
                                     key='linha_for{}'.format(idx), size=(50, 35))])

    layout_selec_for = [
        [Sg.Text('')],
        *linhas,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15)),
         Sg.Button('Next', key='btnNextFor', button_color='gray', pad=(0, 15))]
    ]

    selec_for = Sg.Window('Selecionar Fornecedor', layout=layout_selec_for, element_justification='c',
                          size=(1000, 600), margins=(0, 0), finalize=True)
    return selec_for


# Selecionar clientes
def selecionar_clientes(num_cli):
    """"Cria a janela para escolher as lojas/clientes para a consulta"""
    linhas = []
    for idx in range(num_cli):
        linhas.append([Sg.InputCombo(values=[items for items in clientes_cadastrados.values()],
                                     key='linha_cli{}'.format(idx), size=(50, 35))])

    layout_selec_cliente = [
        [Sg.Text('')],
        *linhas,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20)),
         Sg.Button('Next', key='btnNextCli', button_color='gray', pad=(0, 20))]
    ]

    selec_cliente = Sg.Window('Selecionar Clientes', layout=layout_selec_cliente, element_justification='c',
                              size=(1000, 600), margins=(0, 0), finalize=True)
    return selec_cliente


def calcular_demanda(num_cli, num_pro):
    """Cria janela para inserir a demanda dos produtos por cliente"""
    linhas_demanda = []
    for idx_pro in range(num_pro):
        linhas_demanda.append([Sg.Text(produto_pesquisado[idx_pro])])
        linhas_demanda.append([Sg.Text('')])
        for idx_cli in range(num_cli):
            linhas_demanda.append([Sg.Text(cliente_pesquisado[idx_cli], size=(15, 0)),
                                   Sg.Input(key='demanda{}_{}'.format(idx_pro, idx_cli), size=(10, 10))])

    layout_calc_demanda = [
        [Sg.Text('')],
        *linhas_demanda,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15)),
         Sg.Button('Next', key='btnNextDemanda', button_color='gray', pad=(0, 15))]
    ]

    calc_demanda = Sg.Window('Cadastrar Demanda', layout=layout_calc_demanda, element_justification='c',
                             size=(1000, 600), margins=(0, 0), finalize=True)
    return calc_demanda


def calcular_oferta(num_for, num_pro):
    """Cria a janela para inserir a oferta dos produtos por fonecedores"""
    linhas_oferta = []

    for idx_pro in range(num_pro):
        linhas_oferta.append([Sg.Text('')])
        linhas_oferta.append([Sg.Text(produto_pesquisado[idx_pro])])
        linhas_oferta.append([Sg.Text('')])
        for idx_for in range(num_for):
            linhas_oferta.append([Sg.Text(fornecedor_pesquisado[idx_for], size=(15, 0)),
                                  Sg.Input(key='oferta{}_{}'.format(idx_pro, idx_for), size=(10, 10))])

    layout_calc_oferta = [
        [Sg.Text('')],
        *linhas_oferta,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15)),
         Sg.Button('Next', key='btnNextOferta', button_color='gray', pad=(0, 15))]
    ]

    calc_oferta = Sg.Window('Cadastrar Oferta', layout=layout_calc_oferta, element_justification='c',
                            size=(1000, 600), margins=(0, 0), finalize=True)
    return calc_oferta


def custo_produto(num_for, num_pro, num_cli):
    """Cria a janela para inserir o custo dos produtos de cada fabrica por cliente"""
    linhas_custo = []

    for idx_pro in range(num_pro):
        linhas_custo.append([Sg.Text(produto_pesquisado[idx_pro])]),
        for idx_cli in range(num_cli):
            linhas_custo.append([Sg.Text(cliente_pesquisado[idx_cli])]),
            for idx_for in range(num_for):
                linhas_custo.append([Sg.Text(fornecedor_pesquisado[idx_for]),
                                     Sg.Input(key='custo{}_{}_{}'.format(idx_pro, idx_for, idx_cli))])

    layout_calc_custo = [
        [Sg.Text('')],
        *linhas_custo,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15)),
         Sg.Button('Next', key='btnNextCusto', button_color='gray', pad=(0, 15))]
    ]

    calc_custo = Sg.Window('Cadastrar Custo', layout=layout_calc_custo, element_justification='c',
                           size=(1000, 810), margins=(0, 0), finalize=True)
    return calc_custo


def calcular_otimizacao():
    """Cria a janela para chamar a função de otimização"""
    valor = Backend.otimizacao(quantPro, quantFor, quantCli, custo, demanda, oferta)
    layout_calc_otimizacao = [
        [Sg.Text('')],
        [Sg.Text('Valor Otimizado: '), Sg.Text(valor)]
    ]

    calc_otimizacao = Sg.Window('Calcular Otimização', layout=layout_calc_otimizacao, element_justification='c',
                                size=(1000, 600), margins=(0, 0), finalize=True)
    return calc_otimizacao


def sobre():
    """Cria a janela para apresentar o time de desenvolvimento"""
    layout_sobre = [
        [Sg.Menu(menu_opt)],

        [Sg.Text('Grupo: Aguinele Queiroz')],
        [Sg.Text('Grupo: Brenda Orlandi')],
        [Sg.Text('Grupo: Túlio Cordeiro')],
        [Sg.Text('Grupo: Luis Otávio')],
        [Sg.Text('Grupo: Rafael Lucas')],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    sobre_tela = Sg.Window('Sobre...', layout=layout_sobre, element_justification='c',
                           size=(1000, 600), margins=(0, 0), finalize=True)
    return sobre_tela

""" Telas chamada na Home """
tela_inicio, registrar_produtos, listar_produtos, registrar_lojas, listar_lojas, registrar_fornecedores, \
listar_fornecedores, realizar_pedido, selecionar_n_produtos, selecionar_n_fornecedores, seleciona_n_clientes, \
inserir_demandas, inserir_ofertas, inserir_custos, calc_otimizacao, sobre_app = \
    home(), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

while True:
    """ Lê os dados inseridos, eventos e telas """
    telas, eventos, dados = Sg.read_all_windows()

    """Usuário fecha a janela no 'x'"""
    if eventos == Sg.WINDOW_CLOSED:
        break

    """Abre a janela de cadastro de produtos"""
    if eventos == 'Cadastrar Produtos':
        registrar_produtos = cadastrar_produtos()
        telas.hide()

    """Inserir os dados fornecidos na lista de Produtos"""
    if eventos == 'btnCadProduto':
        if dados['nome_produto'] != '':
            nome = dados['nome_produto']
            p = produtos_cadastrados[len(produtos_cadastrados)] = nome
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')

    """Abre a janela de listar produtos"""
    if eventos == 'Produtos Cadastrados':
        listar_produtos = mostrar_produtos()
        telas.hide()

    """Abre a janela de Cadastrar lojas"""
    if eventos == 'Cadastrar Lojas':
        # A ideia é que fossem armazenados numa lista de dicionários talvez
        registrar_lojas = cadastrar_loja()
        telas.hide()

    """Inserir os dados fornecidos na lista de Lojas"""
    if eventos == 'btnCadLoja':
        if dados['nome_loja'] != '':
            nome = dados['nome_loja']
            p = clientes_cadastrados[len(clientes_cadastrados)] = nome
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')

    """Abre a janela de listar lojas"""
    if eventos == 'Lojas Cadastradas':
        listar_lojas = lojas_cadastradas()
        telas.hide()

    """Abre a janela de cadastrar fornecedores"""
    if eventos == 'Cadastrar Fornecedores':
        registrar_fornecedores = cadastrar_fornecedor()
        telas.hide()

    """Inserir os dados fornecidos na lista de fornecedores"""
    if eventos == 'btnCadFornecedor':
        if dados['nome_fornecedor'] != '':
            nome = dados['nome_fornecedor']
            fornecedores_cadastrados[len(fornecedores_cadastrados)] = nome
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')

    """Abre a janela de listar fornecedores"""
    if eventos == 'Fornecedores Cadastrados':
        listar_fornecedores = mostrar_fornecedores()
        telas.hide()

    """Abre a janela de cadastrar pedido"""
    if eventos == 'Fazer Pedido':
        realizar_pedido = cadastrar_pedidos()
        telas.hide()

    """Insere os dados de quantidade de fornecedores, lojas e produtos em uma variável"""
    if eventos == 'btnContPed':
        quantFor = int(dados['quantFor'])
        quantCli = int(dados['quantCli'])
        quantPro = int(dados['quantPro'])
        selecionar_n_produtos = selecionar_produtos(quantPro)
        telas.hide()

    """Guarda os produtos selecionados pelo usuário em uma lista"""
    if eventos == 'btnNextPro':
        produto_pesquisado = []
        for i in range(quantPro):
            """Teste para não armazenar campos em branco ou produtos duplicados"""
            if dados['linha_pro{}'.format(i)] != '':
                if i > 0:
                    if dados['linha_pro{}'.format(i)] != dados['linha_pro{}'.format(i - 1)]:
                        produto_pesquisado.append(dados['linha_pro{}'.format(i)])
                    else:
                        Sg.popup('Produtos sao iguais', title='Mensagem')
                        break
                elif i == 0:
                    produto_pesquisado.append(dados['linha_pro{}'.format(i)])
            else:
                Sg.popup('Campo Vazio', title='Mensagem')
            if i == (quantPro - 1):
                selecionar_n_fornecedores = seleciona_fornecedor(quantFor)
                telas.hide()

    """Guarda os fornecedores selecionados pelo usuário em uma lista"""
    if eventos == 'btnNextFor':
        fornecedor_pesquisado = []
        for i in range(quantFor):
            """Teste para não armazenar campos em branco ou fornecedores duplicados"""
            if dados['linha_for{}'.format(i)] != '':
                if i > 0:
                    if dados['linha_for{}'.format(i)] != dados['linha_for{}'.format(i - 1)]:
                        fornecedor_pesquisado.append(dados['linha_for{}'.format(i)])
                    else:
                        Sg.popup('Fornecedores sao iguais', title='Mensagem')
                        break
                elif i == 0:
                    fornecedor_pesquisado.append(dados['linha_for{}'.format(i)])
            else:
                Sg.popup('Campo Vazio', title='Mensagem')
            if i == (quantFor - 1):
                seleciona_n_clientes = selecionar_clientes(quantCli)
                telas.hide()

    """Guarda os clientes selecionados pelo usuário em uma lista"""
    if eventos == 'btnNextCli':
        cliente_pesquisado = []
        for i in range(quantCli):
            """Teste para não armazenar campos em branco ou clientes duplicados"""
            if dados['linha_cli{}'.format(i)] != '':
                if i > 0:
                    if dados['linha_cli{}'.format(i)] != dados['linha_cli{}'.format(i - 1)]:
                        cliente_pesquisado.append(dados['linha_cli{}'.format(i)])
                    else:
                        Sg.popup('Clientes sao iguais', title='Mensagem')
                        break
                elif i == 0:
                    cliente_pesquisado.append(dados['linha_cli{}'.format(i)])
            else:
                Sg.popup('Campo Vazio', title='Mensagem')
            if i == (quantCli - 1):
                inserir_demandas = calcular_demanda(quantCli, quantPro)
                telas.hide()

    """Guarda em um dicionário as demandas de cada produto inseridos pelo usuário"""
    if eventos == 'btnNextDemanda':
        demanda = dict()
        for i in range(quantPro):
            for j in range(quantCli):
                if dados['demanda{}_{}'.format(i, j)] != '':
                    if dados['demanda{}_{}'.format(i, j)] >= '0':
                        demanda[i, j] = int(dados['demanda{}_{}'.format(i, j)])
                    else:
                        Sg.popup('Demanda com valor negativo', title='Mensagem')
                        break
                else:
                    Sg.popup('Campo Vazio', title='Mensagem')
                    demanda[i, j] = 0
                if i == (quantPro - 1) and j == (quantCli - 1):
                    inserir_ofertas = calcular_oferta(quantFor, quantPro)
                    telas.hide()

    """Guarda em um dicionário as ofertas de cada produto inseridos pelo usuário"""
    if eventos == 'btnNextOferta':
        oferta = dict()
        for i in range(quantPro):
            for j in range(quantFor):
                if dados['oferta{}_{}'.format(i, j)] != '':
                    if dados['oferta{}_{}'.format(i, j)] >= '0':
                        oferta[i, j] = int(dados['oferta{}_{}'.format(i, j)])
                    else:
                        Sg.popup('Oferta com valor negativo', title='Mensagem')
                        break
                else:
                    Sg.popup('Campo Vazio', title='Mensagem')
                    oferta[i, j] = 0
                if i == (quantPro - 1) and j == (quantFor - 1):
                    inserir_custos = custo_produto(quantFor, quantPro, quantCli)
                    telas.hide()

    """Guarda em um dicionário os custos de cada produto inseridos pelo usuário"""
    if eventos == 'btnNextCusto':
        custo = dict()
        for i in range(quantPro):
            for j in range(quantFor):
                for k in range(quantCli):
                    if dados['custo{}_{}_{}'.format(i, j, k)] != '':
                        if dados['custo{}_{}_{}'.format(i, j, k)] >= '0':
                            custo[i, j, k] = float(dados['custo{}_{}_{}'.format(i, j, k)])
                        else:
                            Sg.popup('Custo com valor negativo', title='Mensagem')
                            break
                    else:
                        Sg.popup('Campo Vazio', title='Mensagem')
                        custo[i, j, k] = 0.0
                    if i == (quantPro - 1) and j == (quantFor - 1) and k == (quantCli - 1):
                        calc_otimizacao = calcular_otimizacao()
                        telas.hide()

    """Abre a janela de QUem Somos"""
    if eventos == 'Quem Somos':
        sobre_app = sobre()
        telas.hide()

        """Volta para a janela Home"""
    elif telas and eventos == 'Voltar':
        telas.hide()
        tela_inicio.un_hide()

        """Finaliza o sistema"""
    elif telas and eventos == 'Sair':
        telas.close()
        sys.exit()
