"""
Kurdish Keyboard Layout Converter - گۆڕینی لەیاوتی کیبۆرد
Convert between English and Kurdish keyboard layouts.
"""


class KurdishKeyboard:
    """Kurdish keyboard layout converter."""

    EN_TO_KU_MAP = {
        "q": "ق", "w": "و", "e": "ە", "r": "ر", "t": "ت",
        "y": "ی", "u": "ئ", "i": "ح", "o": "ۆ", "p": "پ",
        "a": "ا", "s": "س", "d": "د", "f": "ف", "g": "گ",
        "h": "ه", "j": "ژ", "k": "ک", "l": "ل",
        "z": "ز", "x": "خ", "c": "ج", "v": "ڤ",
        "b": "ب", "n": "ن", "m": "م",
        "Q": "ق", "W": "وو", "E": "ێ", "R": "ڕ", "T": "ط",
        "Y": "ێ", "U": "ء", "I": "ع", "O": "ؤ", "P": "ث",
        "A": "ئا", "S": "ش", "D": "ذ", "F": "إ", "G": "غ",
        "H": "ھ", "J": "چ", "K": "ك", "L": "ڵ",
        "Z": "ض", "X": "ص", "C": "چ", "V": "ظ",
        "B": "ب", "N": "ن", "M": "م",
    }

    @staticmethod
    def en_to_ku(text: str) -> str:
        """
        Convert English keyboard layout to Kurdish.
        گۆڕینی دەقی ئینگلیزی بۆ کوردی (بەپێی لەیاوتی کیبۆرد)

        >>> KurdishKeyboard.en_to_ku("slaw")
        'سلاو'
        """
        result = []
        for char in text:
            result.append(KurdishKeyboard.EN_TO_KU_MAP.get(char, char))
        return "".join(result)

    @staticmethod
    def ku_to_en(text: str) -> str:
        """
        Convert Kurdish keyboard layout to English.
        گۆڕینی دەقی کوردی بۆ ئینگلیزی (بەپێی لەیاوتی کیبۆرد)
        """
        # Build reverse map
        ku_to_en_map = {}
        for en, ku in KurdishKeyboard.EN_TO_KU_MAP.items():
            if ku not in ku_to_en_map:
                ku_to_en_map[ku] = en

        result = []
        for char in text:
            result.append(ku_to_en_map.get(char, char))
        return "".join(result)
