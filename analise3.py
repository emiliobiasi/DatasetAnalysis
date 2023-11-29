import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import chi2_contingency
from itertools import combinations


# Leitura do CSV
dataframe = pd.read_csv(r'C:/PROJECTS/TAREFAS FACUL/DatasetAnalysis/vgsales.csv')

# Agrupar por Ano e calcular a soma de vendas globais
sales_by_year = dataframe.groupby('Year')['Global_Sales'].sum().reset_index()

# Renomear as colunas para maior clareza
sales_by_year.columns = ['Year', 'Total_Global_Sales']

# Exibir a tabela agrupada por ano
print('\nVendas Globais por Ano:\n', sales_by_year)

# Criar gráfico de barra para a primeira tabela
plt.figure(figsize=(10, 6))
plt.bar(sales_by_year['Year'], sales_by_year['Total_Global_Sales'], color='blue')
plt.title('Vendas Globais por Ano (Gráfico de Barra)')
plt.xlabel('Ano')
plt.ylabel('Vendas Globais')
plt.show()

# Criar gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(sales_by_year['Year'], sales_by_year['Total_Global_Sales'], color='red', alpha=0.7)
plt.title('Relação entre Ano de Lançamento e Vendas Globais (Gráfico de Dispersão)')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Vendas Globais')
plt.grid(True)
plt.show()

#-------------------------------------------------------------------------------------------

# Agrupar por Plataforma e calcular a soma de vendas globais
sales_by_platform = dataframe.groupby('Platform')['Global_Sales'].sum().reset_index()

# Ordenar o DataFrame sales_by_platform por 'Global_Sales' em ordem decrescente
sales_by_platform = sales_by_platform.sort_values(by='Global_Sales', ascending=False)

# Exibir a tabela agrupada por plataforma
print('\nVendas Globais por Plataforma:\n', sales_by_platform)

# Criar gráfico de barras para as vendas globais por plataforma
plt.figure(figsize=(12, 6))
plt.bar(sales_by_platform['Platform'], sales_by_platform['Global_Sales'], color='orange')
plt.title('Vendas Globais por Plataforma (Gráfico de Barra)')
plt.xlabel('Plataforma')
plt.ylabel('Vendas Globais')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.show()

# Agrupar por Plataforma e calcular a média de vendas globais
average_sales_by_platform = dataframe.groupby('Platform')['Global_Sales'].mean().reset_index()

# Ordenar o DataFrame average_sales_by_platform por 'Global_Sales' em ordem decrescente
average_sales_by_platform = average_sales_by_platform.sort_values(by='Global_Sales', ascending=False)
# Exibir a tabela da média de vendas por plataforma
print('\nMédia de Vendas Globais por Plataforma:\n', average_sales_by_platform)

# Criar gráfico de barras para a média de vendas por plataforma
plt.figure(figsize=(12, 6))
plt.bar(average_sales_by_platform['Platform'], average_sales_by_platform['Global_Sales'], color='green')
plt.title('Média de Vendas Globais por Plataforma (Gráfico de Barra)')
plt.xlabel('Plataforma')
plt.ylabel('Média de Vendas Globais')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.show()

#-------------------------------------------------------------------------------------------

# Agrupar por Gênero e calcular a soma de vendas globais
sales_by_genre = dataframe.groupby('Genre')['Global_Sales'].sum().reset_index()

# Ordenar o DataFrame sales_by_genre por 'Global_Sales' em ordem decrescente
sales_by_genre = sales_by_genre.sort_values(by='Global_Sales', ascending=False)

# Exibir a tabela agrupada por gênero
print('\nVendas Globais por Gênero:\n', sales_by_genre)

# Criar gráfico de barras para as vendas globais por gênero
plt.figure(figsize=(12, 6))
plt.bar(sales_by_genre['Genre'], sales_by_genre['Global_Sales'], color='purple')
plt.title('Vendas Globais por Gênero (Gráfico de Barra)')
plt.xlabel('Gênero')
plt.ylabel('Vendas Globais')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.show()

# Agrupar por Gênero e calcular a média de vendas globais
average_sales_by_genre = dataframe.groupby('Genre')['Global_Sales'].mean().reset_index()

# Ordenar o DataFrame average_sales_by_genre por 'Global_Sales' em ordem decrescente
average_sales_by_genre = average_sales_by_genre.sort_values(by='Global_Sales', ascending=False)

# Exibir a tabela da média de vendas por gênero
print('\nMédia de Vendas Globais por Gênero:\n', average_sales_by_genre)

# Criar gráfico de barras para a média de vendas por gênero
plt.figure(figsize=(12, 6))
plt.bar(average_sales_by_genre['Genre'], average_sales_by_genre['Global_Sales'], color='orange')
plt.title('Média de Vendas Globais por Gênero (Gráfico de Barra)')
plt.xlabel('Gênero')
plt.ylabel('Média de Vendas Globais')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.show()

#-------------------------------------------------------------------------------------------

# Agrupar por Produtora e calcular a soma de vendas globais
sales_by_publisher = dataframe.groupby('Publisher')['Global_Sales'].sum().reset_index()

# Ordenar o DataFrame sales_by_publisher por 'Global_Sales' em ordem decrescente
sales_by_publisher = sales_by_publisher.sort_values(by='Global_Sales', ascending=False)

# Selecionar apenas as 100 maiores produtoras
top_100_publishers = sales_by_publisher.head(30)

# Exibir a tabela das 100 maiores produtoras
print('\nTop 30 Vendas Globais por Produtora:\n', top_100_publishers)

# Criar gráfico de barras para as vendas globais das 100 maiores produtoras
plt.figure(figsize=(12, 6))
plt.bar(top_100_publishers['Publisher'], top_100_publishers['Global_Sales'], color='green')
plt.title('Top 30 Vendas Globais por Produtora (Gráfico de Barra)')
plt.xlabel('Produtora')
plt.ylabel('Vendas Globais')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.show()

# Agrupar por Produtora e calcular a média de vendas globais
average_sales_by_publisher = dataframe.groupby('Publisher')['Global_Sales'].mean().reset_index()

# Ordenar o DataFrame average_sales_by_publisher por 'Global_Sales' em ordem decrescente
average_sales_by_publisher = average_sales_by_publisher.sort_values(by='Global_Sales', ascending=False)

# Selecionar apenas as 30 maiores produtoras
top_30_publishers = average_sales_by_publisher.head(30)

# Exibir a tabela das 30 maiores produtoras
print('\nTop 30 Média de Vendas Globais por Produtora:\n', top_30_publishers)

# Criar gráfico de barras para a média de vendas das 30 maiores produtoras
plt.figure(figsize=(12, 6))
plt.bar(top_30_publishers['Publisher'], top_30_publishers['Global_Sales'], color='purple')
plt.title('Top 30 Média de Vendas Globais por Produtora (Gráfico de Barra)')
plt.xlabel('Produtora')
plt.ylabel('Média de Vendas Globais')
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.show()
#-------------------------------------------------------------------------------------------


# Lista de variáveis categóricas para análise
categorical_variables = ['Platform', 'Genre', 'Publisher']

# Loop para realizar o teste qui-quadrado entre todas as combinações possíveis
for var1, var2 in combinations(categorical_variables, 2):
    contingency_table = pd.crosstab(index=dataframe[var1], columns=dataframe[var2])
    print(contingency_table)
    chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)
    
    # Exibição dos resultados para cada par de variáveis
    print(f'Teste Qui-Quadrado entre {var1} e {var2}:')
    print('Estatística Qui-Quadrado:', chi2_stat)
    print('Valor p do Teste Qui-Quadrado:', p_value)
    alpha_chi2 = 0.05
    if p_value < alpha_chi2:
        print('Rejeitar H0: Há evidências de associação significativa.')
    else:
        print('Não rejeitar H0: Não há evidências suficientes para afirmar associação significativa.')
    print('\n')


# Os resultados indicam que em cada teste qui-quadrado entre pares de variáveis (Plataforma e Gênero, Plataforma e Produtora, Gênero e Produtora), 
# você rejeitou a hipótese nula (H0) em todos os casos. Isso sugere que há evidências estatísticas de uma associação significativa entre as variáveis testadas.

# A interpretação específica para cada par seria:

# Plataforma e Gênero:

# Estatística Qui-Quadrado: 5909.98
# Valor p: 0.0 (muito próximo de zero)
# Conclusão: Há evidências de associação significativa entre as Plataformas e Gêneros dos jogos.
# Plataforma e Produtora:

# Estatística Qui-Quadrado: 73562.08
# Valor p: 0.0 (muito próximo de zero)
# Conclusão: Há evidências de associação significativa entre as Plataformas e Produtoras dos jogos.
# Gênero e Produtora:

# Estatística Qui-Quadrado: 25587.35
# Valor p: 0.0 (muito próximo de zero)
# Conclusão: Há evidências de associação significativa entre os Gêneros e Produtoras dos jogos.
# Em resumo, os resultados sugerem que as escolhas de Plataformas, Gêneros e Produtoras estão associadas 
# entre si nos dados analisados. Isso pode indicar que as preferências dos jogadores, estratégias de marketing ou 
# outros fatores estão influenciando as vendas de jogos de maneira conjunta em relação a essas variáveis.
