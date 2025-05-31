import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA


def escolher_k(dados_norm, k_min=2, k_max=10):
    distortions = []
    silhouettes = []

    for k in range(k_min, k_max + 1):
        kmeans = KMeans(n_clusters=k, random_state=0)
        labels = kmeans.fit_predict(dados_norm)
        distortions.append(kmeans.inertia_)
        silhouettes.append(silhouette_score(dados_norm, labels))

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(range(k_min, k_max + 1), distortions, marker='o')
    plt.title("Método do Cotovelo (Inércia)")
    plt.xlabel("Número de Clusters (k)")
    plt.ylabel("Inércia")

    plt.subplot(1, 2, 2)
    plt.plot(range(k_min, k_max + 1), silhouettes, marker='o')
    plt.title("Silhouette Score")
    plt.xlabel("Número de Clusters (k)")
    plt.ylabel("Score")

    plt.tight_layout()
    plt.show()

def aplicar_kmeans(dados, n_clusters=3, nomes_colunas=None, exportar_csv=True):
    imputer = SimpleImputer(strategy='mean')
    dados_sem_nan = imputer.fit_transform(dados)

    scaler = StandardScaler()
    dados_norm = scaler.fit_transform(dados_sem_nan)

    print("\nAvaliar melhor número de clusters:")
    escolher_k(dados_norm, k_min=2, k_max=10)

    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    clusters = kmeans.fit_predict(dados_norm)

    print(f"\nDistribuição dos clusters (K-Means, k={n_clusters}):")
    print(pd.Series(clusters).value_counts())

    pca = PCA(n_components=2)
    componentes = pca.fit_transform(dados_norm)

    plt.figure(figsize=(8, 6))
    plt.scatter(componentes[:, 0], componentes[:, 1], c=clusters, cmap='Set1')
    plt.title("Clusters visualizados com PCA")
    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    if nomes_colunas:
        df_resultado = pd.DataFrame(dados, columns=nomes_colunas)
    else:
        df_resultado = pd.DataFrame(dados)

    df_resultado['Cluster'] = clusters

    print("\nMédia de cada variável por cluster:")
    print(df_resultado.groupby('Cluster').mean())

    if exportar_csv:
        df_resultado.to_csv("dados_clusterizados.csv", index=False)
        print("\nArquivo 'dados_clusterizados.csv' criado com os clusters atribuídos.")

    return df_resultado, clusters
