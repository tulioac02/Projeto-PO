import PySimpleGUI as Sg
import Produtos

Sg.theme('DefaultNoMoreNagging')

menu_opt = [['&Produtos', ['Cadastrar Produtos', 'Produtos Cadastrados']],
            ['&Lojas', ['Cadastrar Lojas', 'Lojas Cadastradas']],
            ['&Fornecedores', ['Cadastrar Fornecedores', 'Fornecedores Cadastrados']],
            ['&Calcular Pedido'],
            ['&Sobre']
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
        [Sg.Menu(menu_opt)],
        [Sg.Text('Nome do Produto')],
        [Sg.Input(key='nome_produto', size=(47, 5))],
        [Sg.Text('Detalhes')],
        [Sg.Multiline(key='detalhes', size=(45, 3))],
        [Sg.Button('Cadastrar', button_color='gray', pad=(0, 15))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 45))]
    ]
    cadastrar_pd = Sg.Window('Cadastrar Produtos', layout=layout_cadastrar_produtos, element_justification='c',
                             size=(800, 400), margins=(0, 0), finalize=True)
    return cadastrar_pd


def mostrar_produtos(ls_prod):
    layout_mostrar_produtos = [
        [Sg.Menu(menu_opt)],
        [Sg.Listbox(values=[items for items in ls_prod], key='produtos', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
    ]
    mostrar_pd = Sg.Window('Lista de Produtos', layout=layout_mostrar_produtos, element_justification='c',
                           size=(800, 400), margins=(0, 0), finalize=True)
    return mostrar_pd


def cadastrar_loja():
    layout_cadastrar_lojas = [
        [Sg.Menu(menu_opt)],
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
        [Sg.Menu(menu_opt)],
        [Sg.Listbox(values=[], key='nome_loja', size=(100, 25))],
        [Sg.Button('Voltar', button_color='gray', pad=(0, 15))]
    ]
    ls_loja = Sg.Window('Lojas Cadastradas', layout=layout_ls_lojas, element_justification='c',
                        size=(800, 400), margins=(0, 0), finalize=True)
    return ls_loja


tela_inicio, tela_cad_produto, tela_mostrar_pd, tela_cad_loja, tela_ls_loja = home(), None, None, None, None

produtos = list()
clientes = list()
while True:
    telas, eventos, dados = Sg.read_all_windows()
    # usuário fecha a janela no "x"
    if telas == tela_inicio and eventos == Sg.WINDOW_CLOSED:
        break

    # Em Inicio clicar em cadastrar produtos
    if telas == tela_inicio and eventos == 'Cadastrar Produtos':
        tela_cad_produto = cadastrar_produtos()
        tela_inicio.hide()

    if telas == tela_cad_produto and eventos == 'Cadastrar':
        if dados['nome_produto'] != '':
            nome = dados['nome_produto']
            p = Produtos.Produtos(nome)
            Produtos.listProdutos.append(p)
            # Sg.popup_quick_message(Produtos.listProdutos.__repr__())
        else:
            Sg.popup('Nome do produto em branco!')

    # Em Inicio clicar em mostrar produtos
    elif telas == tela_inicio and eventos == 'Produtos Cadastrados':
        tela_mostrar_pd = mostrar_produtos(produtos)
        tela_inicio.hide()

    # Em Inicio clicar em Cadastrar Lojas
    elif telas == tela_inicio and eventos == 'Cadastrar Lojas':
        # A ideia é que fossem armazenados numa lista de dicionários talvez
        tela_cad_loja = cadastrar_loja()
        tela_inicio.hide()

    # Em Inicio clicar em Lojas Cadastradas
    elif telas == tela_inicio and eventos == 'Lojas Cadastradas':
        tela_ls_loja = lojas_cadastradas()
        tela_inicio.hide()

    # produtos cadastrados para mostrar produtos e vice versa
    elif telas == tela_cad_produto and eventos == 'Produtos Cadastrados':
        tela_mostrar_pd.un_hide()
        tela_cad_produto.hide()

    elif telas == tela_mostrar_pd and eventos == 'Cadastrar Produtos':
        tela_cad_produto.un_hide()
        tela_mostrar_pd.hide()

    # De Cadastrar Lojas ir para lojas cadastradas
    elif telas == tela_cad_loja and eventos == 'Lojas Cadastradas':
        tela_ls_loja = lojas_cadastradas()
        tela_cad_loja.un_hide()

    elif telas == tela_ls_loja and eventos == 'Cadastrar Lojas':
        tela_cad_loja = cadastrar_loja()
        tela_ls_loja.un_hide()

    # Em Inicio clicar em mostrar produtos
    elif telas and eventos == 'Voltar':
        telas.hide()
        tela_inicio.un_hide()

    # Em Inicio clicar em sair
    elif telas == tela_inicio and eventos == 'Sair':
        tela_inicio.close()
