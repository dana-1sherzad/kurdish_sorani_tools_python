"""
Words to Number - گۆڕینی وشە بۆ ژمارە
Convert Kurdish words to numbers.
"""

import re
from .digits import convert_ku_to_en, convert_en_to_ku
from .commas import add_commas

UNITS = {
    "هیچ": 0, "سفر": 0,
    "یەک": 1, "دو": 2, "دوو": 2,
    "سێ": 3, "چار": 4, "چوار": 4,
    "پێنج": 5, "شەش": 6,
    "حەوت": 7, "حەفت": 7,
    "هەشت": 8, "نۆ": 9,
    "دە": 10, "یازده": 11, "یانزه": 11,
    "دوازده": 12, "دوانزه": 12,
    "سێزدە": 13, "سیانزە": 13,
    "چاردە": 14, "چواردە": 14,
    "پانزده": 15, "پانزە": 15, "پازدە": 15,
    "شانزده": 16, "شانزە": 16, "شازدە": 16,
    "حەفە": 17, "حەودە": 17,
    "هەژدە": 18, "نۆزدە": 19,
    "بیست": 20, "سی": 30, "چل": 40,
    "پەنجا": 50, "شەست": 60, "شێست": 60,
    "حەفتا": 70, "حەوتا": 70,
    "هەشتا": 80, "نەوەد": 90, "نەوەت": 90,
}

TEN = {
    "سەد": 100, "سەت": 100,
    "دووسەد": 200, "دووسەت": 200,
    "سێسەت": 300, "سێسەد": 300,
    "چوارسەت": 400, "چوارسەد": 400,
    "چارسەد": 400, "چارسەت": 400,
    "پێنجسەت": 500, "پێنجسەد": 500,
    "شەشسەد": 600, "شەشسەت": 600,
    "حەوتسەد": 700, "حەوتسەت": 700,
    "حەفتسەد": 700, "حەفتسەت": 700,
    "هەشتسەد": 800, "هەشتسەت": 800,
    "نۆسەد": 900, "نۆسەت": 900,
}

MAGNITUDE = {
    "هەزار": 1000,
    "ملیۆن": 1000000, "میلیۆن": 1000000,
    "بلیۆن": 1000000000, "بیلیۆن": 1000000000,
    "میلیارد": 1000000000, "ملیار": 1000000000,
    "ملیارد": 1000000000, "میلیار": 1000000000,
    "تریلیون": 1000000000000, "ترلیۆن": 1000000000000,
}

TYPO_LIST = {
    "شەش سەد": "شەشسەد",
    "حەوت سەد": "حەوتسەد",
    "هەشت سەد": "هەشتسەد",
    "نۆ سەد": "نۆسەد",
    "پێنج سەد": "پێنجسەد",
    "چوار سەد": "چوارسەد",
    "سێ سەد": "سێسەد",
    "دوو سەد": "دووسەد",
    "دە هەزار": "دەهەزار",
    "سەد هەزار": "سەدهەزار",
    "دە ملیۆن": "دەملیۆن",
    "سەد ملیۆن": "سەدملیۆن",
    "دە بلیۆن": "دەبلیۆن",
    "سەد بلیۆن": "سەدبلیۆن",
}

JOINERS = ["و", " و "]
PREFIXES = ["نەرێنی", "ئەرێنی"]


def _replace_map(text: str, map_pattern: dict) -> str:
    """Replace multiple patterns in text."""
    for key, value in map_pattern.items():
        text = text.replace(key, value)
    return text


def _tokenize(words: str) -> list:
    """Tokenize Kurdish number words."""
    temp = _replace_map(words, TYPO_LIST)
    result = []
    for element in temp.split(" "):
        if element != JOINERS[0]:
            result.append(element)
    return result


def _compute(tokens: list) -> int:
    """Compute the numeric value from tokens."""
    total = 0
    is_negative = False

    for element in tokens:
        token = convert_ku_to_en(element)

        if token == PREFIXES[0]:
            is_negative = True
        elif token in UNITS:
            total += UNITS[token]
        elif token in TEN:
            total += TEN[token]
        elif token.isdigit():
            total += int(token)
        elif token in MAGNITUDE:
            total *= MAGNITUDE[token]

    return total * -1 if is_negative else total


def words_to_number(words: str) -> int | None:
    """
    Convert Kurdish words to a number.
    گۆڕینی وشەی کوردی بۆ ژمارە

    >>> words_to_number("سەد و بیست و پێنج")
    125
    >>> words_to_number("یەک هەزار")
    1000
    """
    if not words:
        return None

    # Remove ordinal suffix
    words = re.sub(r"من$", "", words, flags=re.IGNORECASE)
    words = re.sub(r"(ەم|یەم)$", "", words)

    return _compute(_tokenize(words))


def words_to_number_string(
    words: str,
    digits: str = "en",
    add_comma: bool = False,
) -> str | None:
    """
    Convert Kurdish words to a number string.
    گۆڕینی وشەی کوردی بۆ سترینگی ژمارە

    >>> words_to_number_string("سەد و بیست و پێنج")
    '125'
    >>> words_to_number_string("سەد و بیست و پێنج", digits="ku")
    '١٢٥'
    """
    result = words_to_number(words)
    if result is None:
        return None

    result_str = add_commas(result) if add_comma else str(result)

    if digits in ("ku", "ckb"):
        return convert_en_to_ku(result_str)
    return result_str
