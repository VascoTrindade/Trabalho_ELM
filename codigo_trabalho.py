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
path_desemprego = r"C:\Users\DELL\PycharmProjects\Trabalho_ELM\desemprego.csv"
path_envelhecimento = r"C:\Users\DELL\PycharmProjects\Trabalho_ELM\envelhicimento.csv"
path_emprego = r"C:\Users\DELL\PycharmProjects\Trabalho_ELM\populacao_empregada.csv"

df_desemprego = pd.read_csv(path_desemprego, sep=';')
df_envelhecimento = pd.read_csv(path_envelhecimento, sep=';')
df_emprego = pd.read_csv(path_emprego, sep=';')




