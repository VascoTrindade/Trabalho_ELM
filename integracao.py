import pandas as pd
import os

def integracao(pasta_csv, arquivo_saida='juncao_corrigida.csv'):
    ficheiros = [f for f in os.listdir(pasta_csv) if f.lower().endswith('.csv')]

    dfs = []
    for f in ficheiros:
        caminho_completo = os.path.join(pasta_csv, f)
        df = pd.read_csv(caminho_completo, sep=';')
        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)

    df_final = df_final.rename(columns={
        '01. Ano': 'Ano',
        '02. Nome Região (Portugal)': 'Território',
        '04. Filtro 1': 'Categoria',
        '09. Valor': 'Valor'
    })

    df_pivot = df_final.pivot_table(
        index=['Ano', 'Território'],
        columns='Categoria',
        values='Valor',
        aggfunc='first'  # Assume que não há duplicatas
    ).reset_index()

    df_pivot.columns.name = None  # Remover nome do eixo das colunas
    df_pivot = df_pivot.rename(columns={
        'Homens': 'Homens',
        'Mulheres': 'Mulheres',
        'Total': 'Total'
    })

    df_pivot = df_pivot[['Ano', 'Território', 'Homens', 'Mulheres', 'Total']]

    output_path = os.path.join(pasta_csv, arquivo_saida)
    df_pivot.to_csv(output_path, sep=';', index=False)

    print(f"Arquivo criado em: {output_path}")
    return output_path

integracao('C:\\Users\\carlo\\OneDrive\\Ambiente de Trabalho\\Universidade\\Licenciatura\\2ª Ano de Licenciatura\\1º Semestre\\Programação (1ºano)\\csv')