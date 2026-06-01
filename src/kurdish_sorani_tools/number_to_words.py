"""
Number to Words - گۆڕینی ژمارە بۆ وشەی کوردی
Convert numbers to Kurdish Sorani words.
"""

from .commas import remove_commas

# Constants
ZERO = "سفر"
AND = " و "
SCALE = ["", "هەزار", "ملیۆن", "ملیارد"]

NUMBER_TO_WORD = {
    0: "",
    1: "یەک",
    2: "دوو",
    3: "سێ",
    4: "چوار",
    5: "پێنج",
    6: "شەش",
    7: "حەوت",
    8: "هەشت",
    9: "نۆ",
    10: "دە",
    11: "یازده",
    12: "دوازده",
    13: "سێزدە",
    14: "چواردە",
    15: "پازدە",
    16: "شازدە",
    17: "حەڤدە",
    18: "هەژدە",
    19: "نۆزدە",
    20: "بیست",
    30: "سی",
    40: "چل",
    50: "پەنجا",
    60: "شەست",
    70: "حەفتا",
    80: "هەشتا",
    90: "نەوەد",
    100: "سەد",
    200: "دوو سەد",
    300: "سێ سەد",
    400: "چوار سەد",
    500: "پێنج سەد",
    600: "شەش سەد",
    700: "حەوت سەد",
    800: "هەشت سەد",
    900: "نۆ سەد",
}


def _num_to_word(number: int) -> str:
    """Convert a number with 3 or fewer digits to Kurdish words."""
    unit = 100
    result = ""

    while unit > 0:
        if (number // unit) * unit != 0:
            if number in NUMBER_TO_WORD:
                result += NUMBER_TO_WORD[number]
                break
            else:
                result += f"{NUMBER_TO_WORD[(number // unit) * unit]} و "
                number %= unit
        unit //= 10

    return result


def number_to_words(number: int, ordinal: bool = False) -> str:
    """
    Convert an integer to Kurdish words.
    گۆڕینی ژمارە بۆ نووسینی کوردی

    >>> number_to_words(0)
    'سفر'
    >>> number_to_words(125)
    'سەد و بیست و پێنج'
    >>> number_to_words(1000)
    'یەک هەزار'
    >>> number_to_words(1500000)
    'یەک ملیۆن و پێنج سەد هەزار'
    """
    if number == 0:
        return ZERO

    result = []
    is_negative = number < 0
    number = abs(number)

    while number > 0:
        result.append(_num_to_word(number % 1000))
        number //= 1000

    if len(result) > 4:
        return ""

    for i in range(len(result)):
        if result[i] != "" and i != 0:
            result[i] += f" {SCALE[i]} و "

    result.reverse()
    words = "".join(result)

    if words.endswith(AND):
        words = words[:-3]

    words = words.strip()
    if is_negative:
        words = f"سالب {words}"

    return words


def number_to_words_string(number_str: str, ordinal: bool = False) -> str | None:
    """
    Convert a number string (may contain commas) to Kurdish words.
    گۆڕینی سترینگی ژمارە بۆ وشەی کوردی

    >>> number_to_words_string("1,500,000")
    'یەک ملیۆن و پێنج سەد هەزار'
    """
    if not number_str:
        return None
    if number_str == "0":
        return ZERO

    num = int(remove_commas(number_str))
    return number_to_words(num, ordinal=ordinal)
