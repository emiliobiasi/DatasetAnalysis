import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import scipy.stats as stats

# Leitura do CSV
dataframe = pd.read_csv(r'C:/PROJECTS/TAREFAS FACUL/DatasetAnalysis/vgsales.csv')
print(dataframe)
colunas_para_transformar = ['Other_Sales']
dataframe[colunas_para_transformar] = dataframe[colunas_para_transformar] / 1_000_000

def gera_tabela(df):
    publishers = set(df['Publisher'])
    tabela = []
    for publisher in publishers:
        jogos = []
        sim = 0
        nao = 0
        for index, jogo in df.iterrows():
            if jogo['Publisher'] == publisher:
                df.drop(index=index)
                jogos.append(jogo)
        index=0
        for jogo in jogos:
            if index != 0:
                if jogo['Global_Sales'] <= jogos[index-1]['Global_Sales']:
                    nao += 1
                else:
                    sim += 1
            index+=1
        tabela.append([publisher, sim, nao, sim+nao])
    print(tabela)


gera_tabela(dataframe)