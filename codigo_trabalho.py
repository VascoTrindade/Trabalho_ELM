import pandas as pd

#lê csv
path_desemprego = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\desemprego.csv"
path_envelhecimento = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\envelhicimento.csv"
path_emprego = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\populacao_empregada.csv"

df_desemprego = pd.read_csv(path_desemprego, sep=';')
df_envelhecimento = pd.read_csv(path_envelhecimento, sep=';')
df_emprego = pd.read_csv(path_emprego, sep=';')

#Vê os nosmes das colunas
print("Colunas do Desemprego:", df_desemprego.columns)
print("Colunas do Envelhecimento:", df_envelhecimento.columns)
print("Colunas do Emprego:", df_emprego.columns)

#
