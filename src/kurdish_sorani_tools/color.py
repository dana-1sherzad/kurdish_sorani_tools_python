"""
Kurdish Color Names - ناوی ڕەنگەکان
Color names in Kurdish.
"""


class KurdishColor:
    """Kurdish color name utilities."""

    # Color value (RGB hex) to Kurdish name
    COLOR_NAMES = {
        (255, 0, 0): "سوور",
        (0, 255, 0): "سەوز",
        (0, 0, 255): "شین",
        (255, 255, 0): "زەرد",
        (255, 128, 0): "پرتەقاڵی",
        (128, 0, 128): "مۆر",
        (255, 255, 255): "سپی",
        (0, 0, 0): "ڕەش",
        (128, 128, 128): "خۆڵەمێشی",
        (165, 42, 42): "قاوەیی",
        (255, 192, 203): "پەمبەیی",
        (0, 255, 255): "ئاسمانی",
        (192, 192, 192): "زیوی",
        (255, 215, 0): "ئاڵتوونی",
        (75, 0, 130): "نیلی",
        (238, 130, 238): "بەنەوشەیی",
    }

    # Kurdish name to RGB tuple
    NAMED_COLORS = {
        "سوور": (255, 0, 0),
        "سەوز": (0, 255, 0),
        "شین": (0, 0, 255),
        "زەرد": (255, 255, 0),
        "پرتەقاڵی": (255, 128, 0),
        "مۆر": (128, 0, 128),
        "سپی": (255, 255, 255),
        "ڕەش": (0, 0, 0),
        "خۆڵەمێشی": (128, 128, 128),
        "قاوەیی": (165, 42, 42),
        "پەمبەیی": (255, 192, 203),
        "ئاسمانی": (0, 255, 255),
        "زیوی": (192, 192, 192),
        "ئاڵتوونی": (255, 215, 0),
        "نیلی": (75, 0, 130),
        "بەنەوشەیی": (238, 130, 238),
    }

    @staticmethod
    def get_name(r: int, g: int, b: int) -> str:
        """
        Get Kurdish name of a color by RGB values.
        گەڕاندنەوەی ناوی ڕەنگ بە کوردی

        >>> KurdishColor.get_name(255, 0, 0)
        'سوور'
        """
        return KurdishColor.COLOR_NAMES.get((r, g, b), "نەناسراو")

    @staticmethod
    def from_name(name: str) -> tuple | None:
        """
        Get RGB tuple from Kurdish color name.
        گەڕاندنەوەی ڕەنگ لە ناوی کوردی

        >>> KurdishColor.from_name("سوور")
        (255, 0, 0)
        """
        return KurdishColor.NAMED_COLORS.get(name)

    @staticmethod
    def get_all_names() -> list[str]:
        """Get all Kurdish color names."""
        return list(KurdishColor.NAMED_COLORS.keys())

    @staticmethod
    def get_closest_name(r: int, g: int, b: int) -> str:
        """
        Find the closest named color.
        نزیکترین ڕەنگ بدۆزەرەوە و ناوی کوردی بگەڕێنەوە

        >>> KurdishColor.get_closest_name(250, 10, 10)
        'سوور'
        """
        min_distance = float("inf")
        closest_name = "نەناسراو"

        for name, (cr, cg, cb) in KurdishColor.NAMED_COLORS.items():
            distance = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_name = name

        return closest_name

    @staticmethod
    def get_name_from_hex(hex_color: str) -> str:
        """
        Get Kurdish color name from hex string.

        >>> KurdishColor.get_name_from_hex("#FF0000")
        'سوور'
        """
        hex_color = hex_color.lstrip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return KurdishColor.get_closest_name(r, g, b)
