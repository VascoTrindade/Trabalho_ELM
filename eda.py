import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Programming\Elementos\TPcsv\juncao_corrigida.csv', sep=';')

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


#Tornar em funções

print("Informações gerais:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe(include='all'))

# 2. Verificar valores em falta
print("\nValores em falta por coluna:")
missing = df.isnull().sum()
print(missing[missing > 0])

print("\nColunas com valor único (sem variabilidade):")
low_variance = [col for col in df.columns if df[col].nunique() == 1]
print(low_variance)

num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[col].dropna(), vert=False)
    plt.title(f'Boxplot de {col}')
    plt.xlabel(col)
    plt.grid(True)
    plt.show()

print("\nMatriz de correlação:")
correlation = df[num_cols].corr()
print(correlation)

# Visualização da correlação (com Matplotlib)
plt.figure(figsize=(10, 8))
plt.imshow(correlation, cmap='coolwarm', interpolation='none')
plt.colorbar(label='Correlação')
plt.xticks(range(len(num_cols)), num_cols, rotation=90)
plt.yticks(range(len(num_cols)), num_cols)
plt.title("Matriz de Correlação")
plt.tight_layout()
plt.show()

for col in num_cols:
    plt.figure(figsize=(6, 4))
    plt.hist(df[col].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Distribuição de {col}')
    plt.xlabel(col)
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.show()
