"""
Helper Functions
"""

import random
import string
from datetime import datetime


def generate_id(prefix="FD"):

    random_part = ''.join(

        random.choices(

            string.ascii_uppercase + string.digits,

            k=8

        )

    )

    return f"{prefix}-{random_part}"


def current_time():

    return datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )


def success_response(data):

    return {

        "success": True,

        "data": data

    }


def error_response(message):

    return {

        "success": False,

        "error": message

    }


def normalize_text(text):

    return text.lower().strip()


def percentage(value):

    return round(value * 100, 2)