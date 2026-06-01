"""
Kurdish Detection - دۆزینەوەی کوردی
Check if text contains Kurdish characters.
"""

import re

# Kurdish/Arabic Unicode ranges
KU_ALPHABET = "ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنوۆهەیێ"
KU_NUMBERS = "٠١٢٣٤٥٦٧٨٩"
KU_SHORT_VOWELS = "\u064E\u064F\u0650"  # َُِ
KU_OTHERS = "\u200C\u0622\u0627\u064B"  # ‌آاً
KU_MIXED_WITH_ARABIC = "ًٌٍَُِّْٰٔءك\u200Cةۀأإيـئؤ،"

KU_TEXT = KU_ALPHABET + KU_NUMBERS + KU_SHORT_VOWELS + KU_OTHERS
KU_COMPLEX_TEXT = KU_TEXT + KU_MIXED_WITH_ARABIC

TRIM_PATTERN = re.compile(r'["\'\-+()؟\s.]')


def is_kurdish(text: str, is_complex: bool = False) -> bool:
    """
    Check if the entire text is Kurdish.
    چێکی ئینپووتەکە دەکات بزانی دەقەکە کوردیە یاخوود نا

    >>> is_kurdish("سڵاو")
    True
    >>> is_kurdish("Hello")
    False
    """
    raw_text = TRIM_PATTERN.sub("", text)
    if not raw_text:
        return False
    ku_chars = KU_COMPLEX_TEXT if is_complex else KU_TEXT
    pattern = f"^[{re.escape(ku_chars)}]+$"
    return bool(re.match(pattern, raw_text))


def has_kurdish(text: str, is_complex: bool = False) -> bool:
    """
    Check if text contains any Kurdish characters.
    ئەگەر تەنانەت یەک پیتی کوردیشی تیابوو True دەگەڕێنێتەوە

    >>> has_kurdish("Hello سڵاو")
    True
    >>> has_kurdish("Hello World")
    False
    """
    ku_chars = KU_COMPLEX_TEXT if is_complex else KU_TEXT
    pattern = f"[{re.escape(ku_chars)}]"
    return bool(re.search(pattern, text))
