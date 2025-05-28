#Pode ser interessante manter por causa do IQR
# import pandas as pd
#
# #Pode tornar-se numa função
# df = pd.read_csv(r'C:\Programming\Elementos\TPcsv\juncao_corrigida.csv', sep=';')
#
# df['Total'] = pd.to_numeric(df['Total'], errors='coerce')
#
# Q1 = df['Total'].quantile(0.25)
# Q3 = df['Total'].quantile(0.75)
# IQR = Q3 - Q1
#
# limite_inferior = Q1 - 1.5 * IQR
# limite_superior = Q3 + 1.5 * IQR

#outliers = df[(df['Total'] < limite_inferior) | (df['Total'] > limite_superior)]

#print(f'Total de outliers encontrados: {len(outliers)}')
#print(outliers.head())