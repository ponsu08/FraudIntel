"""
Feature Extraction Utility
"""

import re

from utils.url_checker import (
    has_https,
    contains_ip,
    suspicious_symbols
)


def extract_email_features(text):

    text = text.lower()

    return {

        "length": len(text),

        "num_links": text.count("http"),

        "num_digits": sum(c.isdigit() for c in text),

        "urgent_words": len(
            re.findall(
                r"urgent|verify|password|bank|account|otp|login",
                text
            )
        )
    }


def extract_sms_features(text):

    return extract_email_features(text)


def extract_website_features(url):

    return {

        "length": len(url),

        "https": int(has_https(url)),

        "contains_ip": int(contains_ip(url)),

        "symbols": suspicious_symbols(url),

        "dots": url.count("."),

        "slashes": url.count("/")
    }


def extract_social_features(text):

    return {

        "length": len(text),

        "hashtags": text.count("#"),

        "mentions": text.count("@"),

        "links": text.count("http")
    }


def extract_voice_features(transcript):

    return extract_email_features(transcript)


def extract_qr_features(decoded_text):

    return extract_website_features(decoded_text)