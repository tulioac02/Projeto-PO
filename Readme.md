# Pesquisa Operacional: Otimização
## Problema do Transporte

### Introdução
Este Projeto buscou alcançar uma solução ótima para um problema de programação linear de transportes. No qual a função objetivo era minimizar os custos com os frete de cada produto. Dadas as demandas de cada loja, ofertas das fábricas e preços de frete embutidos no preço total do produto.
### Tecnologias
* [Python](https://www.python.org/) : Linguagem de Programação.
* [Pycharm](https://www.jetbrains.com/pt-br/pycharm/): IDE para desenvolvimento com Python
* [Anaconda](https://www.anaconda.com/): Gerenciador de  Distribuições Python,Ambientes de Trabalho e Módulos.
* [Gurobi](https://www.gurobi.com/) : Solver de Otimização comercial para programação linear.
* [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) : Pacote Python para desenvolvimento de GUIs
* [Ubuntu](https://ubuntu.com/) : Distribuição Linux

 ### Requisitos

* Ter instalado Python na versão 3.8 ou superior. O projeto foi desenvolvido usando a versão 3.8, versões anteriores pode não funcionar corretamente;
* Ter instalado Gurobi 9.1.2;
* Ter instalado Pycharm 2020.3;
* Ter instalado PySimpleGUI 4.47.0;
* Ter instalado Anaconda 3;

### Dados de Entrada

* Quantidade de Produtos ;
* Quantidade de Fornecedores
* Quantidade de Clientes;
* Dicionário de demandas;
* Dicionário de Ofertas;
* Dicionário de custos;
* lista de produtos;
* lista de Lojas;
* lista de Fabricas;

  #### Exemplo
  ``` py
  produtos_cadastrados = {0: 'Telha1', 1: 'Telha2', 2: 'Telha3'}
  clientes_cadastrados = {0: 'Minas Novas', 1: 'Turmalina'}
  fabricas_cadastradas = {0: 'Precom', 1: 'Brasilit', 2: 'Imbralit'}
  ```
### Solução Implementada 

* Modelagem matemática do problema:
  Modelo de Programação Linear
  
* Utilização do Solver Gurobi:

  #### Exemplo
  ``` py
  # Função Objetivo
  m.setObjective(gp.quicksum(x[i, j, k] * total[i, j, k] for i in produtos for j in fabricas for k in clientes),
                 sense=gp.GRB.MINIMIZE)
  ```
* Utilização do PySimpleGUI para criação da Interface Gráfica:

  #### Exemplo
    ```py
    def mostrar_produtos():
        layout_mostrar_produtos = [
            [Sg.Listbox(values=[items for items in produtos_cadastrados.values()], key='produtos', size=(100, 25))],
            [Sg.Button('Voltar', button_color='gray', pad=(0, 20))]
        ]
        mostrar_pd = Sg.Window('Lista de Produtos', layout=layout_mostrar_produtos, element_justification='c',
                               size=(1000, 600), margins=(0, 0), finalize=True)
        return mostrar_pd
    ``` 
    ![Captura de tela de 2021-09-20 22-24-35](https://user-images.githubusercontent.com/66737248/134098443-70712800-5e6d-4114-b3ab-bb158b7962f1.png)

### Solução Ótima obtida:

![WhatsApp Image 2021-09-20 at 20 08 33](https://user-images.githubusercontent.com/66737248/134099103-52ebca0d-5fdf-411b-8195-2b6a50973c18.jpeg)

### AUTOR:
    Aguinele Queiroz da Silva
    Brenda Orlandi
    Luiz Otávio
    Rafael Lucas
    Túlio Alves Cordeiro
