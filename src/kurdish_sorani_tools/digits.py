"""
Digit Conversion - گۆڕینی ژمارە
Convert between English and Kurdish (Eastern Arabic) digits.
"""

KU_DIGITS = "٠١٢٣٤٥٦٧٨٩"
EN_DIGITS = "0123456789"


def convert_en_to_ku(text: str) -> str:
    """
    Convert English digits to Kurdish (Eastern Arabic) digits.
    ژمارەی ئینگلیزی دەگۆڕێت بۆ کوردی

    >>> convert_en_to_ku("123")
    '١٢٣'
    """
    result = text
    for i in range(10):
        result = result.replace(str(i), KU_DIGITS[i])
    return result


def convert_ku_to_en(text: str) -> str:
    """
    Convert Kurdish (Eastern Arabic) digits to English digits.
    ژمارەی کوردی دەگۆڕێت بۆ ئینگلیزی

    >>> convert_ku_to_en("١٢٣")
    '123'
    """
    result = text
    for i in range(10):
        result = result.replace(KU_DIGITS[i], str(i))
    return result
