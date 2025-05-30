import pandas as pd
from eda import correlacao, outliers

def limpeza_dados(caminho_csv, caminho_saida="juncao_limpo.csv"):
    df = pd.read_csv(caminho_csv, sep=";")

    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        except:
            continue

    colunas_constantes = [col for col in df.columns if df[col].nunique() <= 1]
    df = df.drop(columns=colunas_constantes)

    missing = df.isnull().sum()
    colunas_muitos_nulos = missing[missing > len(df) * 0.5].index.tolist()
    df = df.drop(columns=colunas_muitos_nulos)

    df = df[df.isnull().mean(axis=1) < 0.5]

    df = df.fillna(df.mean(numeric_only=True))

    df_numerico = df.select_dtypes(include='number')

    colunas_correlacionadas = correlacao(df_numerico, limite=0.9)
    df_numerico = df_numerico.drop(columns=colunas_correlacionadas)

    df_numerico = outliers(df_numerico, z_thresh=3)

    df_numerico.to_csv(caminho_saida, index=False)
    print(f"Dados limpos salvos como '{caminho_saida}'")

if __name__ == "__main__":
    limpeza_dados("juncao_corrigida.csv")