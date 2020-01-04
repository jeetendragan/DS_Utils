import pandas as pd

def get_missing_valuecount_by_col(data):
    missing_val_count_by_column = (data.isnull().sum())
    return missing_val_count_by_column[missing_val_count_by_column > 0]