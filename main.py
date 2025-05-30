import pandas as pd
from eda import valores_falta, estatisticas_descritivas, correlacao, outliers
from a_descritiva import aplicar_kmeans
from limpeza import limpeza_dados

entrada = "C:\\Users\\carlo\\OneDrive\\Ambiente de Trabalho\\Universidade\\Licenciatura\\2ª Ano de Licenciatura\\1º Semestre\\Programação (1ºano)\\Trabalho_ELM\\juncao_corrigida.csv"
saida = "C:\\Users\\carlo\\OneDrive\\Ambiente de Trabalho\\Universidade\\Licenciatura\\2ª Ano de Licenciatura\\1º Semestre\\Programação (1ºano)\\Trabalho_ELM\\juncao_limpa.csv"

df_inicial = pd.read_csv(entrada, sep=";")

print("Análise inicial (dados brutos):")
valores_falta(df_inicial)
estatisticas_descritivas(df_inicial.select_dtypes(include='number'))
correlacao(df_inicial.select_dtypes(include='number'))
outliers(df_inicial.select_dtypes(include='number'))

limpeza_dados(entrada, saida)

df_limpo = pd.read_csv(saida)

print("Análise após limpeza:")
valores_falta(df_limpo)
estatisticas_descritivas(df_limpo)
correlacao(df_limpo)
outliers(df_limpo)

clusters = aplicar_kmeans(df_limpo, n_clusters=3)
df_limpo['Cluster'] = clusters