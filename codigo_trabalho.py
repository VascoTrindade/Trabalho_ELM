import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#lê csv
#path_desemprego = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\desemprego.csv"
#path_envelhecimento = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\envelhicimento.csv"
#path_emprego = "C:\\Users\\carlo\\Licenciatura\\2_ano\\2_semestre\\EIA\\projeto\\populacao_empregada.csv"

#Ricardo
path_desemprego = r"C:\Programming\Elementos\Trabalho\desemprego.csv"
path_envelhecimento = r"C:\Programming\Elementos\Trabalho\envelhicimento.csv"
path_emprego = r"C:\Programming\Elementos\Trabalho\populaçao_empregada.csv"

#Vasco
#path_desemprego = r"C:\Users\DELL\PycharmProjects\Trabalho_ELM\desemprego.csv"
#path_envelhecimento = r"C:\Users\DELL\PycharmProjects\Trabalho_ELM\envelhicimento.csv"
#path_emprego = r"C:\Users\DELL\PycharmProjects\Trabalho_ELM\populacao_empregada.csv"

#Leitura dos dados
df_desemprego = pd.read_csv(path_desemprego, sep=';')
df_envelhecimento = pd.read_csv(path_envelhecimento, sep=';')
df_emprego = pd.read_csv(path_emprego, sep=';')

# === Função para preparar os dados ===
def preparar_dados(df, nome_valor):
    df.columns = df.columns.str.strip()
    df = df.rename(columns={
        "01. Ano": "Ano",
        "02. Nome Região (Portugal)": "Municipio",
        "09. Valor": nome_valor
    })
    df = df[["Ano", "Municipio", nome_valor]]
    df = df[df["Ano"].between(2013, 2022)]
    return df

# === Preparar cada dataset com nomes descritivos ===
df_desemprego_preparado = preparar_dados(df_desemprego, "Desemprego_Jovem")
df_envelhecimento_preparado = preparar_dados(df_envelhecimento, "Indice_Envelhecimento")
df_emprego_preparado = preparar_dados(df_emprego, "Populacao_Empregada")

# === Integrar os dados com merges sucessivos ===
df_merge1 = pd.merge(df_envelhecimento_preparado, df_desemprego_preparado, on=["Ano", "Municipio"], how="inner")
df_final = pd.merge(df_merge1, df_emprego_preparado, on=["Ano", "Municipio"], how="inner")

# === Ver resultado final ===
print("\nDados Integrados:")
print(df_final.head())

# === Guardar o resultado em CSV (opcional) ===
df_final.to_csv("dados_integrados.csv", sep=';', index=False)


# Verificar valores em falta
print("\n Valores em falta por coluna:")
print(df_final.isnull().sum())

# Ver estatísticas descritivas
print("\n Estatísticas descritivas:")
print(df_final.describe())

# Verificar duplicados
print("\n Entradas duplicadas:")
print(df_final.duplicated().sum())

# Verificar correlação entre variáveis
print("\n Correlação entre variáveis:")
print(df_final.corr(numeric_only=True))

# Mapa de calor de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(df_final.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Correlação entre Variáveis")
plt.show()

# Boxplots para deteção de outliers
plt.figure(figsize=(15, 4))
for i, col in enumerate(["Indice_Envelhecimento", "Desemprego_Jovem", "Populacao_Empregada"]):
    plt.subplot(1, 3, i + 1)
    sns.boxplot(y=df_final[col])
    plt.title(f"Outliers em {col}")
plt.tight_layout()
plt.show()

# Histogramas para distribuição
plt.figure(figsize=(15, 4))
for i, col in enumerate(["Indice_Envelhecimento", "Desemprego_Jovem", "Populacao_Empregada"]):
    plt.subplot(1, 3, i + 1)
    sns.histplot(df_final[col], bins=30, kde=True)
    plt.title(f"Distribuição de {col}")
plt.tight_layout()
plt.show()
