"""
Train Email Phishing Detection Model
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


# -------------------------------------------------------
# Paths
# -------------------------------------------------------

DATASET_PATH = "../datasets/emails.csv"
MODEL_PATH = "../models/email_model.pkl"


# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print(df.head())


# -------------------------------------------------------
# Preprocess
# -------------------------------------------------------

df = preprocess_dataframe(df, "text")


# -------------------------------------------------------
# Features & Labels
# -------------------------------------------------------

X = df["text"]

y = df["label"]


# -------------------------------------------------------
# Train/Test Split
# -------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -------------------------------------------------------
# ML Pipeline
# -------------------------------------------------------

pipeline = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )
])


# -------------------------------------------------------
# Train
# -------------------------------------------------------

print("\nTraining Email Model...")

pipeline.fit(X_train, y_train)


# -------------------------------------------------------
# Evaluate
# -------------------------------------------------------

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report")

print(classification_report(y_test, predictions))


# -------------------------------------------------------
# Save Model
# -------------------------------------------------------

os.makedirs("../models", exist_ok=True)

joblib.dump(pipeline, MODEL_PATH)

print(f"\nModel saved to {MODEL_PATH}")