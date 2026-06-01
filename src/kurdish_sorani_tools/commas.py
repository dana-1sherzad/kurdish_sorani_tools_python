"""
Comma Formatting - فاریزە
Add/remove thousand separators.
"""

import re
from .digits import convert_ku_to_en
from .is_kurdish import is_kurdish


def add_commas(number) -> str:
    """
    Add thousand separators to a number.
    فاریزە زیاد دەکات بۆ جیاکردنەوەی هەزاران

    >>> add_commas(1500000)
    '1,500,000'
    >>> add_commas("2500")
    '2,500'
    """
    if not isinstance(number, (int, float, str)):
        raise TypeError("پێویستە سترینگ بێ یان ئینتیجەر")

    number_str = str(number) if not isinstance(number, str) else number
    en_number_str = convert_ku_to_en(number_str) if is_kurdish(number_str) else number_str

    parts = en_number_str.split(".")
    integer_part = re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1,", parts[0])
    decimal_part = f".{parts[1]}" if len(parts) > 1 else ""

    return integer_part + decimal_part


def remove_commas(number_str: str):
    """
    Remove thousand separators from a number string.
    فاریزەکان لادەبات لە ژمارە

    >>> remove_commas("1,500,000")
    1500000
    """
    if "," in number_str:
        number_str = re.sub(r",\s?", "", number_str)

    result = float(number_str) if "." in number_str else int(number_str)
    return result
