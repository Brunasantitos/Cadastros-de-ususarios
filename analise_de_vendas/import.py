import os
import pandas as pd

lista_arquivo = os.listdir("/content/drive/MyDrive/Curso Básico de Python/Vendas")
display(lista_arquivo)

tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
  # se tem "Vendas" no nome do arquivo, então
  if "Vendas" in arquivo:
    # importar o arquivo
    tabela = pd.read_csv(f"/content/drive/MyDrive/Curso Básico de Python/Vendas/{arquivo}")
    tabela_total = tabela_total.append(tabela)

# Passo 3 - Tratar / Compilar as bases de dados
display(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
display(tabela_produtos)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
display(tabela_lojas)

import plotly.express as px

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()