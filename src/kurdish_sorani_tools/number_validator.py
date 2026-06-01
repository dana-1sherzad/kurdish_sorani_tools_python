"""
Kurdish Number Validator - پشکنینی ڕاستی ژمارە
Validate numbers in Kurdish and English formats.
"""

import re


class KurdishNumberValidator:
    """Kurdish number validation utilities."""

    @staticmethod
    def is_kurdish_number(text: str) -> bool:
        """
        Check if text is a Kurdish number (٠-٩).
        پشکنین ئایا سترینگەکە ژمارەی کوردییە

        >>> KurdishNumberValidator.is_kurdish_number("١٢٣")
        True
        """
        if not text:
            return False
        return bool(re.match(r"^[\u0660-\u0669\u06F0-\u06F9]+$", text))

    @staticmethod
    def is_english_number(text: str) -> bool:
        """
        Check if text is an English number.
        پشکنین ئایا سترینگەکە ژمارەی ئینگلیزییە
        """
        if not text:
            return False
        return bool(re.match(r"^\d+$", text))

    @staticmethod
    def is_number(text: str) -> bool:
        """
        Check if text is a number (Kurdish or English).
        پشکنین ئایا سترینگەکە ژمارەیە
        """
        if not text:
            return False
        cleaned = re.sub(r"[,،\s]", "", text)
        return bool(
            re.match(
                r"^[\d\u0660-\u0669\u06F0-\u06F9]+\.?[\d\u0660-\u0669\u06F0-\u06F9]*$",
                cleaned,
            )
        )

    @staticmethod
    def is_integer(text: str) -> bool:
        """Check if text is an integer (no decimal point)."""
        if not text:
            return False
        cleaned = re.sub(r"[,،\s]", "", text)
        return bool(re.match(r"^[\d\u0660-\u0669\u06F0-\u06F9]+$", cleaned))

    @staticmethod
    def is_decimal(text: str) -> bool:
        """Check if text is a decimal number."""
        if not text:
            return False
        cleaned = re.sub(r"[,،\s]", "", text)
        return bool(
            re.match(
                r"^[\d\u0660-\u0669\u06F0-\u06F9]+\.[\d\u0660-\u0669\u06F0-\u06F9]+$",
                cleaned,
            )
        )

    @staticmethod
    def is_negative(text: str) -> bool:
        """Check if text is a negative number."""
        if not text:
            return False
        return text.startswith("-") and KurdishNumberValidator.is_number(text[1:])
