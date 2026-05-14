import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import glob
import os

FEATURE_NAMES = [
    "speed_mean", "speed_std", "delay_mean_5m", "delay_mean_15m", "delay_mean_30m",
    "bunching_index", "on_time_pct", "headway_variance", "alert_nlp_score",
    "alert_count", "fleet_utilization", "speed_drop_ratio"
]

# Find all parquet files in temp subdirectories
parquet_files = glob.glob('temp/**/*.parquet', recursive=True)

print(f"Found {len(parquet_files)} parquet files")

# Read and concatenate feature data
dfs = []
for file in parquet_files:
    try:
        df = pd.read_parquet(file)
        if all(col in df.columns for col in FEATURE_NAMES):
            dfs.append(df[FEATURE_NAMES])
        else:
            print(f"Skipping {file}: missing features")
    except Exception as e:
        print(f"Error reading {file}: {e}")

if not dfs:
    raise ValueError("No valid data found")

combined_df = pd.concat(dfs, ignore_index=True)
print(f"Combined data shape: {combined_df.shape}")

# Fit scaler
scaler = StandardScaler()
scaler.fit(combined_df.values)

# Save to transit_dashboard/models/scaler_latest.pkl
import pickle
with open('transit_dashboard/models/scaler_latest.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("scaler_latest.pkl updated and saved to transit_dashboard/models/")