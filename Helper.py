import pandas as pd

def heatmap(df):
    quality_dummies = pd.get_dummies(df['Quality'], dtype='int')
    df = pd.concat([df, quality_dummies], axis=1)
    df = df.drop(['Quality'], axis=1)
    return df
