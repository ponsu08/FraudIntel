"""
OCR and QR Utility
"""

import cv2
import pytesseract
from pyzbar.pyzbar import decode


def extract_text(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return ""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    return text.strip()


def decode_qr(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None

    decoded_objects = decode(image)

    if decoded_objects:
        return decoded_objects[0].data.decode("utf-8")

    return None