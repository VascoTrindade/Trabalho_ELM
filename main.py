import pandas as pd
from eda import valores_falta, estatisticas_descritivas, correlacao, outliers
from a_descritiva import aplicar_kmeans
from limpeza import limpeza_dados

entrada = r"C:\Programming\Elementos\Trabalho\Trabalho_ELM\juncao_corrigida.csv"
saida = r"C:\Programming\Elementos\Trabalho\Trabalho_ELM\juncao_limpo.csv"

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


dados_numericos = df_limpo.select_dtypes(include='number')
nomes_colunas = dados_numericos.columns.tolist()
df_com_clusters, clusters = aplicar_kmeans(dados_numericos, n_clusters=4, nomes_colunas=nomes_colunas)
df_limpo['Cluster'] = df_com_clusters['Cluster']

