"""
Train Website Phishing Detection Model
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

DATASET_PATH = "../datasets/websites.csv"

MODEL_PATH = "../models/website_model.pkl"

SCALER_PATH = "../models/scaler.pkl"

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

print("Loading Website Dataset...")

df = pd.read_csv(DATASET_PATH)

# -------------------------------------------------------
# Features
# -------------------------------------------------------

X = df.drop("label", axis=1)

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
# Scaling
# -------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# -------------------------------------------------------
# Model
# -------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

print("Training Website Model...")

model.fit(X_train, y_train)

# -------------------------------------------------------
# Evaluation
# -------------------------------------------------------

pred = model.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, pred))

print(classification_report(y_test, pred))

# -------------------------------------------------------
# Save
# -------------------------------------------------------

os.makedirs("../models", exist_ok=True)

joblib.dump(model, MODEL_PATH)

joblib.dump(scaler, SCALER_PATH)

print("Website Model Saved Successfully!")