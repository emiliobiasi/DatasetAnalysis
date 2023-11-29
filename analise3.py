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

# ANÁLISE DE REGRESSÃO MULTIPLA
# a variável dependente (ou resposta) seria Global_Sales, e as variáveis independentes (ou preditoras) seriam Publisher, Platform e Genre.
# Convert the 'Genre' column to a numerical dtype
dataframe['Genre'] = dataframe['Genre'].astype('category').cat.codes

# Convert the 'Platform' column to a numerical dtype
dataframe['Platform'] = dataframe['Platform'].astype('category').cat.codes

# Convert the 'Publisher' column to a numerical dtype
dataframe['Publisher'] = dataframe['Publisher'].astype('category').cat.codes

# Create the OLS model
model = sm.OLS(dataframe['Global_Sales'], dataframe[['Genre', 'Platform', 'Publisher']])

# Estimate the model
model = model.fit()

# Display the results
print(model.summary())

#---------------------------------------------------------------------------------------------


# No modelo de regressão linear que você ajustou, os coeficientes para as variáveis 'Genre', 'Platform' e 'Publisher' 
# indicam a variação média em 'Global_Sales' associada a uma unidade de mudança nessas variáveis, mantendo as outras 
# variáveis constantes.

# A interpretação dos coeficientes no seu caso seria a seguinte:
# Para uma unidade adicional na variável 'Genre', esperamos um aumento médio de 0.0232 nas vendas globais, mantendo 'Platform' e 'Publisher' constantes.
# Para uma unidade adicional na variável 'Platform', esperamos um aumento médio de 0.0140 nas vendas globais, mantendo 'Genre' e 'Publisher' constantes.
# Para uma unidade adicional na variável 'Publisher', esperamos um aumento médio de 0.0006 nas vendas globais, mantendo 'Genre' e 'Platform' constantes.

# Portanto, com base nos coeficientes, a variável que parece ter um impacto mais significativo nas vendas globais é 'Genre', seguida por 'Platform' e 'Publisher'. 
# No entanto, é importante observar que a interpretação dos coeficientes depende da escala das variáveis. Certifique-se de considerar a escala das variáveis ao 
# interpretar os resultados.
# Lembre-se também de que a interpretação causal em um modelo de regressão observacional como este pode ser desafiadora. Os resultados podem indicar associações, 
# mas não necessariamente causalidade.


# Portanto, a análise de regressão múltipla permitiria avaliar como as editoras (Publisher), plataformas (Platform) e gêneros (Genre) contribuem para as vendas 
# globais de jogos, e ajudaria a identificar quais dessas variáveis são mais importantes na explicação das variações nas vendas globais.