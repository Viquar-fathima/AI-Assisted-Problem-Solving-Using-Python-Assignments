import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

# ------------------------------------------------------
# 1. Load Data
# ------------------------------------------------------
file_path = r"C:\Users\moham_219zzho\Downloads\movie_reviews-1.csv"
df = pd.read_csv(file_path)

# ------------------------------------------------------
# 2. BEFORE SUMMARY
# ------------------------------------------------------
print("\n======= BEFORE CLEANING =======\n")
print(df.describe(include='all'))

# ------------------------------------------------------
# 3. TEXT CLEANING
# ------------------------------------------------------
def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()
    return text

df['clean_review'] = df['review_text'].apply(clean_text)

# ------------------------------------------------------
# 4. TF-IDF ENCODING
# ------------------------------------------------------
vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
tfidf_matrix = vectorizer.fit_transform(df['clean_review'])

print("\nTF-IDF Shape:", tfidf_matrix.shape)

# ------------------------------------------------------
# 5. FIX MISSING RATINGS
# ------------------------------------------------------
median_rating = df['rating'].median()
df['rating'] = df['rating'].fillna(median_rating)

# ------------------------------------------------------
# 6. NORMALIZE RATINGS
# ------------------------------------------------------
df['rating_normalized'] = df['rating'] / 10

# ------------------------------------------------------
# 7. AFTER SUMMARY
# ------------------------------------------------------
print("\n======= AFTER CLEANING =======\n")
print(df.describe(include='all'))

# ------------------------------------------------------
# 8. SAVE CLEANED OUTPUT
# ------------------------------------------------------
# Save inside same folder as Task4.py → assignment17/output/
current_directory = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_directory, "output")

os.makedirs(output_folder, exist_ok=True)

save_path = os.path.join(output_folder, "cleaned_movie_reviews.csv")
df.to_csv(save_path, index=False)

print("\nFile saved successfully at:\n", save_path)
