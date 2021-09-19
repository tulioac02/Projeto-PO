import PySimpleGUI as Sg
import Produtos, Fornecedores

# Telas de Cadastro de Produtos
# Telas para Mostrar Produtos
# Telas de Cadastro de Lojas
# Telas para Mostrar Lojas
# Telas de Cadastro de fornecedores
# Telas para mostrar fornecedores
# Telas de Calcular pedido
# Telas para mostrar resultado do calculo

Sg.theme('DefaultNoMoreNagging')

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
        [Sg.Text('Detalhes')],
        [Sg.Multiline(key='detalhes', size=(45, 3))],
        [Sg.Button('Cadastrar', key='btnCadProduto', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cadastrar_pd = Sg.Window('Cadastrar Produtos', layout=layout_cadastrar_produtos, element_justification='c',
                             size=(800, 400), margins=(0, 0), finalize=True)
    return cadastrar_pd


def mostrar_produtos(ls_prod):
    layout_mostrar_produtos = [
        [Sg.Listbox(values=[items for items in ls_prod], key='produtos', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    mostrar_pd = Sg.Window('Lista de Produtos', layout=layout_mostrar_produtos, element_justification='c',
                           size=(800, 400), margins=(0, 0), finalize=True)
    return mostrar_pd


def cadastrar_loja():
    layout_cadastrar_lojas = [
        [Sg.Text('Nome da Loja')],
        [Sg.Input(key='nome_loja', size=(47, 5))],
        [Sg.Text('Cidade'), Sg.Text('UF')],
        [Sg.Input(key='cidade', size=(41, 5)), Sg.Input(key='uf', size=(4, 5))],
        [Sg.Text('Longitude')],
        [Sg.Input(key='long', size=(47, 5))],
        [Sg.Text('Latitude'), Sg.Text('UF')],
        [Sg.Input(key='lat', size=(47, 5))],
        [Sg.Button('Cadastrar Loja', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cad_loja = Sg.Window('Cadastrar uma Loja', layout=layout_cadastrar_lojas, element_justification='c',
                         size=(800, 400), margins=(0, 0), finalize=True)
    return cad_loja


def lojas_cadastradas():
    layout_ls_lojas = [
        [Sg.Listbox(values=[], key='nome_loja', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15))]
    ]
    ls_loja = Sg.Window('Lojas Cadastradas', layout=layout_ls_lojas, element_justification='c',
                        size=(800, 400), margins=(0, 0), finalize=True)
    return ls_loja


def cadastrar_fornecedor():
    layout_cadastrar_fornecedor = [

        [Sg.Text('Nome do Fornecedor'), Sg.Text('Cidade'), Sg.Text('UF')],
        [Sg.Input(key='nome_fornecedor', size=(20, 10)),
         Sg.Input(key='cidade', size=(20, 10)), Sg.Input(key='uf', size=(5, 10))],

        [Sg.Text('Frete')],
        [Sg.Input(key='frete', size=(5, 10))],

        [Sg.Button('Cadastrar Fornecedor', key='btnCadFornecedor', button_color='gray', pad=(0, 15))],

        [Sg.Text('Nome do Produto'), Sg.Text('Preço Produto'), Sg.Text('Oferta')],
        [Sg.Input(key='nome_produto', size=(30, 10)), Sg.Input(key='preço_produto', size=(10, 10)),
         Sg.Input(key='oferta', size=(5, 5))],

        [Sg.Button('Cadastrar Oferta', key='btnCadOferta', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cad_fornecedor = Sg.Window('Cadastrar um fornecedor', layout=layout_cadastrar_fornecedor, element_justification='c',
                               size=(800, 400), margins=(0, 0), finalize=True)
    return cad_fornecedor


def mostrar_fornecedores():
    layout_mostrar_fornecedor = [
        [Sg.Text('Nome'), Sg.Text('Cidade'), Sg.Text('UF'), Sg.Text('Preço/KM')],
        [Sg.Listbox(values=[items for items in Fornecedores.listFornecedores], key='fornecedor', size=(80, 20))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    ls_fornecedor = Sg.Window('Fornecedores Cadastrados', layout=layout_mostrar_fornecedor, element_justification='c',
                              size=(800, 400), margins=(0, 0), finalize=True)
    return ls_fornecedor


num_linhas = 1


def cadastrar_pedidos():
    layout_linha = [Sg.InputCombo(values=Produtos.listProdutos, key='nome_produto', size=(20, 10)),
                    Sg.Input(key='nome_fornecedor', size=(25, 10)),
                    Sg.Input(key='demandas', size=(2, 10))],
    layout_pedido = [
        [Sg.Text('Produto'), Sg.Text('Fornecedor'), Sg.Text('Demanda')],
        layout_linha,
        [Sg.Button('Adicionar', button_color='gray', pad=(0, 115)),
         Sg.Button('Finalizar Pedido', button_color='gray', pad=(0, 115)),
         Sg.Button('Voltar', button_color='gray', pad=(0, 115))]
    ]
    pedido = Sg.Window('Cadastrar Pedido', layout=layout_pedido, element_justification='c',
                       size=(800, 400), margins=(0, 0), finalize=True)
    return pedido


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
            p = Produtos.Produtos(nome)
            Produtos.listProdutos.append(p)
            Sg.popup('Cadastrado com sucesso', title='Mensagem')
        else:
            Sg.popup('Nome do produto em branco!', title='Mensagem')


    # Em Inicio clicar em mostrar produtos
    if eventos == 'Produtos Cadastrados':
        tela_mostrar_pd = mostrar_produtos(Produtos.listProdutos)
        tela_inicio.hide()

    # Em Inicio clicar em Cadastrar Lojas
    if eventos == 'Cadastrar Lojas':
        # A ideia é que fossem armazenados numa lista de dicionários talvez
        tela_cad_loja = cadastrar_loja()
        tela_inicio.hide()

    # Em Inicio clicar em Lojas Cadastradas
    if eventos == 'Lojas Cadastradas':
        tela_ls_loja = lojas_cadastradas()
        tela_inicio.hide()

    # Em Inicio clicar em Cadastrar Fornecedor
    if eventos == 'Cadastrar Fornecedores':
        tela_cad_fornecedor = cadastrar_fornecedor()
        tela_inicio.hide()

    if eventos == 'btnCadFornecedor':
        if dados['nome_fornecedor'] != '' and dados['cidade'] != '' and dados['frete'] != '':
            nome = dados['nome_fornecedor']
            cidade = dados['cidade']
            UF = dados['uf']
            frete = dados['frete']
            p = Fornecedores.Fornecedores(nome, cidade, UF, frete)
            Fornecedores.listFornecedores.append(p)
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
    if eventos == 'Finalizar Pedido':
        tela_calculo = calcular_pedido()
        telas.hide()



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
