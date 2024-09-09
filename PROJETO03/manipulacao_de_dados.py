###################### PROJETO 03 ##############################

#  --------- Bibliotecas usadas ---------

#    - pandas - openpyxl - plotly - nbformat


#  - Carregando os dados do Excel

import pandas as pd

dados = pd.read_excel('vendas.xlsx')

#  - Análises exploratórias

# visualizando as primeiras linhas
dados.head()

print()

# visualizando as últimas linhas
dados.tail()

# formato da tabela de dados (linhas, colunas)
dados.shape

# visualizando informações das colunas
dados.info()

# selecionando colunas
dados[['cidade', 'estado']]

#  - Estatisticas

dados.describe()
print(dados.describe())

#  - Análises

# contagem de vendas por loja
dados['loja'].value_counts()
print(dados['loja'].value_counts())

# contagem de vendas por cidade
dados['cidade'].value_counts()
print(dados['cidade'].value_counts())

# contagem de formas de pagamento
dados['forma_pagamento'].value_counts()
print(dados['forma_pagamento'].value_counts())

#  - Agrupando dados

# faturamento por loja
dados.groupby('loja')['preco'].sum().to_frame
print(dados.groupby('loja')['preco'].sum().to_frame)

# faturamento por forma de pagamento
dados.groupby('forma_pagamento')['preco'].sum().to_frame()
print(dados.groupby('forma_pagamento')['preco'].sum().to_frame())

# faturamento
dados.groupby(['estado', 'cidade', 'loja'])['preco'].sum().to_frame
print(dados.groupby(['estado', 'cidade', 'loja'])['preco'].sum().to_frame)

# enviando relatório para excel
dados_agrupados = dados.groupby(['estado', 'cidade', 'loja', 'forma_pagamento'])['preco'].sum().to_frame()
dados_agrupados.to_excel('Faturamento.xlsx')

#  - Visualização de dados

import plotly.express as px

# Apresentação de gráfico
grafico = px.histogram(dados, x='loja',
             y='preco',
             text_auto=True,
             title='Faturamento',
             color='forma_pagamento')
grafico.show()
grafico.write_html('Faturamento.html')

#  - Listas e o comando for

lista_colunas = ['loja', 'cidade', 'estado', 'tamanho', 'local_consumo']

for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna,
             y='preco',
             text_auto=True,
             title='Faturamento',
             color='forma_pagamento')
    grafico.show()
    grafico.write_html(f'Faturamento-{coluna}.html')
