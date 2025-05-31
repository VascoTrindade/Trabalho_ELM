import pandas as pd
from eda import correlacao, outliers

def limpeza_dados(caminho_csv, caminho_saida="juncao_limpo.csv"):
    df = pd.read_csv(caminho_csv, sep=";")

    col_ano = df['Ano'].copy() if 'Ano' in df.columns else None
    col_territorio_nome = "Território"
    col_territorio = df[col_territorio_nome].copy()

    for col in df.columns:
        if col not in [col_territorio_nome, 'Ano']:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except:
                continue

    colunas_constantes = [col for col in df.columns if df[col].nunique() <= 1 and col not in [col_territorio_nome, 'Ano']]
    df = df.drop(columns=colunas_constantes)

    missing = df.isnull().sum()
    colunas_muitos_nulos = missing[(missing > len(df) * 0.5) & (~missing.index.isin([col_territorio_nome, 'Ano']))].index.tolist()
    df = df.drop(columns=colunas_muitos_nulos)

    df = df[df.isnull().mean(axis=1) < 0.5]

    df = df.fillna(df.mean(numeric_only=True))

    df_numerico = df.select_dtypes(include='number')

    colunas_correlacionadas = correlacao(df_numerico, limite=0.9)
    df_numerico = df_numerico.drop(columns=colunas_correlacionadas)

    df_numerico = outliers(df_numerico, z_thresh=3)

    if col_ano is not None:
        df_numerico.loc[:, 'Ano'] = col_ano.loc[df_numerico.index].values
    df_numerico.loc[:, col_territorio_nome] = col_territorio.loc[df_numerico.index].values

    colunas_finais = ['Ano', 'Território'] + [col for col in df_numerico.columns if col not in ['Ano', 'Território']]
    df_numerico = df_numerico[colunas_finais]

    df_numerico.to_csv(caminho_saida, index=False)
    print(f"Dados limpos salvos como '{caminho_saida}'")

if __name__ == "__main__":
    limpeza_dados("juncao_corrigida.csv")