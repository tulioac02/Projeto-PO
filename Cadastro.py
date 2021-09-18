from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

menu_def = [['&Produtos', ['&Cadastrar', '&Listar']],
            ['&Fornecedores', ['&Cadastrar', '&Listar']],
            ['&Lojas', ['&Cadastrar', '&Listar']],
            ['&Sobre']]


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Menu(menu_def)],
            [sg.Text('Nome', size=(8, 0)), sg.Input(key='nome', size=(15, 0))],
            [sg.Text('Descrição'), sg.Input(key='descricao', password_char='*')],
            [sg.Button('Voltar'), sg.Button('Cadastrar')],
        ]
        self.janela = sg.Window('Cadastrar Produtos').layout(layout)

    def Iniciar(self):
        while True:
            button, values = self.janela.Read()
            nome = self.values['usuario']
            senha = self.values['senha']
            print(f'nome: {nome}')
            print(f'senha: {senha}')


tela = TelaPython()
tela.Iniciar()
