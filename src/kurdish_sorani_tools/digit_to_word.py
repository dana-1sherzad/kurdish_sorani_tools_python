"""
Digit to Word - گۆڕینی ژمارە بۆ وشە
Convert numbers to Kurdish words with different modes.
"""

from enum import Enum


class StrType(Enum):
    """Type of number-to-word conversion."""
    NUM_WORD = "num_word"  # "25 هەزار"
    STR_WORD = "str_word"  # "بیست و پێنج هەزار"


def digit_to_word(
    number: str | None,
    str_type: StrType = StrType.STR_WORD,
    separator: str = ",",
    is_money: bool = False,
    bigger_than_capacity: str = "دەبێت درێژی ژمارەکە لە 16 ژمارە کەمتر بێت",
) -> str:
    """
    Convert a number string to Kurdish words.
    گۆڕینی ژمارە بۆ وشەی کوردی

    >>> digit_to_word("1500000", StrType.NUM_WORD)
    '1 ملیۆن و 500 هەزار'
    >>> digit_to_word("25", StrType.STR_WORD)
    'بیست و پێنج'
    """
    if number is None or number == "":
        return ""
    if len(number) >= 15:
        return bigger_than_capacity

    num_int = number.replace(separator, "")

    if str_type == StrType.NUM_WORD:
        return _num_word(num_int, is_money)
    else:
        return _str_word(num_int, is_money)


def _num_word(input_number: str, is_money: bool) -> str:
    """Convert using numeric representation (e.g., '25 هەزار')."""
    try:
        number = int(input_number)
        if number == 0:
            return "سفر"

        padded = input_number.zfill(15)
        trillion = int(padded[0:3])
        billions = int(padded[3:6])
        millions = int(padded[6:9])
        hundred_thousands = int(padded[9:12])
        thousands = int(padded[12:15])

        result = ""
        if trillion != 0:
            result += f"{trillion} ترلیۆن و"
        if billions != 0:
            result += f"{billions} ملیارد و"
        if millions != 0:
            result += f"{millions} ملیۆن و"
        if hundred_thousands != 0:
            result += f"{hundred_thousands} هەزار و"

        if thousands == 0 and result.endswith(" و"):
            result = result[:-2]
        elif thousands != 0:
            result += str(thousands)

        result = result.strip()
        return f"{result} دیناری عراقی" if is_money else result
    except ValueError:
        return "هەڵبژاردنی جۆریەتی هەڵەیە"


def _str_word(input_number: str, is_money: bool) -> str:
    """Convert using full word representation."""
    try:
        number = int(input_number)
        if number == 0:
            return "سفر"

        padded = input_number.zfill(15)
        trillion = int(padded[0:3])
        billions = int(padded[3:6])
        millions = int(padded[6:9])
        hundred_thousands = int(padded[9:12])
        thousands = int(padded[12:15])

        result = ""
        if trillion != 0:
            word = _convert_num(trillion)
            result += f"{word} ترلیۆن و" if trillion > 1 else f"{word} ترلیۆن "
        if billions != 0:
            result += f"{_convert_num(billions)} ملیارد و"
        if millions != 0:
            result += f"{_convert_num(millions)} ملیۆن و"
        if hundred_thousands != 0:
            if hundred_thousands == 1:
                result += "هەزار و"
            else:
                result += f"{_convert_num(hundred_thousands)} هەزار و"

        result += _convert_num(thousands)

        if result.endswith(" و"):
            result = result[:-2]

        result = result.strip()
        return f"{result} دیناری عراقی" if is_money else result
    except ValueError:
        return "هەڵبژاردنی جۆریەتی هەڵەیە"


def _convert_num(number: int) -> str:
    """Convert a number (0-999) to Kurdish words."""
    tens_names = [
        "", " ده و", " بیست و", " سی و", " چل و",
        " پەنجا و", " شەست و", " حەفتا و", " هەشتا و", " نەوەد و",
    ]
    num_names = [
        "", " یەک", " دوو", " سێ", " چوار", " پێنج",
        " شەش", " حەوت", " هەشت", " نۆ", " ده",
        " یازده", " دوازده", " سێزده", " چوارده", " پازده",
        " شازده", " حەڤدە", " هەژدە", " نۆزدە",
    ]
    thousands_names = [
        "", " سەد و", " دوو سەد و", " سێ سەد و", " چوار سەد و",
        " پێنج سەد و", " شەش سەد و", " حەوت سەد و", " هەشت سەد و", " نۆ سەد و",
    ]

    if number % 100 < 20:
        so_far = num_names[number % 100]
        number = number // 100
    else:
        so_far = num_names[number % 10]
        number = number // 10
        so_far = tens_names[number % 10] + so_far
        number = number // 10

    if number == 0:
        if so_far.endswith(" و"):
            so_far = so_far[:-2]
        return so_far.strip()

    result = (thousands_names[number] + so_far).strip()
    if result.endswith(" و") or result.endswith("و "):
        result = result[:-2].strip()
    return result
