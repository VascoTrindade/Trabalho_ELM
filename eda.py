import matplotlib.pyplot as plt
import pandas as pd

def mostrar_boxplots(df, colunas):
    plt.figure(figsize = (15,4))
    for i, col in enumerate(colunas):
        plt.subplot(1,len(colunas),i+1)
        plt.boxplot(df[col].dropna())
        plt.title(f"Outliers em {col}")
    plt.tight_layout()
    plt.show()

def mostrar_histogramas(df, colunas):
    plt.figure(figsize = (15,4))
    for i, col in enumerate(colunas):
        plt.subplot(1,len(colunas),i+1)
        plt.hist(df[col].dropna(),bins=30, alpha=0.7,edgecolor='black')
        plt.title(f"Distribuição de {col}")
    plt.tight_layout()
    plt.show()

def mapa_corelacao(df):
    import numpy as np
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplot(figsize=(8,6))
    cax = ax.matshow(corr, cmap = "coolwarm")
    fig.colorbar(cax)

    ticks = np.arange(len(corr.columns))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(corr.columns,rotation=45,ha="left")
    ax.set_yticklabels(corr.columns)
    plt.title("Mapa de correlação entre variáveis",pad=20)
    plt.tight_layout()
    plt.show()