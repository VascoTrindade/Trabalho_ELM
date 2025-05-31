# Territórios em Transição: O Impacto do Envelhicimento dos Professores e do Desemprego Jovem

## ÍNDICE
- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos](#objetivos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Fases do Projeto](#fases-do-projeto)
  - [1. Recolha e Integração de Dados](#1-recolha-e-integracao-de-dados)
  - [2. Análise Exploratória de Dados (EDA)](#2-analise-exploratoria-de-dados-eda)
  - [3. Limpeza e Pré-processamento de Dados](#3-limpeza-e-pre-processamento-de-dados)
  - [4. Análise Descritiva e Clustering](#4-analise-descritiva-e-clustering)
- [Visualizações Produzidas](#visualizacoes-produzidas)
- [Conclusões](#conclusoes)


---
## Sobre o projeto
Este projeto foi desenvolvido no âmbito da unidade curricular **Elementos de Inteligência Artificial e Ciência de Dados**.

O foco pricipal deste projeto foi analisar o impacto conjunto de duas problemáticas relevantes para o futuro socioeconómico dos municipios portugueses: o **envelhecimento do corpo docente** e o **desemprego jovem**.

Utilizando dados da [PORDATA](https://www.pordata.pt/municipios), aplicaram-se 
técnicas de análise exploratória, pré-processamento e **machine learning** para descobrir padrões, relações e agrupamentos relevantes.

---
## Objetivos
-Identificar municípios com **elevado envelhecimento docente** e **alto desemprego jovem** <br>
-Avaliar a **correlação entre escolariedade e empregabilidade** <br>
-Detectar variações temporais e regionais que evidenciem a **falta de renovação das gerações**.

---
## Estrutura do Projeto
```bash
|-- integracao.py         # Integração dos ficheiros CSV da PORDATA
|-- eda.py                # Análise exploratória e visualizações
|-- limpeza.py            # Limpeza, imputação e outliers
|-- a_descritiva.py       # K-Means e análises descritivas
|-- main.py               # Script principal
|-- juncao_corrigida.csv  # Dados integrados
|-- juncao_limpa.csv      # Dados limpos
|-- dados_clustering      # Dados com clusters
```
---
## Fases do Projeto
### 1. Recolha e Integração dos Dados
Os dados foram recolhidos da PORDATA em ficheiros separados e posteriormente foram integrados com a função `integracao()`, que automatiza a fusão dos CSVs e transforma os dados num único dataset estruturado por Ano, Território e Variáveis.

**Ficheiro Gerado**: `juncao_corrigida.csv`

---
### 2. Análise Exploratória de Dados (EDA)
Nesta fase foram exploradas as seguintes estatísticas descritivas,valores em falta, outliers e correlações.

Destaques:
- Mapa de correlação entre variáveis.
- Detecção de variáveis redundantes.
- Outliers eliminados com Z-score.

---
### 3. Limpeza e Pré-processamento de Dados
Foram aplicadas diversas técnicas de limpeza:
- Remoção de colunas com vários valores nulos;
- Imputação da média para valores ausentes;
- Eliminação de outliers;
- Exclusão de variáveis altamente correlacionadas.

**Ficheiro Final**: `juncao_limpo.csv`

---
### 4. Análise Descritiva e Clustering
Foi aplicado o algoritmo **K-Means** com número ótimo de clusters determinado por:
- Método do Cotovelo (Inércia)
- Silhouette Score

Os dados foram normalizados com `StandardScaler` e visualizados com **PCA (2D)**.

**Ficheiro Gerado**: `dados_clusterizados.csv`

---
## Visualizações Produzidas
- **Clusters visualizados com PCA (2D)**
- **Top 10 Munícipios com Maior Desemprego Jovem (25-34 anos)**
- **Correlação entre Envelhicimento Docente e Desemprego Jovem**
- **Evolução Temporal: Desemprego Jovem vs Envelhicimento Docente(2010-2023)**
- **Avaliação de Clusters (Elbow e Silhouette Score)**
- **Top 10 Munícipios com Maior Índice de Envelhicimento Docente(Pré-Escolar)**

---
## Conclusoes
- Munícipios como **Oliveira de Azeméis, Nelas e Barcelos** apresentam simultaneamente elevados índices de envelhecimento docente e desemprego jovem;
- Existe **falta de renovação de gerações** no ensino, particularmente no pré-escolar;
- Há uma **correlação fraca entre envelhecimento e escolaridade**, mas padrões consistentes surgem nos clusters;
- Os resultados mostram **agrupamentos regionais claros** e evidenciam desigualdade socioeducativas locais.




