"""
Kurdish Greeting - سڵاوکردن
Time-based Kurdish greetings.
"""

from datetime import datetime


class KurdishGreeting:
    """Kurdish greeting by time of day."""

    ALL_GREETINGS = [
        "بەیانی باش",
        "ڕۆژ باش",
        "ئێوارە باش",
        "شەو باش",
    ]

    @staticmethod
    def now(time: datetime | None = None) -> str:
        """
        Get greeting based on current time.
        گەڕاندنەوەی سڵاو بەپێی کاتی ئێستا

        >>> KurdishGreeting.now(datetime(2024, 1, 1, 9, 0))
        'بەیانی باش'
        """
        hour = (time or datetime.now()).hour
        return KurdishGreeting.from_hour(hour)

    @staticmethod
    def from_hour(hour: int) -> str:
        """
        Get greeting based on hour.
        گەڕاندنەوەی سڵاو بەپێی کاتژمێر
        """
        if 5 <= hour < 12:
            return "بەیانی باش"
        elif 12 <= hour < 17:
            return "ڕۆژ باش"
        elif 17 <= hour < 21:
            return "ئێوارە باش"
        else:
            return "شەو باش"

    @staticmethod
    def with_name(name: str, time: datetime | None = None) -> str:
        """
        Greeting with a name.
        سڵاو لەگەڵ ناو

        >>> KurdishGreeting.with_name("دانا", datetime(2024, 1, 1, 9, 0))
        'بەیانی باش، دانا'
        """
        return f"{KurdishGreeting.now(time)}، {name}"


def kurdish_greeting(time: datetime | None = None) -> str:
    """Shortcut for KurdishGreeting.now."""
    return KurdishGreeting.now(time)
