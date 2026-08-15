"""
preprocessing.py

Utility functions for preprocessing text before training
or making predictions.
"""

import re
import string


def clean_text(text: str) -> str:
    """
    Clean text by removing unnecessary characters.
    """

    if text is None:
        return ""

    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove numbers
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_dataframe(df, text_column):
    """
    Apply preprocessing to a dataframe column.
    """

    df[text_column] = df[text_column].fillna("")
    df[text_column] = df[text_column].apply(clean_text)

    return df