import pandas as pd
from eda import valores_falta, estatisticas_descritivas, correlacao, outliers

df = pd.read_csv(r"/Trabalho/Trabalho_ELM/juncao_corrigida.csv", sep =";")
dados_numericos = df.drop(columns=['Ano', 'Território'])

valores_falta(df)
estatisticas_descritivas(dados_numericos)
correlacao(dados_numericos)
outliers(dados_numericos)

