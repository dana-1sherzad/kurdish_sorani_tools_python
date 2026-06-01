"""
Kurdish Phone Number - ژمارەی مۆبایل
Format and validate Iraqi/Kurdistan phone numbers.
"""

import re
from .digits import convert_en_to_ku


class KurdishPhone:
    """Kurdish phone number utilities."""

    OPERATORS_BY_PREFIX = {
        "075": "کۆڕەک",
        "077": "ئاسیاسێل",
        "078": "زەین",
        "079": "فاستلینک",
    }

    @staticmethod
    def _normalize(phone_number: str) -> str:
        """Normalize phone number."""
        digits = re.sub(r"[^\d]", "", phone_number)
        if digits.startswith("00964"):
            digits = "0" + digits[5:]
        elif digits.startswith("964"):
            digits = "0" + digits[3:]
        return digits

    @staticmethod
    def format(phone_number: str, use_kurdish_digits: bool = False) -> str:
        """
        Format an Iraqi phone number.
        فۆرماتکردنی ژمارەی مۆبایل

        >>> KurdishPhone.format("07501234567")
        '0750 123 4567'
        """
        digits = KurdishPhone._normalize(phone_number)
        if len(digits) != 11:
            return phone_number
        formatted = f"{digits[:4]} {digits[4:7]} {digits[7:]}"
        if use_kurdish_digits:
            return convert_en_to_ku(formatted)
        return formatted

    @staticmethod
    def is_valid(phone_number: str) -> bool:
        """
        Validate an Iraqi mobile phone number.
        پشکنینی ڕاستی ژمارەی مۆبایلی عراقی

        >>> KurdishPhone.is_valid("07501234567")
        True
        >>> KurdishPhone.is_valid("12345")
        False
        """
        digits = KurdishPhone._normalize(phone_number)
        if len(digits) != 11:
            return False
        if not digits.startswith("07"):
            return False
        return True

    @staticmethod
    def get_operator(phone_number: str) -> str | None:
        """
        Detect the mobile operator.
        ناسینەوەی ئۆپەرەیتەر

        >>> KurdishPhone.get_operator("07501234567")
        'کۆڕەک'
        """
        digits = KurdishPhone._normalize(phone_number)
        if len(digits) < 4:
            return None
        prefix = digits[:3]
        return KurdishPhone.OPERATORS_BY_PREFIX.get(prefix)

    @staticmethod
    def to_international(phone_number: str) -> str:
        """
        Convert to international format.
        گۆڕین بۆ فۆرماتی نێودەوڵەتی

        >>> KurdishPhone.to_international("07501234567")
        '+9647501234567'
        """
        digits = KurdishPhone._normalize(phone_number)
        if digits.startswith("0"):
            digits = "964" + digits[1:]
        return f"+{digits}"


def format_phone(phone_number: str, use_kurdish_digits: bool = False) -> str:
    """Shortcut for KurdishPhone.format."""
    return KurdishPhone.format(phone_number, use_kurdish_digits)
