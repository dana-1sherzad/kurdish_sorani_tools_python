"""
Kurdish Form Validators - پشکنینی فۆرم
Validation functions for common form fields.
"""

import re


class KurdishValidators:
    """Kurdish form validation utilities."""

    @staticmethod
    def required(value: str | None, message: str | None = None) -> str | None:
        """
        Validate that a field is not empty.
        پشکنینی پڕبوونەوە

        Returns None if valid, error message if invalid.
        """
        if value is None or not value.strip():
            return message or "ئەم خانەیە پێویستە پڕ بکرێتەوە"
        return None

    @staticmethod
    def min_length(value: str | None, min_len: int, message: str | None = None) -> str | None:
        """Validate minimum length."""
        if value is None or len(value) < min_len:
            return message or f"بەلایەنی کەمەوە {min_len} پیت پێویستە"
        return None

    @staticmethod
    def max_length(value: str | None, max_len: int, message: str | None = None) -> str | None:
        """Validate maximum length."""
        if value is not None and len(value) > max_len:
            return message or f"نابێت لە {max_len} پیت زیاتر بێت"
        return None

    @staticmethod
    def email(value: str | None, message: str | None = None) -> str | None:
        """Validate email format."""
        if value is None or not value:
            return None
        pattern = r"^[\w\-.]+@([\w\-]+\.)+[\w\-]{2,4}$"
        if not re.match(pattern, value):
            return message or "ئیمەیلەکە هەڵەیە"
        return None

    @staticmethod
    def phone(value: str | None, message: str | None = None) -> str | None:
        """Validate Iraqi phone number."""
        if value is None or not value:
            return None
        digits = re.sub(r"[^\d]", "", value)
        if len(digits) != 11 or not digits.startswith("07"):
            return message or "ژمارەی مۆبایل هەڵەیە"
        return None

    @staticmethod
    def numeric(value: str | None, message: str | None = None) -> str | None:
        """Validate numeric input."""
        if value is None or not value:
            return None
        cleaned = re.sub(r"[,،]", "", value)
        try:
            float(cleaned)
            return None
        except ValueError:
            return message or "تەنها ژمارە بنووسە"

    @staticmethod
    def match(value: str | None, other: str, message: str | None = None) -> str | None:
        """Validate two values match."""
        if value != other:
            return message or "خانەکان وەک یەک نین"
        return None

    @staticmethod
    def kurdish_only(value: str | None, message: str | None = None) -> str | None:
        """Validate Kurdish-only text."""
        if value is None or not value:
            return None
        pattern = r"^[\u0600-\u06FF\u0750-\u077F\s\d.,،؟!]+$"
        if not re.match(pattern, value):
            return message or "تەنها کوردی بنووسە"
        return None
