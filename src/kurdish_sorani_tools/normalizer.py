"""
Kurdish Text Normalizer - نۆرمالکردنی دەقی کوردی
Normalize Arabic characters to Kurdish standard.
"""

import re


class KurdishNormalizer:
    """Kurdish text normalization utilities."""

    ARABIC_TO_KURDISH_MAP = {
        "ي": "ی",
        "ك": "ک",
        "ة": "ە",
        "ؤ": "وو",
        "أ": "ئ",
        "إ": "ئ",
        "آ": "ئا",
        "\u0649": "ی",  # ى (Alef Maksura)
        "\u06CC": "ی",  # ی (Farsi Yeh)
    }

    @staticmethod
    def normalize(text: str) -> str:
        """
        Normalize text by converting Arabic characters to Kurdish.
        نۆرمالکردنی دەق - گۆڕینی پیتەکانی عەرەبی بۆ کوردی

        >>> KurdishNormalizer.normalize("كتاب")
        'کتاب'
        """
        result = text
        for arabic, kurdish in KurdishNormalizer.ARABIC_TO_KURDISH_MAP.items():
            result = result.replace(arabic, kurdish)
        return result

    @staticmethod
    def remove_diacritics(text: str) -> str:
        """
        Remove diacritics (harakat) from text.
        سڕینەوەی هەرەکات لە دەق
        """
        return re.sub("[\u064B-\u065F\u0670]", "", text)

    @staticmethod
    def remove_tatweel(text: str) -> str:
        """
        Remove tatweel (kashida) from text.
        سڕینەوەی تاتوێ لە دەق
        """
        return text.replace("\u0640", "")

    @staticmethod
    def normalize_all(text: str) -> str:
        """
        Full normalization: normalize + remove diacritics + remove tatweel.
        نۆرمالکردنی تەواو
        """
        result = KurdishNormalizer.normalize(text)
        result = KurdishNormalizer.remove_diacritics(result)
        result = KurdishNormalizer.remove_tatweel(result)
        return result

    @staticmethod
    def normalize_spaces(text: str) -> str:
        """
        Normalize whitespace (multiple spaces to single).
        ستانداردکردنی بۆشاییەکان
        """
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def remove_zero_width(text: str) -> str:
        """
        Remove zero-width characters.
        سڕینەوەی Zero-Width characters
        """
        return re.sub("[\u200B-\u200F\u202A-\u202E\uFEFF]", "", text)
