#pylint: disable=all
import pandas as pd
import re
import os

def transform_films_data():
    caminho = os.path.join('..', 'main', 'raw', 'df_films.csv')
    df = pd.read_csv(caminho)

    for column in df.columns:
        if df[column].dtype == 'object':  
            df[column] = df[column].str.lower() 

    for column in df.columns:
        if df[column].dtype == 'object':  
            df[column] = df[column].astype(str)  
            df[column] = df[column].apply(lambda x: re.sub(r'[^\w\s]', '', x))

    return df