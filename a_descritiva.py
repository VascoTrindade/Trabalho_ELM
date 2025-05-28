from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.decomposition import PCA


def aplicar_kmeans(dados, n_clusters=3):
    imputer = SimpleImputer(strategy='mean')
    dados_sem_nan = imputer.fit_transform(dados)

    scaler = StandardScaler()
    dados_norm = scaler.fit_transform(dados_sem_nan)

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
