import numpy as np
import matplotlib.pyplot as plt

def valores_falta(df):
    print("Valores em falta por coluna:")
    print(df.isnull().sum())

def estatisticas_descritivas(dados):
    print("\nEstatísticas descritivas:")
    print(dados.describe())

def correlacao(dados, limite=0.9):
    corr = dados.corr()

    corr_triu = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    pares_correlacionados = corr_triu.stack()
    pares_altamente_correlacionados = pares_correlacionados[abs(pares_correlacionados) > limite]

    print("\nMatriz de correlação:")
    print(corr)

    print(f"\nPares de variáveis com correlação maior que {limite}:")
    print(pares_altamente_correlacionados)

    plt.figure(figsize=(10, 6))
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar(label='Correlação')
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title('Matriz de Correlação')
    plt.tight_layout()
    plt.show()

def outliers(dados, z_thresh=3):
    z_scores = (dados - dados.mean()) / dados.std()
    outliers = (np.abs(z_scores) > z_thresh)

    print(f"\nOutliers por variável (Z-score > {z_thresh}):")
    for coluna in dados.columns:
        n_outliers = outliers[coluna].sum()
        print(f"{coluna}: {n_outliers} outlier(s)")

    dados.plot(kind='box', subplots=True, layout=(int(np.ceil(len(dados.columns)/3)), 3),
               figsize=(12, 8), sharex=False, sharey=False)
    plt.tight_layout()
    plt.suptitle('Boxplots para Detecção Visual de Outliers', y=1.02)
    plt.show()