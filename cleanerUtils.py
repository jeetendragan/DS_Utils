import pandas as pd

def get_missing_valuecount_by_col(data):
    missing_val_count_by_column = (data.isnull().sum())
    return missing_val_count_by_column[missing_val_count_by_column > 0]

def get_col_names_with_missing_values(dataframe):
    return dataframe.columns[dataframe.isnull().any()].tolist()

def drop_columns_with_missing_values(dataframe):
    cols_with_missingvals = get_col_names_with_missing_values(dataframe)
    return dataframe.drop(columns = cols_with_missingvals)

def drop_rows_with_missing_values(dataframe):
    return dataframe.dropna()