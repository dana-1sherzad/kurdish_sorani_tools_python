"""
Kurdish Relative Time - کاتی نسبی
Display relative time in Kurdish (e.g., "٥ خولەک لەمەوپێش").
"""

from datetime import datetime


class KurdishRelativeTime:
    """Kurdish relative time utilities."""

    @staticmethod
    def from_datetime(dt: datetime, now: datetime | None = None) -> str:
        """
        Get relative time in Kurdish.
        گەڕاندنەوەی کاتی نسبی بە کوردی

        >>> from datetime import datetime, timedelta
        >>> now = datetime(2024, 1, 1, 12, 0, 0)
        >>> past = now - timedelta(minutes=5)
        >>> KurdishRelativeTime.from_datetime(past, now=now)
        '٥ خولەک لەمەوپێش'
        """
        if now is None:
            now = datetime.now()

        difference = now - dt

        if difference.total_seconds() < 0:
            return KurdishRelativeTime._future_time(abs(difference.total_seconds()))
        return KurdishRelativeTime._past_time(difference.total_seconds())

    @staticmethod
    def _past_time(seconds: float) -> str:
        if seconds < 5:
            return "ئێستا"
        if seconds < 60:
            return f"{int(seconds)} چرکە لەمەوپێش"
        minutes = int(seconds / 60)
        if minutes < 2:
            return "خولەکێک لەمەوپێش"
        if minutes < 60:
            return f"{minutes} خولەک لەمەوپێش"
        hours = int(seconds / 3600)
        if hours < 2:
            return "کاتژمێرێک لەمەوپێش"
        if hours < 24:
            return f"{hours} کاتژمێر لەمەوپێش"
        days = int(seconds / 86400)
        if days < 2:
            return "دوێنێ"
        if days < 7:
            return f"{days} ڕۆژ لەمەوپێش"
        if days < 14:
            return "هەفتەیەک لەمەوپێش"
        if days < 30:
            return f"{days // 7} هەفتە لەمەوپێش"
        if days < 60:
            return "مانگێک لەمەوپێش"
        if days < 365:
            return f"{days // 30} مانگ لەمەوپێش"
        if days < 730:
            return "ساڵێک لەمەوپێش"
        return f"{days // 365} ساڵ لەمەوپێش"

    @staticmethod
    def _future_time(seconds: float) -> str:
        if seconds < 5:
            return "ئێستا"
        if seconds < 60:
            return f"لە {int(seconds)} چرکەدا"
        minutes = int(seconds / 60)
        if minutes < 2:
            return "لە خولەکێکدا"
        if minutes < 60:
            return f"لە {minutes} خولەکدا"
        hours = int(seconds / 3600)
        if hours < 2:
            return "لە کاتژمێرێکدا"
        if hours < 24:
            return f"لە {hours} کاتژمێردا"
        days = int(seconds / 86400)
        if days < 2:
            return "سبەینێ"
        if days < 7:
            return f"لە {days} ڕۆژدا"
        if days < 14:
            return "لە هەفتەیەکدا"
        if days < 30:
            return f"لە {days // 7} هەفتەدا"
        if days < 60:
            return "لە مانگێکدا"
        if days < 365:
            return f"لە {days // 30} مانگدا"
        if days < 730:
            return "لە ساڵێکدا"
        return f"لە {days // 365} ساڵدا"


def kurdish_relative_time(dt: datetime, now: datetime | None = None) -> str:
    """Shortcut for KurdishRelativeTime.from_datetime."""
    return KurdishRelativeTime.from_datetime(dt, now=now)
