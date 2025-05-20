import pandas as pd

#Pode tornar-se numa função
df = pd.read_csv('C:\Programming\Elementos\Trabalho\Trabalho_ELM\dados\juncao.csv', sep=';')

df['09. Valor'] = pd.to_numeric(df['09. Valor'], errors='coerce')

Q1 = df['09. Valor'].quantile(0.25)
Q3 = df['09. Valor'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['09. Valor'] < limite_inferior) | (df['09. Valor'] > limite_superior)]

print(f'Total de outliers encontrados: {len(outliers)}')
print(outliers.head())