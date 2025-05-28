from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def aplicar_kmeans(dados, n_clusters=3):
    scaler = StandardScaler()
    dados_norm = scaler.fit_transform(dados)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
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
