import pandas as pd
import numpy as np
import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import os

# SHOW ALL COLUMNS + ROWS
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', True)
pd.set_option('display.max_rows', None)

# DOWNLOAD STOPWORDS
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# ------------------------------------------------------
# FIXED: LOAD INPUT FILE FROM DOWNLOADS
# ------------------------------------------------------
input_path = r"C:\Users\moham_219zzho\Downloads\social_media.csv"
df = pd.read_csv(input_path)

print("=== BEFORE CLEANING ===")
print(df)

# HANDLE MISSING VALUES
df['likes'] = df['likes'].fillna(0).astype(int)
df['shares'] = df['shares'].fillna(0).astype(int)
df['post_text'] = df['post_text'].fillna("")

# CLEAN TEXT FUNCTION
def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^A-Za-z\s]", " ", text)
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["clean_post"] = df["post_text"].apply(clean_text)

# TIMESTAMP FEATURES
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.day_name()

# POST LENGTH
df["post_length"] = df["clean_post"].apply(lambda x: len(x.split()))
df = df[df["post_length"] >= 0]

print("\n=== AFTER CLEANING ===")
print(df[[
    "post_id", "user", "post_text",
    "likes", "shares",
    "timestamp", "clean_post",
    "hour", "weekday"
]])

# ------------------------------------------------------
# SAVE CLEANED FILE IN ASSIGNMENT FOLDER
# ------------------------------------------------------
save_assignment = r"C:\Users\moham_219zzho\OneDrive\Desktop\Aipp\assignment17\cleaned_social_media.csv"
df.to_csv(save_assignment, index=False)

# ------------------------------------------------------
# ALSO SAVE IN DOWNLOADS
# ------------------------------------------------------
save_downloads = r"C:\Users\moham_219zzho\Downloads\cleaned_social_media.csv"
df.to_csv(save_downloads, index=False)

print("\n✔ Task Completed")
print(f"✔ Saved in assignment folder: {save_assignment}")
print(f"✔ Saved in Downloads: {save_downloads}")
