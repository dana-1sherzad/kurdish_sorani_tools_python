"""
Ordinal Suffix - پاشگری ڕێزبەندی
Add/remove ordinal suffixes for Kurdish numbers.
"""

import re


class KurdishOrdinal:
    """Kurdish ordinal number utilities."""

    _ORDINALS = {
        1: "یەکەم", 2: "دووەم", 3: "سێیەم",
        4: "چوارەم", 5: "پێنجەم", 6: "شەشەم",
        7: "حەوتەم", 8: "هەشتەم", 9: "نۆیەم",
        10: "دەیەم", 11: "یازدەیەم", 12: "دوازدەیەم",
        13: "سێزدەیەم", 14: "چواردەیەم", 15: "پازدەیەم",
        16: "شازدەیەم", 17: "حەڤدەیەم", 18: "هەژدەیەم",
        19: "نۆزدەیەم", 20: "بیستەم",
        30: "سییەم", 40: "چلەم", 50: "پەنجایەم",
        60: "شەستەم", 70: "حەفتایەم", 80: "هەشتایەم",
        90: "نەوەدەم", 100: "سەدەم", 1000: "هەزارەم",
    }

    @staticmethod
    def from_number(number: int) -> str:
        """
        Convert a number to its Kurdish ordinal form.
        گۆڕینی ژمارە بۆ ڕێزبەندی

        >>> KurdishOrdinal.from_number(1)
        'یەکەم'
        >>> KurdishOrdinal.from_number(5)
        'پێنجەم'
        """
        if number in KurdishOrdinal._ORDINALS:
            return KurdishOrdinal._ORDINALS[number]
        return f"{number}ەم"

    @staticmethod
    def add_suffix(word: str) -> str:
        """
        Add ordinal suffix to a word.
        زیادکردنی پاشگری ڕێزبەندی بۆ وشە

        >>> KurdishOrdinal.add_suffix("پێنج")
        'پێنجەم'
        """
        if not word:
            return word

        last_char = word[-1]
        vowels = "اەێۆوی"

        if last_char in vowels:
            return f"{word}یەم"
        if word.endswith("سێ"):
            return f"{word[:-1]}ێیەم"
        return f"{word}ەم"


def add_ordinal_suffix(word: str) -> str:
    """Add ordinal suffix to a word."""
    return KurdishOrdinal.add_suffix(word)


def remove_ordinal_suffix(word: str) -> str:
    """
    Remove ordinal suffix from a word.
    پاشگری ڕێزبەندی لادەبات

    >>> remove_ordinal_suffix("یەکەم")
    'یەک'
    """
    if not word:
        return word

    word = re.sub(r"مین$", "", word, flags=re.IGNORECASE)
    word = re.sub(r"(ام| اُم)$", "", word, flags=re.IGNORECASE)

    if word.endswith("سوم"):
        word = word[:-3] + "سه"
    elif word.endswith("م"):
        word = word[:-1]

    return word
