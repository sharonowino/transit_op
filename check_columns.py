import pandas as pd

# Read one parquet file to check columns
df = pd.read_parquet('temp/extract1/20260323_183401.parquet')
print("Columns in parquet file:")
print(df.columns.tolist())
print("Sample data:")
print(df.head())