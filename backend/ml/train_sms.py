"""
Train SMS Phishing (Smishing) Detection Model
"""

import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

from preprocessing import preprocess_dataframe

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

DATASET_PATH = "../datasets/sms.csv"
MODEL_PATH = "../models/sms_model.pkl"

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

print("Loading SMS dataset...")

df = pd.read_csv(DATASET_PATH)

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
# Pipeline
# -------------------------------------------------------

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )),
    ("classifier", MultinomialNB())
])

# -------------------------------------------------------
# Train
# -------------------------------------------------------

print("Training SMS Model...")

pipeline.fit(X_train, y_train)

# -------------------------------------------------------
# Evaluation
# -------------------------------------------------------

pred = pipeline.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# -------------------------------------------------------
# Save Model
# -------------------------------------------------------

os.makedirs("../models", exist_ok=True)

joblib.dump(pipeline, MODEL_PATH)

print("SMS Model Saved Successfully!")