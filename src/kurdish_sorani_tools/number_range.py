"""
Kurdish Number Range - ڕیزی ژمارە
Convert number ranges to Kurdish words.
"""

import re
from .number_to_words import number_to_words


class KurdishNumberRange:
    """Kurdish number range utilities."""

    @staticmethod
    def to_words(from_num: int, to_num: int, separator: str = " تا ") -> str:
        """
        Convert a number range to Kurdish words.
        گۆڕینی ڕیزی ژمارە بۆ وشەی کوردی

        >>> KurdishNumberRange.to_words(1, 5)
        'یەک تا پێنج'
        """
        from_word = number_to_words(from_num)
        to_word = number_to_words(to_num)
        return f"{from_word}{separator}{to_word}"

    @staticmethod
    def parse_and_convert(range_str: str, separator: str = " تا ") -> str | None:
        """
        Parse a range string and convert to Kurdish words.
        گۆڕینی سترینگی ڕیز بۆ وشەی کوردی

        >>> KurdishNumberRange.parse_and_convert("1-5")
        'یەک تا پێنج'
        """
        parts = re.split(r"[-–—]", range_str)
        if len(parts) != 2:
            return None

        try:
            from_num = int(parts[0].strip())
            to_num = int(parts[1].strip())
        except ValueError:
            return None

        return KurdishNumberRange.to_words(from_num, to_num, separator)
