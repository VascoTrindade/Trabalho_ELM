import pandas as pd
import os

pasta_csv = 'C:\Programming\Elementos\TPcsv'

ficheiros = [f for f in os.listdir(pasta_csv) if f.endswith('.csv')]

dfs = []

for f in ficheiros:
    caminho_completo = os.path.join(pasta_csv, f)
    df = pd.read_csv(caminho_completo, sep=';')
    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

output_path = os.path.join(pasta_csv, 'juncao_corrigida.csv')
df_final.to_csv(output_path, sep=';', index=False)

print(f"Ficheiro final criado com sucesso em: {output_path}")