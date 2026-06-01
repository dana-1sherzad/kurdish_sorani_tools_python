"""
Kurdish Text Direction - ئاڕاستەی دەق
Detect text direction (RTL/LTR).
"""

import re


class KurdishTextDirection:
    """Text direction detection utilities."""

    RTL_REGEX = re.compile(
        "[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]"
    )

    @staticmethod
    def detect_direction(text: str) -> str:
        """
        Detect text direction.
        دیاریکردنی ئاڕاستەی دەق

        Returns "rtl" or "ltr".

        >>> KurdishTextDirection.detect_direction("سڵاو")
        'rtl'
        >>> KurdishTextDirection.detect_direction("Hello")
        'ltr'
        """
        if not text:
            return "ltr"

        for char in text:
            if KurdishTextDirection.RTL_REGEX.match(char):
                return "rtl"
            if re.match("[a-zA-Z]", char):
                return "ltr"

        return "ltr"

    @staticmethod
    def is_rtl(text: str) -> bool:
        """
        Check if text is RTL.
        پشکنین ئایا دەقەکە RTL ە
        """
        return KurdishTextDirection.detect_direction(text) == "rtl"

    @staticmethod
    def is_ltr(text: str) -> bool:
        """
        Check if text is LTR.
        پشکنین ئایا دەقەکە LTR ە
        """
        return KurdishTextDirection.detect_direction(text) == "ltr"
