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
    dados_numericos = dados.select_dtypes(include='number')

    z_scores = (dados_numericos - dados_numericos.mean()) / dados_numericos.std()
    outliers_mask = (np.abs(z_scores) > z_thresh)

    linhas_validas = ~(outliers_mask.any(axis=1))
    print(f"\nRemovendo {len(dados) - linhas_validas.sum()} linhas com outliers (Z > {z_thresh})")

    num_cols = dados_numericos.shape[1]
    cols = 4
    rows = math.ceil(num_cols / cols)
    dados_numericos.plot(kind='box', subplots=True, layout=(rows, cols), figsize=(4 * cols, 3 * rows))
    plt.tight_layout()
    plt.show()

    return dados.loc[linhas_validas].copy()


def graficos_exploratorios(df):
    plt.style.use('ggplot')


    top_envelhecimento = df.sort_values(by="Pré-Escolar", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_envelhecimento, x="Pré-Escolar", y="Território", ci=None)
    plt.title("Top Territórios com Maior Índice de Envelhecimento Docente (Pré-Escolar)")
    plt.xlabel("Índice de Envelhecimento")
    plt.ylabel("Território")
    plt.tight_layout()
    plt.show()


    top_desemprego = df.sort_values(by="Desemprego 25-34 anos", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_desemprego, x="Desemprego 25-34 anos", y="Território", ci=None)
    plt.title("Top Territórios com Maior Desemprego Jovem (25-34 anos)")
    plt.xlabel("Desemprego")
    plt.ylabel("Território")
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="Pré-Escolar", y="Desemprego 25-34 anos")
    plt.title("Correlação entre Envelhecimento Docente e Desemprego Jovem")
    plt.xlabel("Índice de Envelhecimento (Pré-Escolar)")
    plt.ylabel("Desemprego Jovem (25-34 anos)")
    plt.tight_layout()
    plt.show()


    df_grouped = df.groupby("Ano").mean(numeric_only=True).reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped["Ano"], df_grouped["Desemprego 25-34 anos"], label="Desemprego Jovem")
    plt.plot(df_grouped["Ano"], df_grouped["Pré-Escolar"], label="Envelhecimento Docente")
    plt.title("Evolução Temporal: Desemprego Jovem e Envelhecimento Docente")
    plt.xlabel("Ano")
    plt.ylabel("Média")
    plt.legend()
    plt.tight_layout()
    plt.show()


    escolaridade_cols = [
        "População com 1º Ciclo",
        "População com 2º Ciclo",
        "População com 3º Ciclo/Secundário"
    ]
    escolaridade_df = df[escolaridade_cols].mean().reset_index()
    escolaridade_df.columns = ["Escolaridade", "Média População"]
    plt.figure(figsize=(10, 6))
    sns.barplot(data=escolaridade_df, x="Escolaridade", y="Média População", ci=None)
    plt.title("Média de População Empregada por Nível de Escolaridade")
    plt.xlabel("Escolaridade")
    plt.ylabel("População Empregada Média")
    plt.tight_layout()
    plt.show()