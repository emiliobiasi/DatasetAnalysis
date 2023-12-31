import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import squarify


dataframe = pd.read_csv(r'C:/PROJECTS/TAREFAS FACUL/DatasetAnalysis/vgsales.csv')

print(dataframe)

# Selecionar apenas as colunas desejadas
name_platform_global = dataframe.loc[:, ['Name', 'Platform', 'Global_Sales']]

# Exibir a nova tabela
print("\n\nTabela Filtrada: Name | Plataform | Global_Sales\n")
print(name_platform_global)

# Agrupar por título do jogo e somar as vendas globais
nova_tabela_agrupada = name_platform_global.groupby('Name').agg({'Platform': 'count', 'Global_Sales': 'sum'}).reset_index()
# Ordenar a tabela pela quantidade de vendas globais em ordem decrescente
nova_tabela_agrupada = nova_tabela_agrupada.sort_values(by='Global_Sales', ascending=False)
# Exibir a tabela ordenada
print("\n\nTabela Filtrada Agrupada em Ordem: Name | Plataform (em número) | Global_Sales (acumulado)\n")
print(nova_tabela_agrupada)

# Calcular a correlação e p-value
correlacao, p_value = pearsonr(nova_tabela_agrupada['Platform'], nova_tabela_agrupada['Global_Sales'])

# Exibir os resultados
print("\n\nCorrelação de Pearson:")
print("Correlação:", correlacao)
print("P-value:", p_value)

# Scatter Plot (Gráfico de Dispersão)
plt.figure(figsize=(10, 6))
plt.scatter(nova_tabela_agrupada['Platform'], nova_tabela_agrupada['Global_Sales'], alpha=0.5)
plt.title('Relação entre Quantidade de Plataformas e Vendas Globais')
plt.xlabel('Quantidade de Plataformas')
plt.ylabel('Vendas Globais')
plt.show()

# Selecionar apenas os 30 mais vendidos
top_30_vendas = nova_tabela_agrupada.head(30)

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(top_30_vendas['Platform'], top_30_vendas['Global_Sales'], alpha=0.5)
plt.title('Relação entre Quantidade de Plataformas e Vendas Globais (TOP 30)')
plt.xlabel('Quantidade de Plataformas')
plt.ylabel('Vendas Globais')
plt.show()

