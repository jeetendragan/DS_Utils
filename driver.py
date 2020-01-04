import cleanerUtils
import pandas as pd
import numpy as np

age = np.array([19, None, 25, 18, 19])
gender = np.array(['Male', None, 'Female', None, 'Female'])
df = pd.DataFrame({'age' : age, 'gender': gender})
print(df)

print(cleanerUtils.get_missing_valuecount_by_col(df))