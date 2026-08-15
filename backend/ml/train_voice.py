"""
Train Voice Phishing (Vishing) Detection Model
"""

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

DATASET_PATH = "../datasets/voice.csv"

MODEL_PATH = "../models/voice_model.pkl"

SCALER_PATH = "../models/scaler.pkl"

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

print("=" * 50)
print("Loading Voice Dataset...")
print("=" * 50)

df = pd.read_csv(DATASET_PATH)

print("\nDataset Shape:", df.shape)
print(df.head())

# -------------------------------------------------------
# Features
# -------------------------------------------------------

# Expected columns:
# duration
# num_suspicious_words
# urgency_score
# caller_reputation
# label

X = df.drop("label", axis=1)
y = df["label"]

# -------------------------------------------------------
# Train/Test Split
# -------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -------------------------------------------------------
# Feature Scaling
# -------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# -------------------------------------------------------
# Model
# -------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

# -------------------------------------------------------
# Train
# -------------------------------------------------------

print("\nTraining Voice Phishing Model...\n")

model.fit(X_train, y_train)

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("Accuracy")
print("=" * 50)

print(f"{accuracy * 100:.2f}%")

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

# -------------------------------------------------------
# Save Model
# -------------------------------------------------------

os.makedirs("../models", exist_ok=True)

joblib.dump(model, MODEL_PATH)

joblib.dump(scaler, SCALER_PATH)

print("\nVoice Model Saved Successfully!")

print(MODEL_PATH)

print(SCALER_PATH)