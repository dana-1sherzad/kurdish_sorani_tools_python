"""
Kurdish Currency Formatter - فۆرماتکردنی دراو
Format currency amounts with Kurdish names and symbols.
"""

import re
from enum import Enum
from .digits import convert_en_to_ku


class CurrencyType(Enum):
    """Currency types supported."""
    IQD = "iqd"
    USD = "usd"
    EUR = "eur"
    GBP = "gbp"
    IRR = "irr"
    TRL = "trl"


class KurdishCurrency:
    """Kurdish currency formatting utilities."""

    CURRENCY_NAMES = {
        CurrencyType.IQD: "دیناری عراقی",
        CurrencyType.USD: "دۆلاری ئەمریکی",
        CurrencyType.EUR: "یۆرۆ",
        CurrencyType.GBP: "پاوەندی بەریتانی",
        CurrencyType.IRR: "تومانی ئێرانی",
        CurrencyType.TRL: "لیرەی تورکی",
    }

    CURRENCY_SYMBOLS = {
        CurrencyType.IQD: "د.ع",
        CurrencyType.USD: "$",
        CurrencyType.EUR: "€",
        CurrencyType.GBP: "£",
        CurrencyType.IRR: "ت",
        CurrencyType.TRL: "₺",
    }

    @staticmethod
    def format(
        amount: float | int,
        currency: CurrencyType = CurrencyType.IQD,
        use_kurdish_digits: bool = False,
        show_name: bool = False,
        decimal_places: int = 0,
    ) -> str:
        """
        Format a currency amount.
        فۆرماتکردنی بڕی پارە بە فاریزە و هێمای دراو

        >>> KurdishCurrency.format(1500000)
        '1,500,000 د.ع'
        >>> KurdishCurrency.format(1500000, show_name=True)
        '1,500,000 دیناری عراقی'
        """
        if decimal_places > 0:
            amount_str = f"{amount:.{decimal_places}f}"
        else:
            amount_str = str(int(amount))

        # Add thousand separators
        parts = amount_str.split(".")
        integer_part = re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1,", parts[0])
        decimal_part = f".{parts[1]}" if len(parts) > 1 else ""
        formatted = integer_part + decimal_part

        if use_kurdish_digits:
            formatted = convert_en_to_ku(formatted)

        if show_name:
            return f"{formatted} {KurdishCurrency.CURRENCY_NAMES[currency]}"
        return f"{formatted} {KurdishCurrency.CURRENCY_SYMBOLS[currency]}"

    @staticmethod
    def get_currency_name(currency: CurrencyType) -> str:
        """Get Kurdish name of a currency."""
        return KurdishCurrency.CURRENCY_NAMES.get(currency, "")

    @staticmethod
    def get_currency_symbol(currency: CurrencyType) -> str:
        """Get symbol of a currency."""
        return KurdishCurrency.CURRENCY_SYMBOLS.get(currency, "")
