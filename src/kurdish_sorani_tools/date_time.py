"""
Kurdish Date/Time - بەروار و کاتی کوردی
Format dates and times in Kurdish Sorani.
"""

from datetime import datetime


class KurdishDateTime:
    """Kurdish date and time formatting utilities."""

    DAY_NAMES = [
        "دووشەممە",
        "سێشەممە",
        "چوارشەممە",
        "پێنجشەممە",
        "هەینی",
        "شەممە",
        "یەکشەممە",
    ]

    DAY_NAMES_SHORT = [
        "دوو",
        "سێ",
        "چوار",
        "پێنج",
        "هەینی",
        "شەم",
        "یەک",
    ]

    MONTH_NAMES = [
        "کانوونی دووەم",
        "شوبات",
        "ئازار",
        "نیسان",
        "ئایار",
        "حوزەیران",
        "تەممووز",
        "ئاب",
        "ئەیلوول",
        "تشرینی یەکەم",
        "تشرینی دووەم",
        "کانوونی یەکەم",
    ]

    MONTH_NAMES_SHORT = [
        "کانوونی٢",
        "شوبات",
        "ئازار",
        "نیسان",
        "ئایار",
        "حوزەیران",
        "تەممووز",
        "ئاب",
        "ئەیلوول",
        "تشرینی١",
        "تشرینی٢",
        "کانوونی١",
    ]

    @staticmethod
    def get_day_name(weekday: int) -> str:
        """
        Get Kurdish day name. weekday: 1=Monday, 7=Sunday (ISO format).
        گەڕاندنەوەی ناوی ڕۆژ بە کوردی

        >>> KurdishDateTime.get_day_name(1)
        'دووشەممە'
        """
        return KurdishDateTime.DAY_NAMES[weekday - 1]

    @staticmethod
    def get_day_name_short(weekday: int) -> str:
        """Get short Kurdish day name."""
        return KurdishDateTime.DAY_NAMES_SHORT[weekday - 1]

    @staticmethod
    def get_month_name(month: int) -> str:
        """
        Get Kurdish month name.
        گەڕاندنەوەی ناوی مانگ بە کوردی

        >>> KurdishDateTime.get_month_name(1)
        'کانوونی دووەم'
        """
        return KurdishDateTime.MONTH_NAMES[month - 1]

    @staticmethod
    def get_month_name_short(month: int) -> str:
        """Get short Kurdish month name."""
        return KurdishDateTime.MONTH_NAMES_SHORT[month - 1]

    @staticmethod
    def format(date: datetime, pattern: str = "dd MMMM yyyy") -> str:
        """
        Format a datetime in Kurdish.
        فۆرماتکردنی بەروار بە کوردی

        Patterns: yyyy, yy, MMMM, MMM, MM, dd, EEEE, EEE, HH, mm, ss

        >>> from datetime import datetime
        >>> KurdishDateTime.format(datetime(2024, 3, 15), "dd MMMM yyyy")
        '15 ئازار 2024'
        """
        result = pattern
        # weekday: Python uses 0=Monday, 6=Sunday; we need 1=Monday, 7=Sunday
        weekday = date.isoweekday()

        result = result.replace("EEEE", KurdishDateTime.get_day_name(weekday))
        result = result.replace("EEE", KurdishDateTime.get_day_name_short(weekday))
        result = result.replace("MMMM", KurdishDateTime.get_month_name(date.month))
        result = result.replace("MMM", KurdishDateTime.get_month_name_short(date.month))
        result = result.replace("MM", str(date.month).zfill(2))
        result = result.replace("dd", str(date.day).zfill(2))
        result = result.replace("yyyy", str(date.year))
        result = result.replace("yy", str(date.year)[2:])
        result = result.replace("HH", str(date.hour).zfill(2))
        result = result.replace("mm", str(date.minute).zfill(2))
        result = result.replace("ss", str(date.second).zfill(2))

        return result

    @staticmethod
    def today(pattern: str = "EEEE, dd MMMM yyyy") -> str:
        """
        Get today's date in Kurdish.
        گەڕاندنەوەی بەرواری ئەمڕۆ بە کوردی
        """
        return KurdishDateTime.format(datetime.now(), pattern=pattern)


def kurdish_date_format(date: datetime, pattern: str = "dd MMMM yyyy") -> str:
    """Shortcut function for formatting dates in Kurdish."""
    return KurdishDateTime.format(date, pattern=pattern)
