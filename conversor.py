import pandas as pd

def spliter_and_convert(df, coordinate_col, components):
    """
    Separa os valores de Graus, Minutos e Segundos da coluna de coordenada em colunas menores
    e converte as novas colunas em valor numérico
    """
    df[coordinate_col] = df[coordinate_col].str.replace(',','.')
    df[components] = df[coordinate_col].str.split(':', expand=True)
    df[components] = df[components].apply(pd.to_numeric, errors='coerce')

def convert_coordinate(df, degree_col, minute_col, second_col, result_col):
    """
    Converte os valores de Graus, Minutos e Segundos em Graus Decimais
    """
    if (df[degree_col] < 0).any():
        df[result_col] = df[degree_col] - ((df[minute_col] / 60) + df[second_col] / 3600)
    else:
        df[result_col] = df[degree_col] + ((df[minute_col] / 60) + df[second_col] / 3600)

def converter_latlong(df):
    """
    Centraliza a operação de conversão em uma única função,
    deleta as colunas obsoletas do DataFrame 
    e padroniza os nomes dos novos campos
    """
    spliter_and_convert(df, 'LATITUDE', ['latd', 'latm', 'lats'])
    convert_coordinate(df, 'latd', 'latm', 'lats', 'LATITUDE_FINAL')

    spliter_and_convert(df, 'LONGITUDE', ['lond', 'lonm', 'lons'])
    convert_coordinate(df, 'lond', 'lonm', 'lons', 'LONGITUDE_FINAL')

    df = df.drop(columns=['latd', 'latm', 'lats', 'lond', 'lonm', 'lons', 'LATITUDE', 'LONGITUDE'])
    df = df.rename(columns={"LATITUDE_FINAL": "LATITUDE", "LONGITUDE_FINAL": "LONGITUDE"})

    return df