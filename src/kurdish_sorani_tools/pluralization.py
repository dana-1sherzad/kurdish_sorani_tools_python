"""
Kurdish Pluralization - کۆکردنەوەی وشەکان
Kurdish plural forms.
"""


class KurdishPlural:
    """Kurdish pluralization utilities."""

    PLURAL_SUFFIX = "ەکان"
    INDEFINITE_PLURAL_SUFFIX = "ان"

    @staticmethod
    def _ends_with_vowel(word: str) -> bool:
        """Check if word ends with a vowel."""
        if not word:
            return False
        return word[-1] in "اەێۆوی"

    @staticmethod
    def plural_definite(word: str) -> str:
        """
        Make a word plural (definite form with ەکان).
        کۆکردنەوەی وشە بە پاشگری "ەکان" (دیاری)

        >>> KurdishPlural.plural_definite("کتێب")
        'کتێبەکان'
        >>> KurdishPlural.plural_definite("باڵندە")
        'باڵندەکان'
        """
        if not word:
            return word
        if KurdishPlural._ends_with_vowel(word):
            return f"{word}کان"
        return f"{word}{KurdishPlural.PLURAL_SUFFIX}"

    @staticmethod
    def plural_indefinite(word: str) -> str:
        """
        Make a word plural (indefinite form with ان).
        کۆکردنەوەی وشە بە پاشگری "ان" (نادیاری)

        >>> KurdishPlural.plural_indefinite("کتێب")
        'کتێبان'
        """
        if not word:
            return word
        if KurdishPlural._ends_with_vowel(word):
            return f"{word}یان"
        return f"{word}{KurdishPlural.INDEFINITE_PLURAL_SUFFIX}"

    @staticmethod
    def singular(word: str) -> str:
        """
        Remove plural suffix and return singular form.
        سڕینەوەی پاشگری کۆ و گەڕاندنەوەی تاک

        >>> KurdishPlural.singular("کتێبەکان")
        'کتێب'
        """
        if word.endswith("ەکان"):
            return word[:-4]
        if word.endswith("کان"):
            return word[:-3]
        if word.endswith("یان"):
            return word[:-3]
        if word.endswith("ان"):
            return word[:-2]
        return word

    @staticmethod
    def is_plural(word: str) -> bool:
        """
        Check if a word is plural.
        پشکنین ئایا وشەکە کۆیە
        """
        return (
            word.endswith("ەکان")
            or word.endswith("کان")
            or word.endswith("یان")
            or word.endswith("ان")
        )

    @staticmethod
    def count(number: int, word: str, definite: bool = True) -> str:
        """
        Number with appropriate plural/singular form.
        دانانی ژمارە لەگەڵ وشەی کۆ/تاک

        >>> KurdishPlural.count(1, "کتێب")
        '١ کتێب'
        >>> KurdishPlural.count(3, "کتێب")
        '3 کتێبەکان'
        """
        if number == 1:
            return f"١ {word}"
        plural = (
            KurdishPlural.plural_definite(word)
            if definite
            else KurdishPlural.plural_indefinite(word)
        )
        return f"{number} {plural}"


def plural_definite(word: str) -> str:
    """Shortcut for KurdishPlural.plural_definite."""
    return KurdishPlural.plural_definite(word)


def plural_indefinite(word: str) -> str:
    """Shortcut for KurdishPlural.plural_indefinite."""
    return KurdishPlural.plural_indefinite(word)
