import pandas as pd
import os

def integracao(pasta_csv, arquivo_saida='juncao_corrigida.csv'):
    ficheiros = [f for f in os.listdir(pasta_csv) if f.lower().endswith('.csv')]

    dfs = []
    for f in ficheiros:
        caminho_completo = os.path.join(pasta_csv, f)
        df = pd.read_csv(caminho_completo, sep=';')

        # Verificação das colunas esperadas
        colunas_esperadas = ['01. Ano', '02. Nome Região (Portugal)', '04. Filtro 1', '09. Valor']
        for col in colunas_esperadas:
            if col not in df.columns:
                print(f"Aviso: coluna '{col}' não encontrada no ficheiro {f}")

        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)
    df_final = df_final.drop_duplicates()

    # Renomear colunas padrão
    df_final = df_final.rename(columns={
        '01. Ano': 'Ano',
        '02. Nome Região (Portugal)': 'Território',
        '04. Filtro 1': 'Categoria',
        '09. Valor': 'Valor'
    })

    # Remover entradas agregadas (não-municipais)
    agregados = ['Portugal', 'Continente', 'Norte', 'Centro', 'Lisboa', 'Alentejo', 'Algarve', 'RA Açores', 'RA Madeira']
    df_final = df_final[~df_final['Território'].isin(agregados)]

    df_pivot = df_final.pivot_table(
        index=['Ano', 'Território'],
        columns='Categoria',
        values='Valor',
        aggfunc='first'
    ).reset_index()

    df_pivot.columns.name = None

    df_pivot = df_pivot.rename(columns={
        '25-34': 'Desemprego 25-34 anos',
        '35-44': 'Desemprego 35-44 anos',
        '45-54': 'Desemprego 45-54 anos',
        '55 ou mais anos': 'Desemprego 55+ anos',
        'Básico - 1º Ciclo': 'População com 1º Ciclo',
        'Básico - 2º Ciclo': 'População com 2º Ciclo',
        'Básico - 3º Ciclo e secundário': 'População com 3º Ciclo/Secundário',
        'Educação Pré-Escolar': 'Pré-Escolar',
        'Homens': 'População Empregada - Homens',
        'Mulheres': 'População Empregada - Mulheres',
        'Total': 'População Empregada - Total'
    })

    df_pivot = df_pivot[[
        'Ano', 'Território',
        'Desemprego 25-34 anos', 'Desemprego 35-44 anos', 'Desemprego 45-54 anos', 'Desemprego 55+ anos',
        'População com 1º Ciclo', 'População com 2º Ciclo', 'População com 3º Ciclo/Secundário', 'Pré-Escolar',
        'População Empregada - Homens', 'População Empregada - Mulheres', 'População Empregada - Total'
    ]]

    output_path = os.path.join(pasta_csv, arquivo_saida)
    df_pivot.to_csv(output_path, sep=';', index=False)

    print(f"Arquivo criado em: {output_path}")
    return output_path

integracao('C:\\Users\\carlo\\OneDrive\\Ambiente de Trabalho\\Universidade\\Licenciatura\\2ª Ano de Licenciatura\\1º Semestre\\Programação (1ºano)\\csv')