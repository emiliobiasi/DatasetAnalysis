import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import scipy.stats as stats

# Leitura do CSV
dataframe = pd.read_csv(r'C:/PROJECTS/TAREFAS FACUL/DatasetAnalysis/vgsales.csv')
print(dataframe)

# Filtrar os jogos da série GTA
gta_games = dataframe[dataframe['Name'].str.contains('Grand Theft Auto', case=False)]

# Selecionar apenas as colunas desejadas
gta_games_subset = gta_games[['Name', 'Year', 'Global_Sales']]

# Exibir os jogos da série GTA com as colunas selecionadas
print(gta_games_subset)

# Especificar o caminho do arquivo Excel de saída
output_excel_path = 'C:/PROJECTS/TAREFAS FACUL/DatasetAnalysis/gta_games_subset.xlsx'

# Salvar o DataFrame gta_games_subset em um arquivo Excel
gta_games_subset.to_excel(output_excel_path, index=False)

# Exibir mensagem informando que o Excel foi salvo com sucesso
print(f'Dados dos jogos da série GTA salvos em: {output_excel_path}')
