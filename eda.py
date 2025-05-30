import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


def valores_falta(df):
    print("Valores em falta por coluna:")
    print(df.isnull().sum())
    return df.isnull().sum()

def estatisticas_descritivas(dados):
    print("\nEstatísticas descritivas:")
    print(dados.describe())
    return dados.describe()

def correlacao(dados, limite=0.9):
    dados_numericos = dados.select_dtypes(include=['number'])
    corr = dados_numericos.corr()

    corr_triu = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    pares_correlacionados = corr_triu.stack()
    pares_altamente_correlacionados = pares_correlacionados[abs(pares_correlacionados) > limite]

    print(f"\nPares de variáveis com correlação maior que {limite}:")
    print(pares_altamente_correlacionados)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de Correlação")
    plt.tight_layout()
    plt.show()

    return list(pares_altamente_correlacionados.index.get_level_values(1).unique())

def outliers(dados, z_thresh=3):
    z_scores = (dados - dados.mean()) / dados.std()
    outliers = (np.abs(z_scores) > z_thresh)

    linhas_validas = ~(outliers.any(axis=1))
    print(f"\nRemovendo {len(dados) - linhas_validas.sum()} linhas com outliers (Z > {z_thresh})")

    num_cols = dados.shape[1]
    cols = 4
    rows = math.ceil(num_cols / cols)
    dados.plot(kind='box', subplots=True, layout=(rows, cols), figsize=(4 * cols, 3 * rows))

    return dados[linhas_validas]

