"""
Kurdish String Utilities - ئامرازەکانی سترینگ
String manipulation utilities for Kurdish text.
"""

import re


class KurdishStringUtils:
    """Kurdish string utility functions."""

    @staticmethod
    def to_slug(text: str) -> str:
        """
        Create a URL slug from Kurdish text.
        دروستکردنی slug بۆ URL لە دەقی کوردی

        >>> KurdishStringUtils.to_slug("سڵاو جیهان")
        'سڵاو-جیهان'
        """
        result = text.strip().lower()
        result = re.sub(r"\s+", "-", result)
        result = re.sub(r"[^\u0600-\u06FF\u0750-\u077F\w\-]", "", result)
        result = re.sub(r"-+", "-", result)
        result = re.sub(r"^-+|-+$", "", result)
        return result

    @staticmethod
    def word_count(text: str) -> int:
        """
        Count words in text.
        ژمردنی وشەکان لە دەق

        >>> KurdishStringUtils.word_count("سڵاو جیهان")
        2
        """
        if not text.strip():
            return 0
        return len(text.strip().split())

    @staticmethod
    def char_count(text: str, include_spaces: bool = False) -> int:
        """
        Count characters in text.
        ژمردنی پیتەکان

        >>> KurdishStringUtils.char_count("سڵاو جیهان")
        9
        """
        if include_spaces:
            return len(text)
        return len(re.sub(r"\s", "", text))

    @staticmethod
    def truncate_words(text: str, max_words: int, ellipsis: str = "...") -> str:
        """
        Truncate text to a maximum number of words.
        بڕینی دەق بە ژمارەی وشەی دیاریکراو

        >>> KurdishStringUtils.truncate_words("یەک دوو سێ چوار پێنج", 3)
        'یەک دوو سێ...'
        """
        words = text.strip().split()
        if len(words) <= max_words:
            return text
        return " ".join(words[:max_words]) + ellipsis

    @staticmethod
    def capitalize(text: str) -> str:
        """Capitalize first character (for Latin characters in mixed text)."""
        if not text:
            return text
        return text[0].upper() + text[1:]

    @staticmethod
    def reverse(text: str) -> str:
        """
        Reverse Kurdish text.
        پێچەوانەکردنی دەق

        >>> KurdishStringUtils.reverse("سڵاو")
        'واڵس'
        """
        return text[::-1]

    @staticmethod
    def remove_numbers(text: str) -> str:
        """
        Remove all numbers from text.
        سڕینەوەی هەموو ژمارەکان لە دەق
        """
        return re.sub(r"[\d\u0660-\u0669\u06F0-\u06F9]", "", text)

    @staticmethod
    def extract_numbers(text: str) -> str:
        """
        Extract only numbers from text.
        هەڵگرتنی ژمارەکان تەنها لە دەق
        """
        matches = re.findall(r"[\d\u0660-\u0669\u06F0-\u06F9]+", text)
        return " ".join(matches)
