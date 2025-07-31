import pandas as pd

df = pd.read_csv('test.csv')


total_rows = df.shape[0]
total_cols = df.shape[1]
print("Total number of rows:", total_rows)
print("Total number of cols:", total_cols)

