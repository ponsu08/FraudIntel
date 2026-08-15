"""
URL Checker Utility
"""

import re
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """
    Validate URL format.
    """
    pattern = re.compile(
        r'^(https?:\/\/)?'
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})'
        r'(\/.*)?$'
    )

    return bool(pattern.match(url))


def get_domain(url: str):
    """
    Extract domain name.
    """
    parsed = urlparse(url)

    if parsed.netloc:
        return parsed.netloc

    return parsed.path


def has_https(url: str):
    return url.lower().startswith("https://")


def contains_ip(url: str):
    pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return bool(re.search(pattern, url))


def suspicious_symbols(url: str):
    symbols = ["@", "-", "_", "%", "~"]

    count = 0

    for s in symbols:
        count += url.count(s)

    return count


def check_url(url: str):
    """
    Complete URL analysis.
    """
    return {
        "valid": is_valid_url(url),
        "domain": get_domain(url),
        "https": has_https(url),
        "contains_ip": contains_ip(url),
        "suspicious_symbols": suspicious_symbols(url),
    }