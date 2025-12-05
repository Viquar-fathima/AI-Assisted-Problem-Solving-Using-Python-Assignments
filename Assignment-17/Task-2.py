import pandas as pd
import numpy as np

# ============================
# LOAD DATA
# ============================
df = pd.read_csv(r"C:\Users\moham_219zzho\Downloads\financial_data.csv")


# Convert date to datetime & sort (important for time-series)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date').reset_index(drop=True)

print("=== BEFORE CLEANING ===")
print(df)

# ============================
# 1. HANDLE MISSING VALUES
# ============================

# closing_price → forward fill → backward fill
df['closing_price'] = df['closing_price'].fillna(method='ffill').fillna(method='bfill')

# volume → replace missing with 0
df['volume'] = df['volume'].fillna(0)

# ============================
# 2. CREATE LAG FEATURES
# ============================
df['return_1d'] = df['closing_price'].pct_change(1)       # 1-day return
df['return_7d'] = df['closing_price'].pct_change(7)       # 7-day return

# ============================
# 3. NORMALIZE VOLUME USING LOG-SCALING
# ============================
df['log_volume'] = np.log1p(df['volume'])   # log(1 + volume)

# ============================
# 4. DETECT OUTLIERS (IQR METHOD)
# ============================
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['is_outlier'] = (df['closing_price'] < lower) | (df['closing_price'] > upper)

# ============================
# FINAL OUTPUT
# ============================
print("\n=== AFTER CLEANING ===")
print(df)

# Save processed dataset
df.to_csv("financial_data_preprocessed.csv", index=False)

print("\nPreprocessing Complete ✔ Time-series dataset ready for forecasting models.")
