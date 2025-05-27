from utils import ler_csv, preparar_dados
from eda import mostrar_boxplots, mostrar_histogramas, mapa_corelacao
import pandas as pd

#Caminhos dos ficheiros
path_juncao = "juncao.csv"

#Leitura e preparação dos dados
df_desemprego = preparar_dados(ler_csv(path_juncao),"Desemprego_jovem")
df_envelhecimento = preparar_dados(ler_csv(path_juncao), "Indice_Envelhecimento")
df_emprego = preparar_dados(ler_csv(path_juncao), "População_Empregada")

#Integração dos dados
df_merge = pd.merge(df_envelhecimento, df_envelhecimento, df_desemprego,on =["Ano","Municipio"],how="inner")
df_final = pd.merge(df_merge, df_emprego, on= ["Ano","Municipio"],how="inner")

