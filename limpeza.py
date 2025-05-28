#Eu criei um ficheiro a parte que é para não tar a estragar o codigo, eu prefiro que um de voces verifique primeiro se ta tudo bem com as alteraçoes para a limpeza


#EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def valores_falta(df):
    """Identifica valores ausentes no DataFrame"""
    print("Valores em falta por coluna:")
    print(df.isnull().sum())


def estatisticas_descritivas(dados):
    """Exibe estatísticas descritivas dos dados"""
    print("\nEstatísticas descritivas:")
    print(dados.describe())


def correlacao(dados, limite=0.9):
    """Calcula e visualiza correlações entre variáveis"""
    corr = dados.corr()

    print("\nMatriz de correlação:")
    print(corr)

    # Identifica correlações fortes
    corr_triu = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    pares_fortes = corr_triu.stack()[abs(corr_triu.stack()) > limite]

    print(f"\nPares com correlação > {limite}:")
    print(pares_fortes)

    # Heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title('Matriz de Correlação')
    plt.tight_layout()
    plt.show()


def outliers(dados, z_thresh=3):
    """Identifica e visualiza outliers"""
    z_scores = np.abs((dados - dados.mean()) / dados.std())
    outliers = z_scores > z_thresh

    print(f"\nOutliers (Z-score > {z_thresh}):")
    for col in dados.columns:
        print(f"{col}: {outliers[col].sum()}")

    # Boxplot
    dados.plot(kind='box', subplots=True, layout=(4, 4), figsize=(15, 10))
    plt.suptitle('Distribuição das Variáveis', y=1.02)
    plt.tight_layout()
    plt.show()

#a_descritiva
def aplicar_kmeans(dados, n_clusters=3):
    """Aplica algoritmo K-means e visualiza resultados"""
    # Pré-processamento
    imputer = SimpleImputer(strategy='mean')
    scaler = StandardScaler()

    dados_imputados = imputer.fit_transform(dados)
    dados_norm = scaler.fit_transform(dados_imputados)

    # Clusterização
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(dados_norm)

    print(f"\nDistribuição dos clusters (K={n_clusters}):")
    print(pd.Series(clusters).value_counts())

    # Visualização com PCA
    pca = PCA(n_components=2)
    componentes = pca.fit_transform(dados_norm)

    plt.figure(figsize=(10, 6))
    plt.scatter(componentes[:, 0], componentes[:, 1], c=clusters, cmap='viridis')
    plt.title('Visualização dos Clusters')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.colorbar(label='Cluster')
    plt.grid(True)
    plt.show()

    return clusters

#integraçao
def integracao(pasta_csv, arquivo_saida='juncao_corrigida.csv'):
    """Integra múltiplos arquivos CSV em um dataset unificado"""
    # Lista arquivos CSV
    arquivos = [f for f in os.listdir(pasta_csv) if f.lower().endswith('.csv')]

    # Carrega e combina os dados
    dfs = []
    for arquivo in arquivos:
        caminho = os.path.join(pasta_csv, arquivo)
        df = pd.read_csv(caminho, sep=';')
        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)

    # Padroniza colunas
    df_final = df_final.rename(columns={
        '01. Ano': 'Ano',
        '02. Nome Região (Portugal)': 'Território',
        '04. Filtro 1': 'Categoria',
        '09. Valor': 'Valor'
    })

    # Transforma para formato wide
    df_pivot = df_final.pivot_table(
        index=['Ano', 'Território'],
        columns='Categoria',
        values='Valor',
        aggfunc='first'
    ).reset_index()

    # Limpa e organiza colunas
    df_pivot.columns.name = None
    colunas_ordenadas = [
        'Ano', 'Território', '25-34', '35-44', '45-54', '55 ou mais anos',
        'Básico - 1º Ciclo', 'Básico - 2º Ciclo', 'Básico - 3º Ciclo e secundário',
        'Educação Pré-Escolar', 'Homens', 'Mulheres', 'Total'
    ]
    df_final = df_pivot[colunas_ordenadas]

    # Salva o resultado
    caminho_saida = os.path.join(pasta_csv, arquivo_saida)
    df_final.to_csv(caminho_saida, sep=';', index=False)

    print(f"Dataset integrado salvo em: {caminho_saida}")
    return caminho_saida

#main
from eda import valores_falta, estatisticas_descritivas, correlacao, outliers
from a_descritiva import aplicar_kmeans
from integracao import integracao

if __name__ == "__main__":
    # 1. Integração dos dados
    caminho_dados = integracao(r'C:\Programming\Elementos\TPcsv')

    # 2. Carregar e preparar dados
    df = pd.read_csv(caminho_dados, sep=';')
    dados_numericos = df.drop(columns=['Ano', 'Território'])

    # 3. Análise Exploratória
    valores_falta(df)
    estatisticas_descritivas(dados_numericos)
    correlacao(dados_numericos)
    outliers(dados_numericos)

    # 4. Clusterização
    clusters = aplicar_kmeans(dados_numericos, n_clusters=3)
    df['Cluster'] = clusters

    # 5. Salvar resultados
    df.to_csv(caminho_dados.replace('.csv', '_com_clusters.csv'), sep=';', index=False)
