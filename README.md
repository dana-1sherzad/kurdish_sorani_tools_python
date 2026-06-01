# Kurdish Sorani Tools - Python 🇮🇶

<div align="center">

**ئامرازەکانی کوردی سۆرانی بۆ پایتۆن**

A comprehensive Python package providing 25+ utilities for the Kurdish Sorani (سۆرانی) language.

[![PyPI version](https://badge.fury.io/py/kurdish-sorani-tools.svg)](https://pypi.org/project/kurdish-sorani-tools/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📦 Installation

```bash
pip install kurdish-sorani-tools
```

---

## 🚀 Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Number to Words | گۆڕینی ژمارە بۆ وشەی کوردی |
| 2 | Words to Number | گۆڕینی وشەی کوردی بۆ ژمارە |
| 3 | Digit Conversion | گۆڕینی ژمارە (ئینگلیزی ↔ کوردی) |
| 4 | Comma Formatting | فاریزە (جیاکەرەوەی هەزاران) |
| 5 | Kurdish Detection | دۆزینەوەی دەقی کوردی |
| 6 | URL Fix | چاککردنی لینک |
| 7 | Ordinal Suffix | پاشگری ڕێزبەندی (یەکەم، دووەم...) |
| 8 | Date/Time | بەروار و کاتی کوردی |
| 9 | Keyboard Converter | گۆڕینی لەیاوتی کیبۆرد |
| 10 | Text Normalizer | نۆرمالکردنی دەق |
| 11 | Currency Formatter | فۆرماتکردنی دراو |
| 12 | Text Direction | دیاریکردنی ئاڕاستەی دەق (RTL/LTR) |
| 13 | Pluralization | کۆکردنەوەی وشەکان |
| 14 | String Utilities | ئامرازەکانی سترینگ |
| 15 | Relative Time | کاتی نسبی |
| 16 | Phone Number | ژمارەی مۆبایلی عراقی |
| 17 | Number Range | ڕیزی ژمارە بۆ وشە |
| 18 | Sentence Utils | ئامرازەکانی ڕستە |
| 19 | Number Validator | پشکنینی ژمارە |
| 20 | Form Validators | پشکنینی فۆرم |
| 21 | Greeting | سڵاوکردن بەپێی کات |
| 22 | Count Suffix | پاشگری ژمارە (ئۆتۆ-کۆکردنەوە) |
| 23 | Calendar | ڕۆژژمێری هیجری و کوردی |
| 24 | Color Names | ناوی ڕەنگەکان بە کوردی |
| 25 | Digit to Word | گۆڕینی ژمارە بە دوو شێوە |

---

## 📖 Full Usage Guide

### 1. Number to Words — گۆڕینی ژمارە بۆ وشە

```python
from kurdish_sorani_tools import number_to_words, number_to_words_string

# Basic conversion
print(number_to_words(0))          # سفر
print(number_to_words(7))          # حەوت
print(number_to_words(25))         # بیست و پێنج
print(number_to_words(100))        # سەد
print(number_to_words(125))        # سەد و بیست و پێنج
print(number_to_words(1000))       # یەک هەزار
print(number_to_words(12345))      # دوازده هەزار و سێ سەد و چل و پێنج
print(number_to_words(1000000))    # یەک ملیۆن
print(number_to_words(1500000))    # یەک ملیۆن و پێنج سەد هەزار
print(number_to_words(-42))        # سالب چل و دوو

# From string with commas
print(number_to_words_string("1,500,000"))  # یەک ملیۆن و پێنج سەد هەزار
```

### 2. Words to Number — گۆڕینی وشە بۆ ژمارە

```python
from kurdish_sorani_tools import words_to_number, words_to_number_string

print(words_to_number("سەد و بیست و پێنج"))     # 125
print(words_to_number("یەک هەزار"))              # 1000
print(words_to_number("پێنج ملیۆن"))             # 5000000

# Return as string with Kurdish digits
print(words_to_number_string("سەد و بیست", digits="ku"))  # ١٢٠

# Return with commas
print(words_to_number_string("یەک ملیۆن", add_comma=True))  # 1,000,000
```

### 3. Digit Conversion — گۆڕینی ژمارە

```python
from kurdish_sorani_tools import convert_en_to_ku, convert_ku_to_en

# English to Kurdish digits
print(convert_en_to_ku("0123456789"))   # ٠١٢٣٤٥٦٧٨٩
print(convert_en_to_ku("2025/06/01"))   # ٢٠٢٥/٠٦/٠١

# Kurdish to English digits
print(convert_ku_to_en("١٢٣٤٥"))       # 12345
print(convert_ku_to_en("٢٠٢٥"))        # 2025
```

### 4. Comma Formatting — فاریزە

```python
from kurdish_sorani_tools import add_commas, remove_commas

# Add thousand separators
print(add_commas(1500000))       # 1,500,000
print(add_commas("2500000"))     # 2,500,000
print(add_commas(1234.56))       # 1,234.56

# Remove separators
print(remove_commas("1,500,000"))  # 1500000
```

### 5. Kurdish Detection — دۆزینەوەی کوردی

```python
from kurdish_sorani_tools import is_kurdish, has_kurdish

# Check if entire text is Kurdish
print(is_kurdish("سڵاو جیهان"))      # True
print(is_kurdish("Hello World"))      # False
print(is_kurdish("سڵاو Hello"))      # False (mixed)

# Check if text contains any Kurdish
print(has_kurdish("Hello سڵاو"))      # True
print(has_kurdish("Hello World"))      # False
```

### 6. URL Fix — چاککردنی لینک

```python
from kurdish_sorani_tools import fix_url

print(fix_url("https://example.com/my file.pdf"))
# https://example.com/my%20file.pdf

print(fix_url("https://example.com/کوردی سۆرانی"))
# https://example.com/کوردی%20سۆرانی
```

### 7. Ordinal Suffix — پاشگری ڕێزبەندی

```python
from kurdish_sorani_tools import KurdishOrdinal, add_ordinal_suffix, remove_ordinal_suffix

# Number to ordinal
print(KurdishOrdinal.from_number(1))    # یەکەم
print(KurdishOrdinal.from_number(2))    # دووەم
print(KurdishOrdinal.from_number(3))    # سێیەم
print(KurdishOrdinal.from_number(10))   # دەیەم
print(KurdishOrdinal.from_number(20))   # بیستەم
print(KurdishOrdinal.from_number(100))  # سەدەم

# Add suffix to word
print(KurdishOrdinal.add_suffix("پێنج"))   # پێنجەم
print(KurdishOrdinal.add_suffix("سێ"))     # سێیەم
```

### 8. Date/Time — بەروار و کات

```python
from kurdish_sorani_tools import KurdishDateTime, kurdish_date_format
from datetime import datetime

# Today's date
print(KurdishDateTime.today())
# دووشەممە, 01 حوزەیران 2026

# Custom format
now = datetime.now()
print(KurdishDateTime.format(now, "EEEE، dd MMMM yyyy"))
# دووشەممە، 01 حوزەیران 2026

print(KurdishDateTime.format(now, "dd/MM/yyyy HH:mm"))
# 01/06/2026 09:30

# Get names
print(KurdishDateTime.get_day_name(5))     # هەینی
print(KurdishDateTime.get_month_name(3))   # ئازار

# Shortcut function
print(kurdish_date_format(datetime(2024, 3, 21)))  # 21 ئازار 2024
```

### 9. Keyboard Converter — گۆڕینی کیبۆرد

```python
from kurdish_sorani_tools import KurdishKeyboard

# English layout → Kurdish characters
print(KurdishKeyboard.en_to_ku("slaw"))      # سلاو
print(KurdishKeyboard.en_to_ku("kwrdstan"))  # کوردستان

# Kurdish → English layout
print(KurdishKeyboard.ku_to_en("سلاو"))      # slaw
```

### 10. Text Normalizer — نۆرمالکردن

```python
from kurdish_sorani_tools import KurdishNormalizer

# Arabic → Kurdish character normalization
print(KurdishNormalizer.normalize("كتاب"))        # کتاب
print(KurdishNormalizer.normalize("يوم"))          # یوم
print(KurdishNormalizer.normalize("ة"))            # ە

# Remove diacritics (harakat)
print(KurdishNormalizer.remove_diacritics("كِتَابٌ"))  # كتاب

# Remove tatweel (kashida)
print(KurdishNormalizer.remove_tatweel("کـــوردی"))   # کوردی

# Full normalization (all combined)
print(KurdishNormalizer.normalize_all("كِتَابٌ يَوْمِي"))  # کتاب یومی

# Normalize spaces
print(KurdishNormalizer.normalize_spaces("سڵاو    جیهان"))  # سڵاو جیهان

# Remove zero-width characters
print(KurdishNormalizer.remove_zero_width("کوردی\u200Bسۆرانی"))  # کوردیسۆرانی
```

### 11. Currency Formatter — فۆرماتی دراو

```python
from kurdish_sorani_tools import KurdishCurrency, CurrencyType

# Iraqi Dinar
print(KurdishCurrency.format(1500000))
# 1,500,000 د.ع

print(KurdishCurrency.format(1500000, show_name=True))
# 1,500,000 دیناری عراقی

# With Kurdish digits
print(KurdishCurrency.format(25000, use_kurdish_digits=True))
# ٢٥,٠٠٠ د.ع

# US Dollar
print(KurdishCurrency.format(99.99, currency=CurrencyType.USD, decimal_places=2))
# 99.99 $

print(KurdishCurrency.format(99.99, currency=CurrencyType.USD, show_name=True, decimal_places=2))
# 99.99 دۆلاری ئەمریکی

# Euro
print(KurdishCurrency.format(500, currency=CurrencyType.EUR, show_name=True))
# 500 یۆرۆ

# All supported currencies: IQD, USD, EUR, GBP, IRR, TRL
```

### 12. Text Direction — ئاڕاستەی دەق

```python
from kurdish_sorani_tools import KurdishTextDirection

print(KurdishTextDirection.detect_direction("سڵاو"))    # rtl
print(KurdishTextDirection.detect_direction("Hello"))   # ltr

print(KurdishTextDirection.is_rtl("کوردی"))   # True
print(KurdishTextDirection.is_ltr("English"))  # True
```

### 13. Pluralization — کۆکردنەوە

```python
from kurdish_sorani_tools import KurdishPlural, plural_definite, plural_indefinite

# Definite plural (ەکان)
print(plural_definite("کتێب"))     # کتێبەکان
print(plural_definite("باڵندە"))   # باڵندەکان
print(plural_definite("ماڵ"))      # ماڵەکان

# Indefinite plural (ان)
print(plural_indefinite("کتێب"))   # کتێبان
print(plural_indefinite("باڵندە")) # باڵندەیان

# Singular (remove plural suffix)
print(KurdishPlural.singular("کتێبەکان"))  # کتێب
print(KurdishPlural.singular("ماڵان"))      # ماڵ

# Check if plural
print(KurdishPlural.is_plural("کتێبەکان"))  # True
print(KurdishPlural.is_plural("کتێب"))      # False

# Count with auto-plural
print(KurdishPlural.count(1, "کتێب"))   # ١ کتێب
print(KurdishPlural.count(5, "کتێب"))   # 5 کتێبەکان
```

### 14. String Utilities — ئامرازەکانی سترینگ

```python
from kurdish_sorani_tools import KurdishStringUtils

# Word count
print(KurdishStringUtils.word_count("سڵاو جیهان چۆنی"))  # 3

# Character count
print(KurdishStringUtils.char_count("سڵاو جیهان"))           # 9 (without spaces)
print(KurdishStringUtils.char_count("سڵاو جیهان", True))     # 10 (with spaces)

# URL slug
print(KurdishStringUtils.to_slug("سڵاو جیهان"))  # سڵاو-جیهان

# Truncate by words
print(KurdishStringUtils.truncate_words("یەک دوو سێ چوار پێنج", 3))
# یەک دوو سێ...

# Reverse text
print(KurdishStringUtils.reverse("سڵاو"))  # واڵس

# Remove numbers
print(KurdishStringUtils.remove_numbers("سڵاو ١٢٣ جیهان"))  # سڵاو  جیهان

# Extract numbers
print(KurdishStringUtils.extract_numbers("سڵاو ١٢٣ جیهان ٤٥٦"))  # ١٢٣ ٤٥٦
```

### 15. Relative Time — کاتی نسبی

```python
from kurdish_sorani_tools import KurdishRelativeTime, kurdish_relative_time
from datetime import datetime, timedelta

now = datetime.now()

# Past
print(kurdish_relative_time(now - timedelta(seconds=3)))    # ئێستا
print(kurdish_relative_time(now - timedelta(seconds=30)))   # 30 چرکە لەمەوپێش
print(kurdish_relative_time(now - timedelta(minutes=5)))    # 5 خولەک لەمەوپێش
print(kurdish_relative_time(now - timedelta(hours=3)))      # 3 کاتژمێر لەمەوپێش
print(kurdish_relative_time(now - timedelta(days=1)))       # دوێنێ
print(kurdish_relative_time(now - timedelta(days=5)))       # 5 ڕۆژ لەمەوپێش
print(kurdish_relative_time(now - timedelta(days=14)))      # 2 هەفتە لەمەوپێش
print(kurdish_relative_time(now - timedelta(days=45)))      # مانگێک لەمەوپێش
print(kurdish_relative_time(now - timedelta(days=400)))     # ساڵێک لەمەوپێش

# Future
print(kurdish_relative_time(now + timedelta(hours=2)))      # لە 2 کاتژمێردا
print(kurdish_relative_time(now + timedelta(days=1)))       # سبەینێ
```

### 16. Phone Number — ژمارەی مۆبایل

```python
from kurdish_sorani_tools import KurdishPhone, format_phone

# Format
print(format_phone("07501234567"))           # 0750 123 4567
print(KurdishPhone.format("07501234567", use_kurdish_digits=True))
# ٠٧٥٠ ١٢٣ ٤٥٦٧

# Validate
print(KurdishPhone.is_valid("07501234567"))  # True
print(KurdishPhone.is_valid("12345"))        # False

# Detect operator
print(KurdishPhone.get_operator("07501234567"))  # کۆڕەک
print(KurdishPhone.get_operator("07701234567"))  # ئاسیاسێل
print(KurdishPhone.get_operator("07801234567"))  # زەین
print(KurdishPhone.get_operator("07901234567"))  # فاستلینک

# International format
print(KurdishPhone.to_international("07501234567"))  # +9647501234567
```

### 17. Number Range — ڕیزی ژمارە

```python
from kurdish_sorani_tools import KurdishNumberRange

print(KurdishNumberRange.to_words(1, 5))       # یەک تا پێنج
print(KurdishNumberRange.to_words(10, 20))     # دە تا بیست

# Parse from string
print(KurdishNumberRange.parse_and_convert("1-10"))    # یەک تا دە
print(KurdishNumberRange.parse_and_convert("5-100"))   # پێنج تا سەد
```

### 18. Sentence Utilities — ئامرازەکانی ڕستە

```python
from kurdish_sorani_tools import KurdishSentence

# Split sentences
print(KurdishSentence.split_sentences("سڵاو. چۆنی؟ باشم"))
# ['سڵاو', 'چۆنی', 'باشم']

# Count sentences
print(KurdishSentence.sentence_count("سڵاو. چۆنی؟ باشم"))  # 3

# Ensure end punctuation
print(KurdishSentence.ensure_end_punctuation("سڵاو"))   # سڵاو.
print(KurdishSentence.ensure_end_punctuation("سڵاو."))  # سڵاو.
```

### 19. Number Validator — پشکنینی ژمارە

```python
from kurdish_sorani_tools import KurdishNumberValidator

print(KurdishNumberValidator.is_kurdish_number("١٢٣"))    # True
print(KurdishNumberValidator.is_kurdish_number("123"))     # False

print(KurdishNumberValidator.is_english_number("123"))     # True
print(KurdishNumberValidator.is_number("١٢٣"))            # True
print(KurdishNumberValidator.is_number("123"))             # True

print(KurdishNumberValidator.is_integer("123"))            # True
print(KurdishNumberValidator.is_decimal("12.5"))           # True
print(KurdishNumberValidator.is_negative("-5"))            # True
```

### 20. Form Validators — پشکنینی فۆرم

```python
from kurdish_sorani_tools import KurdishValidators

# Required field
print(KurdishValidators.required(""))       # ئەم خانەیە پێویستە پڕ بکرێتەوە
print(KurdishValidators.required("سڵاو"))   # None (valid)

# Min/Max length
print(KurdishValidators.min_length("ab", 3))   # بەلایەنی کەمەوە 3 پیت پێویستە
print(KurdishValidators.max_length("abcdef", 5))  # نابێت لە 5 پیت زیاتر بێت

# Email
print(KurdishValidators.email("test@test.com"))  # None (valid)
print(KurdishValidators.email("invalid"))        # ئیمەیلەکە هەڵەیە

# Phone
print(KurdishValidators.phone("07501234567"))    # None (valid)
print(KurdishValidators.phone("12345"))          # ژمارەی مۆبایل هەڵەیە

# Numeric
print(KurdishValidators.numeric("abc"))          # تەنها ژمارە بنووسە

# Kurdish only
print(KurdishValidators.kurdish_only("Hello"))   # تەنها کوردی بنووسە
print(KurdishValidators.kurdish_only("سڵاو"))    # None (valid)
```

### 21. Greeting — سڵاوکردن

```python
from kurdish_sorani_tools import KurdishGreeting, kurdish_greeting
from datetime import datetime

# Auto greeting based on current time
print(kurdish_greeting())  # بەیانی باش / ڕۆژ باش / ئێوارە باش / شەو باش

# Greeting by hour
print(KurdishGreeting.from_hour(8))    # بەیانی باش
print(KurdishGreeting.from_hour(14))   # ڕۆژ باش
print(KurdishGreeting.from_hour(19))   # ئێوارە باش
print(KurdishGreeting.from_hour(23))   # شەو باش

# Greeting with name
print(KurdishGreeting.with_name("دانا"))  # بەیانی باش، دانا
```

### 22. Count Suffix — پاشگری ژمارە

```python
from kurdish_sorani_tools import KurdishCountSuffix

print(KurdishCountSuffix.count(0, "کتێب"))   # هیچ کتێبێک
print(KurdishCountSuffix.count(1, "کتێب"))   # ١ کتێب
print(KurdishCountSuffix.count(5, "کتێب"))   # 5 کتێبەکان

# With Kurdish digits
print(KurdishCountSuffix.count(5, "کتێب", use_kurdish_digits=True))  # ٥ کتێبەکان
```

### 23. Calendar — ڕۆژژمێر

```python
from kurdish_sorani_tools import KurdishCalendar, HijriDate, KurdishDate
from datetime import datetime

now = datetime.now()

# Gregorian to Hijri
hijri = KurdishCalendar.gregorian_to_hijri(now)
print(hijri)  # 1447/12/15

# Format Hijri in Kurdish
print(KurdishCalendar.format_hijri(now))  # 15 زولحیججە 1447

# Gregorian to Kurdish (Rojhalati)
kurdish = KurdishCalendar.gregorian_to_kurdish(now)
print(kurdish)  # 2726/3/11

# Format Kurdish calendar
print(KurdishCalendar.format_kurdish(now))  # 11 جۆزەردان 2726

# Hijri to Gregorian
greg = KurdishCalendar.hijri_to_gregorian(1445, 9, 1)
print(greg)  # Ramadan 1st as Gregorian date

# Kurdish month names
print(KurdishCalendar.KURDISH_MONTH_NAMES)
# ['خاکەلێوە', 'گوڵان', 'جۆزەردان', ...]

print(KurdishCalendar.HIJRI_MONTH_NAMES)
# ['موحەڕەم', 'سەفەر', 'ڕەبیعی یەکەم', ...]
```

### 24. Color Names — ناوی ڕەنگەکان

```python
from kurdish_sorani_tools import KurdishColor

# Get Kurdish name by RGB
print(KurdishColor.get_name(255, 0, 0))      # سوور
print(KurdishColor.get_name(0, 0, 255))      # شین
print(KurdishColor.get_name(255, 255, 0))    # زەرد

# Get closest color name
print(KurdishColor.get_closest_name(250, 10, 10))  # سوور

# From hex
print(KurdishColor.get_name_from_hex("#FF0000"))   # سوور
print(KurdishColor.get_name_from_hex("#00FF00"))   # سەوز

# Kurdish name to RGB
print(KurdishColor.from_name("سوور"))    # (255, 0, 0)
print(KurdishColor.from_name("شین"))     # (0, 0, 255)

# All color names
print(KurdishColor.get_all_names())
# ['سوور', 'سەوز', 'شین', 'زەرد', 'پرتەقاڵی', 'مۆر', 'سپی', 'ڕەش', ...]
```

### 25. Digit to Word (Two Modes) — گۆڕینی ژمارە بە دوو شێوە

```python
from kurdish_sorani_tools import digit_to_word, StrType

# STR_WORD mode: full Kurdish words
print(digit_to_word("25000", StrType.STR_WORD))
# بیست و پێنج هەزار

# NUM_WORD mode: numbers + Kurdish scale words
print(digit_to_word("25000", StrType.NUM_WORD))
# 25 هەزار

# With money
print(digit_to_word("1500000", StrType.STR_WORD, is_money=True))
# یەک ملیۆن و پێنج سەد هەزار دیناری عراقی
```

---

## 🖥️ Demo App (Tkinter)

A full desktop demo app is included in `kurdish_tkinter_app/main.py`:

```bash
pip install kurdish-sorani-tools
python kurdish_tkinter_app/main.py
```

The demo includes 10 interactive tabs showcasing all features:
- Number to Words (with ordinal)
- Digit Converter (EN↔KU + commas + words→number)
- Keyboard Layout Converter
- Text Normalizer + Slug
- Phone Number Formatter
- Kurdish Detection + Direction + Word Count
- Currency Formatter
- Pluralization
- Relative Time + Number Range
- Calendar (Gregorian/Hijri/Kurdish) + Colors + Validators

---

## 🔗 Also Available

- **Flutter/Dart package:** [kurdish_sorani_tools](https://github.com/dana-1sherzad/flutter_kurdish_sorani_tools_project) on pub.dev

---

## 📄 License

MIT License — Dana Sherzad

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

```bash
git clone https://github.com/dana-1sherzad/kurdish_sorani_tools_python.git
cd kurdish_sorani_tools_python
pip install -e .
```
