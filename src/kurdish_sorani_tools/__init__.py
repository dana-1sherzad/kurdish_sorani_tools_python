"""
Kurdish Sorani Tools - Python
ئامرازەکانی کوردی سۆرانی بۆ پایتۆن

A comprehensive Python package providing utilities for the Kurdish Sorani language.
"""

from .digits import convert_en_to_ku, convert_ku_to_en
from .commas import add_commas, remove_commas
from .number_to_words import number_to_words, number_to_words_string
from .words_to_number import words_to_number, words_to_number_string
from .is_kurdish import is_kurdish, has_kurdish
from .url_fix import fix_url
from .ordinal import KurdishOrdinal, add_ordinal_suffix, remove_ordinal_suffix
from .date_time import KurdishDateTime, kurdish_date_format
from .keyboard import KurdishKeyboard
from .normalizer import KurdishNormalizer
from .currency import KurdishCurrency, CurrencyType
from .text_direction import KurdishTextDirection
from .pluralization import KurdishPlural, plural_definite, plural_indefinite
from .string_utils import KurdishStringUtils
from .relative_time import KurdishRelativeTime, kurdish_relative_time
from .phone import KurdishPhone, format_phone
from .number_range import KurdishNumberRange
from .sentence import KurdishSentence
from .number_validator import KurdishNumberValidator
from .validators import KurdishValidators
from .greeting import KurdishGreeting, kurdish_greeting
from .count_suffix import KurdishCountSuffix
from .calendar import KurdishCalendar, HijriDate, KurdishDate
from .color import KurdishColor
from .digit_to_word import digit_to_word, StrType

__version__ = "0.1.1"
__author__ = "Dana Sherzad"

__all__ = [
    # Digits
    "convert_en_to_ku",
    "convert_ku_to_en",
    # Commas
    "add_commas",
    "remove_commas",
    # Number to words
    "number_to_words",
    "number_to_words_string",
    # Words to number
    "words_to_number",
    "words_to_number_string",
    # Kurdish detection
    "is_kurdish",
    "has_kurdish",
    # URL fix
    "fix_url",
    # Ordinal
    "KurdishOrdinal",
    "add_ordinal_suffix",
    "remove_ordinal_suffix",
    # Date/Time
    "KurdishDateTime",
    "kurdish_date_format",
    # Keyboard
    "KurdishKeyboard",
    # Normalizer
    "KurdishNormalizer",
    # Currency
    "KurdishCurrency",
    "CurrencyType",
    # Text direction
    "KurdishTextDirection",
    # Pluralization
    "KurdishPlural",
    "plural_definite",
    "plural_indefinite",
    # String utils
    "KurdishStringUtils",
    # Relative time
    "KurdishRelativeTime",
    "kurdish_relative_time",
    # Phone
    "KurdishPhone",
    "format_phone",
    # Number range
    "KurdishNumberRange",
    # Sentence
    "KurdishSentence",
    # Number validator
    "KurdishNumberValidator",
    # Validators
    "KurdishValidators",
    # Greeting
    "KurdishGreeting",
    "kurdish_greeting",
    # Count suffix
    "KurdishCountSuffix",
    # Calendar
    "KurdishCalendar",
    "HijriDate",
    "KurdishDate",
    # Color
    "KurdishColor",
    # Digit to word
    "digit_to_word",
    "StrType",
]
