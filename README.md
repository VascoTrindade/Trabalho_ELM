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
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Autor](#autor)

## Sobre o projeto
Este projeto foi desenvolvido no âmbito da unidade curricular **Elementos de Inteligência Artificial e Ciência de Dados**.

O foco pricipal deste projeto ´analisar o impacto conjunto de duas problematicas relevantes para o futuro socioeconómico dos municipios portugueses: o **envelhecimento do corpo docente** e o **desemprego jovem**.

Utilizando dados da [PORDATA](https://www.pordata.pt/municipios), aplicaram-se 
técnicas de análise exploratória, pré-processamento e **machine learning** para descobrir padrões, relações e agrupamentos relevantes.


## Objetivos
-Identificar municípios com **elevado envelhecimento docente** e **alto desemprego jovem** <br>
-Avaliar a **correlação entre escolariedade e empregabilidade** <br>
-Detectar variações temporais e reginais que evidenciem **falta de renovação geracional**.

## Estrutura do Projeto
```bash
|-- integracao.py             # Integração dos ficheiros CSV da PORDATA
|--eda.py                     # Análise exploratória e visualizações
|--limpeza.py                 # Limpeza, imputação e outliers
|--a_descritiva.py            #K-Means e análises descritivas
|--main.py                    # Script principal
|--juncao_corrigida.csv       # Dados integrados
|--juncao_limpa.csv           # Dados limpos
|--dados_clustering           # Dados com clusters







