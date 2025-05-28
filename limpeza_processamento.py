def tratar_valores_em_falta(df, limiar_colunas=0.5):
    #remove coluna que tenham mais de 50% de valores em falta
    df = df.loc[:, df.isnull().mean < limiar_colunas]
    #Preenche valores em falta com a mediana de cada coluna(apenas colunas numéricas)
    df = df.fillna(df.mean(numeric_only=True))
    return df

