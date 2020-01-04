import cleanerUtils
import pandas as pd
import numpy as np

age = np.array([12, 20, 25, 18, 19])
gender = np.array(['Male', None, 'Female', None, 'Female'])
df = pd.DataFrame({'age' : age, 'gender': gender})
print(df)

print(cleanerUtils.get_missing_valuecount_by_col(df))
print("*****")
print(cleanerUtils.get_col_names_with_missing_values(df))

new_df = cleanerUtils.drop_columns_with_missing_values(df)
print(new_df)

new_df2 = cleanerUtils.drop_rows_with_missing_values(df)
print(new_df2)


