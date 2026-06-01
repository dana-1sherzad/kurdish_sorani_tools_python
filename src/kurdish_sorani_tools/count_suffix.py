"""
Kurdish Count Suffix - پاشگری ژمارە
Auto-pluralize based on count.
"""

from .pluralization import KurdishPlural
from .digits import KU_DIGITS


class KurdishCountSuffix:
    """Kurdish count suffix utilities."""

    @staticmethod
    def _to_kurdish_digit(number: int) -> str:
        """Convert number to Kurdish digits."""
        return "".join(KU_DIGITS[int(d)] for d in str(number))

    @staticmethod
    def count(number: int, word: str, use_kurdish_digits: bool = False) -> str:
        """
        Number with appropriate singular/plural form.
        دانانی ژمارە لەگەڵ وشەی گونجاو

        >>> KurdishCountSuffix.count(0, "کتێب")
        'هیچ کتێبێک'
        >>> KurdishCountSuffix.count(1, "کتێب")
        '١ کتێب'
        >>> KurdishCountSuffix.count(5, "کتێب")
        '5 کتێبەکان'
        """
        if number == 0:
            return f"هیچ {word}ێک"
        if number == 1:
            return f"١ {word}"
        plural = KurdishPlural.plural_definite(word)
        num_str = KurdishCountSuffix._to_kurdish_digit(number) if use_kurdish_digits else str(number)
        return f"{num_str} {plural}"

    @staticmethod
    def count_simple(number: int, word: str, use_kurdish_digits: bool = False) -> str:
        """Simple count without pluralization."""
        num_str = KurdishCountSuffix._to_kurdish_digit(number) if use_kurdish_digits else str(number)
        return f"{num_str} {word}"
