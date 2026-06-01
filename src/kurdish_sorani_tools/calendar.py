"""
Kurdish Calendar - ڕۆژژمێری کوردی
Hijri and Kurdish (Rojhalati) calendar conversion.
"""

from datetime import datetime
from dataclasses import dataclass


@dataclass
class HijriDate:
    """Hijri (Islamic) date."""
    year: int
    month: int
    day: int

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


@dataclass
class KurdishDate:
    """Kurdish (Rojhalati) date."""
    year: int
    month: int
    day: int

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


class KurdishCalendar:
    """Kurdish calendar conversion utilities."""

    HIJRI_MONTH_NAMES = [
        "موحەڕەم", "سەفەر", "ڕەبیعی یەکەم",
        "ڕەبیعی دووەم", "جومادی یەکەم", "جومادی دووەم",
        "ڕەجەب", "شەعبان", "ڕەمەزان",
        "شەوال", "زولقەعدە", "زولحیججە",
    ]

    KURDISH_MONTH_NAMES = [
        "خاکەلێوە", "گوڵان", "جۆزەردان",
        "پووشپەڕ", "گەلاوێژ", "خەرمانان",
        "ڕەزبەر", "گەڵاڕێزان", "سەرماوەز",
        "بەفرانبار", "ڕێبەندان", "ڕەشەمە",
    ]

    @staticmethod
    def gregorian_to_hijri(date: datetime) -> HijriDate:
        """
        Convert Gregorian date to Hijri.
        گۆڕینی بەرواری گریگۆری بۆ هیجری
        """
        jd = KurdishCalendar._gregorian_to_julian(date.year, date.month, date.day)
        return KurdishCalendar._julian_to_hijri(jd)

    @staticmethod
    def hijri_to_gregorian(year: int, month: int, day: int) -> datetime:
        """
        Convert Hijri date to Gregorian.
        گۆڕینی بەرواری هیجری بۆ گریگۆری
        """
        jd = KurdishCalendar._hijri_to_julian(year, month, day)
        return KurdishCalendar._julian_to_gregorian(jd)

    @staticmethod
    def gregorian_to_kurdish(date: datetime) -> KurdishDate:
        """
        Convert Gregorian date to Kurdish (Rojhalati).
        گۆڕینی گریگۆری بۆ کوردی (ڕۆژهەڵاتی)
        """
        persian = KurdishCalendar._gregorian_to_persian(date.year, date.month, date.day)
        return KurdishDate(
            year=persian[0] + 1321,
            month=persian[1],
            day=persian[2],
        )

    @staticmethod
    def format_hijri(date: datetime, pattern: str = "dd MMMM yyyy") -> str:
        """Format Hijri date in Kurdish."""
        hijri = KurdishCalendar.gregorian_to_hijri(date)
        result = pattern
        result = result.replace("MMMM", KurdishCalendar.HIJRI_MONTH_NAMES[hijri.month - 1])
        result = result.replace("MM", str(hijri.month).zfill(2))
        result = result.replace("dd", str(hijri.day).zfill(2))
        result = result.replace("yyyy", str(hijri.year))
        return result

    @staticmethod
    def format_kurdish(date: datetime, pattern: str = "dd MMMM yyyy") -> str:
        """Format Kurdish (Rojhalati) date."""
        kd = KurdishCalendar.gregorian_to_kurdish(date)
        result = pattern
        result = result.replace("MMMM", KurdishCalendar.KURDISH_MONTH_NAMES[kd.month - 1])
        result = result.replace("MM", str(kd.month).zfill(2))
        result = result.replace("dd", str(kd.day).zfill(2))
        result = result.replace("yyyy", str(kd.year))
        return result

    # Internal conversion algorithms

    @staticmethod
    def _gregorian_to_julian(year: int, month: int, day: int) -> int:
        if month <= 2:
            year -= 1
            month += 12
        a = year // 100
        b = 2 - a + a // 4
        return int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524

    @staticmethod
    def _julian_to_hijri(jd: int) -> HijriDate:
        l = jd - 1948440 + 10632
        n = (l - 1) // 10631
        l2 = l - 10631 * n + 354
        j = ((10985 - l2) // 5316) * ((50 * l2) // 17719) + (l2 // 5670) * ((43 * l2) // 15238)
        l3 = l2 - ((30 - j) // 15) * ((17719 * j) // 50) - (j // 16) * ((15238 * j) // 43) + 29
        month = (24 * l3) // 709
        day = l3 - (709 * month) // 24
        year = 30 * n + j - 30
        return HijriDate(year=year, month=month, day=day)

    @staticmethod
    def _hijri_to_julian(year: int, month: int, day: int) -> int:
        return ((11 * year + 3) // 30 + 354 * year + 30 * month
                - (month - 1) // 2 + day + 1948440 - 385)

    @staticmethod
    def _julian_to_gregorian(jd: int) -> datetime:
        l = jd + 68569
        n = (4 * l) // 146097
        l2 = l - (146097 * n + 3) // 4
        i = (4000 * (l2 + 1)) // 1461001
        l3 = l2 - (1461 * i) // 4 + 31
        j = (80 * l3) // 2447
        day = l3 - (2447 * j) // 80
        l4 = j // 11
        month = j + 2 - 12 * l4
        year = 100 * (n - 49) + i + l4
        return datetime(year, month, day)

    @staticmethod
    def _gregorian_to_persian(gy: int, gm: int, gd: int) -> list:
        g_days_in_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        gy2 = gy + 1 if gm > 2 else gy
        days = (355666 + (365 * gy) + ((gy2 + 3) // 4)
                - ((gy2 + 99) // 100) + ((gy2 + 399) // 400)
                + gd + g_days_in_month[gm - 1])
        jy = -1595 + (33 * (days // 12053))
        days %= 12053
        jy += 4 * (days // 1461)
        days %= 1461
        if days > 365:
            jy += (days - 1) // 365
            days = (days - 1) % 365
        if days < 186:
            jm = 1 + (days // 31)
            jd = 1 + (days % 31)
        else:
            jm = 7 + ((days - 186) // 30)
            jd = 1 + ((days - 186) % 30)
        return [jy, jm, jd]
