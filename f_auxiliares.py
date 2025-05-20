import pandas as pd

def ler_csv(path, sep=';'):
    return pd.read_csv(path, sep=sep)

def preparar_dados(df, nome_valor):
    df.columns = df.columns.str.strip()
    df = df.rename(columns={
        "01. Ano": "Ano",
        "02. Nome Região (Portugal)": "Municipio",
        "09. Valor": nome_valor
    })
    df = df[["Ano", "Municipio", nome_valor]]
    df = df[df["Ano"].between(2013, 2022)]
    return df