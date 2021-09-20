import PySimpleGUI as Sg

# Telas de Cadastro de Produtos
# Telas para Mostrar Produtos
# Telas de Cadastro de Lojas
# Telas para Mostrar Lojas
# Telas de Cadastro de fornecedores
# Telas para mostrar fornecedores
# Telas de Calcular pedido
# Telas para mostrar resultado do calculo

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

menu_opt = [['&Produtos', ['Cadastrar Produtos', 'Produtos Cadastrados']],
            ['&Lojas', ['Cadastrar Lojas', 'Lojas Cadastradas']],
            ['&Fornecedores', ['Cadastrar Fornecedores', 'Fornecedores Cadastrados']],
            ['&Orçamentos', ['Fazer Pedido']],
            ['&Sobre', ['Quem Somos']]
            ]


def home():
    layout_home = [
        [Sg.Menu(menu_opt)],
        [Sg.Text('Bem Vindo!', auto_size_text=True, pad=(0, 150))],
        [Sg.Button('Sair', button_color='gray', pad=(0, 30))]
    ]
    my_home = Sg.Window('Inicio', layout=layout_home, element_justification='c',
                        size=(800, 400), margins=(0, 0), finalize=True)
    return my_home


def cadastrar_produtos():
    layout_cadastrar_produtos = [
        [Sg.Text('Nome do Produto')],
        [Sg.Input(key='nome_produto', size=(47, 5))],
        [Sg.Button('Cadastrar', key='btnCadProduto', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cadastrar_pd = Sg.Window('Cadastrar Produtos', layout=layout_cadastrar_produtos, element_justification='c',
                             size=(800, 400), margins=(0, 0), finalize=True)
    return cadastrar_pd


def mostrar_produtos():
    layout_mostrar_produtos = [
        [Sg.Listbox(values=[items for items in produtos_cadastrados.values()], key='produtos', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    mostrar_pd = Sg.Window('Lista de Produtos', layout=layout_mostrar_produtos, element_justification='c',
                           size=(800, 400), margins=(0, 0), finalize=True)
    return mostrar_pd


def cadastrar_loja():
    layout_cadastrar_lojas = [
        [Sg.Text('Nome da Loja')],
        [Sg.Input(key='nome_loja', size=(47, 5))],
        [Sg.Button('Cadastrar Loja', key='btnCadLoja', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cad_loja = Sg.Window('Cadastrar Loja', layout=layout_cadastrar_lojas, element_justification='c',
                         size=(800, 400), margins=(0, 0), finalize=True)
    return cad_loja


def lojas_cadastradas():
    layout_ls_lojas = [
        [Sg.Listbox(values=[items for items in clientes_cadastrados.values()], key='clientes', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15))]
    ]
    ls_loja = Sg.Window('Lojas Cadastradas', layout=layout_ls_lojas, element_justification='c',
                        size=(800, 400), margins=(0, 0), finalize=True)
    return ls_loja


def cadastrar_fornecedor():
    layout_cadastrar_fornecedor = [

        [Sg.Text('Nome do Fornecedor')],
        [Sg.Input(key='nome_fornecedor', size=(20, 10))],
        [Sg.Button('Cadastrar Fornecedor', key='btnCadFornecedor', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cad_fornecedor = Sg.Window('Cadastrar um fornecedor', layout=layout_cadastrar_fornecedor, element_justification='c',
                               size=(800, 400), margins=(0, 0), finalize=True)
    return cad_fornecedor


def mostrar_fornecedores():
    layout_mostrar_fornecedor = [
        [Sg.Text('Nome'), Sg.Text('Cidade'), Sg.Text('UF'), Sg.Text('Preço/KM')],
        [Sg.Listbox(values=[items for items in fornecedores_cadastrados.values()], key='fornecedores', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    ls_fornecedor = Sg.Window('Fornecedores Cadastrados', layout=layout_mostrar_fornecedor, element_justification='c',
                              size=(800, 400), margins=(0, 0), finalize=True)
    return ls_fornecedor


def cadastrar_pedidos():
    num_produtos = [[Sg.Text('')],
                    [Sg.Text('Digite a quantidade de produtos'),
                     Sg.Spin([j + 1 for j in range(len(produtos_cadastrados))], key='quantPro', size=(5, 1))],
                    [Sg.Text('Digite a quantidade de fornecedores'),
                     Sg.Spin([k + 1 for k in range(len(fornecedores_cadastrados))], key='quantFor', size=(5, 1))],
                    [Sg.Text('Digite a quantidade de clientes'),
                     Sg.Spin([l + 1 for l in range(len(clientes_cadastrados))], key='quantCli', size=(5, 1))],
                    [Sg.Button('Voltar', button_color='gray', pad=(0, 115)),
                     Sg.Button('Continuar', key='btnContPed', button_color='gray', pad=(0, 115))]]

    pedido = Sg.Window('Cadastrar Pedido', layout=num_produtos, element_justification='c',
                       size=(800, 400), margins=(0, 0), finalize=True)
    return pedido


def seleciona_fornecedor(num_for):
    linhas = []
    for idx in range(num_for):
        linhas.append([Sg.InputCombo(values=[items for items in fornecedores_cadastrados.values()],
                                     key='linha_for{}'.format(idx), size=(50, 35))])

    layout_selec_for = [
        [Sg.Text('')],
        *linhas,
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))],
        [Sg.Button('Finalizar Pedido', key='btnFinalFor', button_color='gray', pad=(0, 20))]
    ]

    selec_for = Sg.Window('Selecionar Fornecedor', layout=layout_selec_for, element_justification='c',
                          size=(800, 400), margins=(0, 0), finalize=True)
    return selec_for


def calcular_pedido():
    layout_calc_pedido = [

        [Sg.Input('Origem', size=(37, 10), justification='c'),
         Sg.Input('Destino', size=(40, 10), justification='c'),
         Sg.Input('Custo/Origem', size=(37, 10), justification='c')],

        [Sg.Input('Produto1', size=(20, 10), justification='c'),
         Sg.Input('Produto2', size=(20, 10), justification='c'),
         Sg.Input('Produto3', size=(20, 10), justification='c')],

        [Sg.Input('Fabrica1', size=(20, 10), justification='c'),
         Sg.Input('', size=(20, 10)), Sg.Input('', size=(20, 10)), Sg.Input('', size=(20, 10)),
         Sg.Input('', size=(20, 10))],

        [Sg.Input('Fabrica2', size=(20, 10), justification='c'),
         Sg.Input('', size=(20, 10)), Sg.Input('', size=(20, 10)), Sg.Input('', size=(20, 10)),
         Sg.Input('', size=(20, 10))],

        [Sg.Input('Fabrica3', size=(20, 10), justification='c'),
         Sg.Input('', size=(20, 10)), Sg.Input('', size=(20, 10)), Sg.Input('', size=(20, 10)),
         Sg.Input('', size=(20, 10))],

        [Sg.Button('Novo Calculo', button_color='gray', pad=(0, 100))],
        [Sg.Button('Sair', button_color='gray', pad=(0, 20))]
    ]
    calc_pedido = Sg.Window('Cadastrar Pedido', layout=layout_calc_pedido, element_justification='c',
                            size=(800, 400), margins=(0, 0), finalize=True)
    return calc_pedido


def sobre():
    layout_sobre = [
        [Sg.Menu(menu_opt)],

        [Sg.Text('Grupo: Aguinele Queiroz')],
        [Sg.Text('Grupo: Brenda Orlandi')],
        [Sg.Text('Grupo: Túlio Cordeiro')],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    sobre_tela = Sg.Window('Sobre...', layout=layout_sobre, element_justification='c',
                           size=(800, 400), margins=(0, 0), finalize=True)
    return sobre_tela


tela_inicio, tela_cad_produto, tela_ls_pd, tela_cad_loja, tela_ls_loja, tela_cad_fornecedor, tela_ls_fornecedor, \
tela_pedido, tela_calculo, tela_sobre = home(), None, None, None, None, None, None, None, None, None

produtos = list()
clientes = list()

while True:
    telas, eventos, dados = Sg.read_all_windows()
    # usuário fecha a janela no "x"
    if eventos == Sg.WINDOW_CLOSED:
        break

    # cadastro de produtos
    if eventos == 'Cadastrar Produtos':
        tela_cad_produto = cadastrar_produtos()
        tela_inicio.hide()

    if eventos == 'btnCadProduto':
        if dados['nome_produto'] != '':
            nome = dados['nome_produto']
            p = produtos_cadastrados[len(produtos_cadastrados)] = nome
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')

    # Em Inicio clicar em mostrar produtos
    if eventos == 'Produtos Cadastrados':
        tela_mostrar_pd = mostrar_produtos()
        tela_inicio.hide()

    # Em Inicio clicar em Cadastrar Lojas
    if eventos == 'Cadastrar Lojas':
        # A ideia é que fossem armazenados numa lista de dicionários talvez
        tela_cad_loja = cadastrar_loja()
        tela_inicio.hide()

    if eventos == 'btnCadLoja':
        if dados['nome_loja'] != '':
            nome = dados['nome_loja']
            p = clientes_cadastrados[len(clientes_cadastrados)] = nome
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')

    # Em Inicio clicar em Lojas Cadastradas
    if eventos == 'Lojas Cadastradas':
        tela_ls_loja = lojas_cadastradas()
        tela_inicio.hide()

    # Em Inicio clicar em Cadastrar Fornecedor
    if eventos == 'Cadastrar Fornecedores':
        tela_cad_fornecedor = cadastrar_fornecedor()
        tela_inicio.hide()

    if eventos == 'btnCadFornecedor':
        if dados['nome_fornecedor'] != '':
            nome = dados['nome_fornecedor']
            p = fornecedores_cadastrados[len(fornecedores_cadastrados)] = nome
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')

    # Em Inicio clicar em  Fornecedores Cadastrados
    if eventos == 'Fornecedores Cadastrados':
        tela_ls_fornecedor = mostrar_fornecedores()
        tela_inicio.hide()

    if eventos == 'Fazer Pedido':
        tela_pedido = cadastrar_pedidos()
        telas.hide()

    # Em Inicio clicar em  Fornecedores Cadastrados
    if eventos == 'btnContPed':
        quantFor = dados['quantFor']
        tela_selec_fornecedor = seleciona_fornecedor(quantFor)
        telas.hide()

    if eventos == 'btnFinalFor':
        fornecedor_pesquisado = []
        for i in range(quantFor):
            if i > 0:
                if dados['linha_for{}'.format(i)] != dados['linha_for{}'.format(i - 1)]:
                    fornecedor_pesquisado.append(dados['linha_for{}'.format(i)])
                else:
                    Sg.popup('Fornecedores sao iguais', title='Mensagem')
                    break
            elif i == 0:
                fornecedor_pesquisado.append(dados['linha_for{}'.format(i)])
            if i == (quantFor - 1):
                Sg.popup('Fornecedores Selecionados', title='Mensagem')
                Sg.popup_quick_message(fornecedor_pesquisado)


    if eventos == 'Quem Somos':
        tela_sobre = sobre()
        telas.hide()

    # # produtos cadastrados para mostrar produtos e vice versa
    # elif telas == tela_cad_produto and eventos == 'Produtos Cadastrados':
    #     tela_ls_pd = mostrar_produtos(produtos)
    #     tela_cad_produto.hide()
    #
    # elif telas == tela_ls_pd and eventos == 'Cadastrar Produtos':
    #     tela_cad_produto.un_hide()
    #     tela_ls_pd.hide()
    #
    # # De Cadastrar Lojas ir para lojas cadastradas  e vice versa
    # elif telas == tela_cad_loja and eventos == 'Lojas Cadastradas':
    #     tela_ls_loja = lojas_cadastradas()
    #     tela_cad_loja.un_hide()
    #
    # elif telas == tela_ls_loja and eventos == 'Cadastrar Lojas':
    #     tela_cad_loja = cadastrar_loja()
    #     tela_ls_loja.un_hide()
    #
    # # Em Cadastrar Fornecedores ir Fornecedores cadastrados e vice versa
    # elif telas == tela_cad_fornecedor and eventos == 'Fornecedores Cadastrados':
    #     tela_ls_fornecedor = mostrar_fornecedores()
    #     tela_cad_fornecedor.hide()
    #
    # elif telas == tela_ls_fornecedor and eventos == 'Cadastrar Fornecedores':
    #     tela_cad_fornecedor = cadastrar_fornecedor()
    #     tela_ls_fornecedor.hide()
    #
    # elif telas == tela_calculo and eventos == 'Novo Calculo':
    #     tela_pedido.un_hide()
    #     tela_calculo.hide()
    #
    # # De uma guia para outra
    # elif telas and eventos == 'Cadastrar Produtos':
    #     tela_cad_produto = cadastrar_produtos()
    #     telas.hide()
    #
    # elif telas and eventos == 'Produtos Cadastrados':
    #     tela_ls_produto = mostrar_produtos(produtos)
    #     telas.hide()
    #
    # elif telas and eventos == 'Cadastrar Lojas':
    #     tela_cad_loja = cadastrar_loja()
    #     telas.hide()
    #
    # elif telas and eventos == 'Lojas Cadastradas':
    #     tela_ls_loja = lojas_cadastradas()
    #     telas.hide()
    #
    # elif telas and eventos == 'Cadastrar Fornecedores':
    #     tela_cad_fornecedor = cadastrar_fornecedor()
    #     telas.hide()
    #
    # elif telas and eventos == 'Fornecedores Cadastrados':
    #     tela_ls_fornecedor = mostrar_fornecedores()
    #     telas.hide()
    #
    # elif telas and eventos == 'Fazer Pedido':
    #     tela_pedido = cadastrar_pedidos()
    #     telas.hide()
    #
    # elif telas and eventos == 'Quem Somos':
    #     tela_sobre = sobre()
    #     telas.hide()
    #
    # Em Inicio clicar em mostrar produtos
    elif telas and eventos == 'Voltar':
        telas.hide()
        tela_inicio.un_hide()

    # Em Inicio clicar em sair
    elif telas and eventos == 'Sair':
        telas.close()
