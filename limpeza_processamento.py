def tratar_valores_em_falta(df, limiar_colunas=0.5):
    df = df.loc[:, df.isnull().mean < limiar_colunas]
    df = df.fillna(df.mean(numeric_only=True))
    return df

#def win_outliers(df):
    #for col in df.select_dtypes(include=['number']).columns:
        #Q1 = df[col].quantile(0.25)
        #Q3 = df[col].quantile(0.75)
        #IQR = Q3 - Q1
        #low, high = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        #df[col] = df[col].clip(lower=low, upper=high)
        #return df

def remover_outliers(df, z_thresh=3):
    z_scores = (df - df.mean()) / df.std()
    filtro = (z_scores.abs() < z_thresh).all(axis=1)
    df_filtrado = df[filtro]
    return df_filtrado