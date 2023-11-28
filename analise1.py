import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv(r'C:/PROJECTS/TAREFAS FACUL/TrabalhoFinal - ISAIAS/vgsales.csv')

print(dataset)

# Selecionar apenas as colunas desejadas
name_platform_global = dataset.loc[:, ['Name', 'Platform', 'Global_Sales']]

# Exibir a nova tabela
print("\n\nTabela Filtrada: Name | Plataform | Global_Sales\n")
print(name_platform_global)

# Agrupar por título do jogo e somar as vendas globais
nova_tabela_agrupada = name_platform_global.groupby('Name').agg({'Platform': 'count', 'Global_Sales': 'sum'}).reset_index()

# Exibir a nova tabela agrupada
print("\n\nTabela Filtrada Agrupada : Name | Plataform (em número) | Global_Sales (acumulado)\n")
print(nova_tabela_agrupada)

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

# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x=nova_tabela_agrupada['Global_Sales'])
plt.title('Box Plot das Vendas Globais')
plt.xlabel('Vendas Globais')
plt.show()


# Agrupar por número de plataformas e somar as vendas globais
vendas_por_plataformas = nova_tabela_agrupada.groupby('Platform')['Global_Sales'].sum().reset_index()

# Ordenar a tabela por número de plataformas
vendas_por_plataformas = vendas_por_plataformas.sort_values(by='Platform', ascending=True)

# Exibir a tabela de vendas por número de plataformas
print("\n\nTabela de Vendas Agrupadas por Número de Plataformas:\n")
print(vendas_por_plataformas)

# # Calcular a média de vendas para cada quantidade de plataformas
# media_vendas_por_quantidade_plataformas = nova_tabela_agrupada.groupby('Platform')['Global_Sales'].mean()
# print(media_vendas_por_quantidade_plataformas)
# # Gráfico de Barras
# plt.figure(figsize=(12, 6))
# plt.bar(media_vendas_por_quantidade_plataformas.index, media_vendas_por_quantidade_plataformas)
# plt.title('Média de Vendas por Quantidade de Plataformas')
# plt.xlabel('Quantidade de Plataformas')
# plt.ylabel('Média de Vendas Globais')
# plt.show()