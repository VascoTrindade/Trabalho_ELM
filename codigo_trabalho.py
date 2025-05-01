import pandas as pd

#lê csv
path_desemprego = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\desemprego.csv"
path_envelhecimento = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\envelhicimento.csv"
path_emprego = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\populacao_empregada.csv"

#Ricardo
#path_desemprego = r"C:\Programming\Elementos\Trabalho\desemprego.csv"
#path_envelhecimento = r"C:\Programming\Elementos\Trabalho\envelhicimento.csv"
#path_emprego = r"C:\Programming\Elementos\Trabalho\populaçao_empregada.csv"

#Vasco
#path_desemprego = ""
#path_envelhecimento = ""
#path_emprego = ""

df_desemprego = pd.read_csv(path_desemprego, sep=';')
df_envelhecimento = pd.read_csv(path_envelhecimento, sep=';')
df_emprego = pd.read_csv(path_emprego, sep=';')




