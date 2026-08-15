"""
Train Social Media Phishing Detection Model

Dataset:
backend/datasets/social.csv

Output:
backend/models/social_model.pkl
"""

import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from preprocessing import preprocess_dataframe

# -----------------------------------------------------
# Paths
# -----------------------------------------------------

DATASET_PATH = "../datasets/social.csv"
MODEL_PATH = "../models/social_model.pkl"

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

print("=" * 50)
print("Loading Social Media Dataset...")
print("=" * 50)

df = pd.read_csv(DATASET_PATH)

print("\nDataset Shape:", df.shape)
print(df.head())

# -----------------------------------------------------
# Preprocess Text
# -----------------------------------------------------

df = preprocess_dataframe(df, "text")

# -----------------------------------------------------
# Features & Labels
# -----------------------------------------------------

X = df["text"]
y = df["label"]

# -----------------------------------------------------
# Train/Test Split
# -----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------------------------------
# ML Pipeline
# -----------------------------------------------------

pipeline = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=5000,
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            random_state=42
        )
    )
])

# -----------------------------------------------------
# Train Model
# -----------------------------------------------------

print("\nTraining Social Phishing Model...\n")

pipeline.fit(X_train, y_train)

# -----------------------------------------------------
# Evaluate
# -----------------------------------------------------

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("Accuracy")
print("=" * 50)

print(f"{accuracy * 100:.2f}%")

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

# -----------------------------------------------------
# Save Model
# -----------------------------------------------------

os.makedirs("../models", exist_ok=True)

joblib.dump(pipeline, MODEL_PATH)

print("\nSocial Media Model Saved Successfully!")

print("Saved to:", MODEL_PATH)