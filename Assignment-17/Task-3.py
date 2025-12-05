import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

print("Current working directory:", os.getcwd())

# ------------------------------------
# 1. Load dataset
# ------------------------------------
df = pd.read_csv(r"C:\Users\moham_219zzho\Downloads\iot_sensor.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp')

# ------------------------------------
# 2. BEFORE CLEANING
# ------------------------------------
before_cleaning = df.copy()
print("\n=========== BEFORE CLEANING ===========")
print(before_cleaning.head(), "\n")

# ------------------------------------
# 3. CLEANING STEPS
# ------------------------------------
df[['temperature', 'humidity']] = df[['temperature', 'humidity']].ffill()

df['temperature_clean'] = df['temperature'].rolling(window=10, min_periods=1).mean()
df['humidity_clean'] = df['humidity'].rolling(window=10, min_periods=1).mean()

scaler = StandardScaler()
df[['temp_scaled', 'hum_scaled']] = scaler.fit_transform(
    df[['temperature_clean', 'humidity_clean']]
)

encoder = LabelEncoder()
df['sensor_encoded'] = encoder.fit_transform(df['sensor_id'])

# ------------------------------------
# 4. AFTER CLEANING
# ------------------------------------
after_cleaning = df[['timestamp',
                     'sensor_id', 'sensor_encoded',
                     'temperature', 'temperature_clean', 'temp_scaled',
                     'humidity', 'humidity_clean', 'hum_scaled']]

print("=========== AFTER CLEANING ===========")
print(after_cleaning.head(), "\n")

# ------------------------------------
# 5. SAVE CLEANED FILE IN ASSIGNMENT FOLDER
# ------------------------------------
save_local = "cleaned_iot_data.csv"
after_cleaning.to_csv(save_local, index=False)

print(f"✔ Cleaned file saved in current folder at: {os.path.abspath(save_local)}")

# ------------------------------------
# 6. ALSO SAVE IN DOWNLOADS FOLDER
# ------------------------------------
save_downloads = r"C:\Users\moham_219zzho\Downloads\cleaned_iot_data.csv"
after_cleaning.to_csv(save_downloads, index=False)

print(f"✔ Cleaned file also saved at: {save_downloads}")
