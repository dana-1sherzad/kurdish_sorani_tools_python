"""
Kurdish Tkinter Support - پشتگیری تکینتەر بۆ کوردی
Auto-fix Kurdish character rendering in Tkinter applications.

Inspired by kurdish_characters package by Nashwan Taha Nheli.
"""

import tkinter as tk
from tkinter import font as tkfont


# All Kurdish characters (isolated, initial, medial, final forms)
KURDISH_CHARS = [
    "ئ", "ا", "ب", "پ", "ت", "ج", "چ", "ح", "خ", "د",
    "ر", "ڕ", "ز", "ژ", "س", "ش", "ع", "غ", "ف", "ڤ",
    "ق", "ک", "گ", "ل", "ڵ", "م", "ن", "و", "ۆ", "ه",
    "ھ", "ە", "ی", "ێ",
]

# Preferred fonts for Kurdish text (ordered by quality)
KURDISH_FONTS = [
    "Tahoma",
    "Arial Unicode MS",
    "Noto Sans Arabic",
    "Noto Naskh Arabic",
    "Noto Kufi Arabic",
    "Segoe UI",
    "Microsoft Sans Serif",
    "DejaVu Sans",
    "Times New Roman",
    "Arial",
]


class KurdishTkinter:
    """
    Helper class for proper Kurdish character display in Tkinter.
    کڵاسی یاریدەدەر بۆ پیشاندانی دروستی پیتەکانی کوردی لە تکینتەر.

    Usage:
        from kurdish_sorani_tools import KurdishTkinter

        root = KurdishTkinter.create_window("ئەپی من")
        # or fix an existing window:
        KurdishTkinter.fix_window(root)
    """

    _cached_font = None

    @staticmethod
    def get_best_font(size: int = 12) -> tuple:
        """
        Find the best available font for Kurdish characters.
        دۆزینەوەی باشترین فۆنتی بەردەست بۆ پیتەکانی کوردی.

        Returns:
            tuple: (font_name, size) suitable for tkinter widgets
        """
        if KurdishTkinter._cached_font:
            return (KurdishTkinter._cached_font, size)

        try:
            available = list(tkfont.families())
            for font_name in KURDISH_FONTS:
                if font_name in available:
                    KurdishTkinter._cached_font = font_name
                    return (font_name, size)
        except Exception:
            pass

        KurdishTkinter._cached_font = "Tahoma"
        return ("Tahoma", size)

    @staticmethod
    def fix_window(root: tk.Tk, size: int = 12):
        """
        Fix an existing Tkinter window to properly display Kurdish characters.
        چاککردنی پەنجەرەیەکی تکینتەر بۆ پیشاندانی دروستی پیتەکانی کوردی.

        This sets the default font for the entire window to a Kurdish-compatible font.

        Args:
            root: The Tkinter root window or Toplevel
            size: Font size (default 12)
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        try:
            default_font = tkfont.nametofont("TkDefaultFont")
            default_font.configure(family=font_name, size=size)

            text_font = tkfont.nametofont("TkTextFont")
            text_font.configure(family=font_name, size=size)

            fixed_font = tkfont.nametofont("TkFixedFont")
            fixed_font.configure(family=font_name, size=size)
        except Exception:
            pass

    @staticmethod
    def create_window(title: str = "Kurdish App", size: int = 12) -> tk.Tk:
        """
        Create a new Tkinter window configured for Kurdish text.
        دروستکردنی پەنجەرەیەکی نوێی تکینتەر کە بۆ نامەی کوردی ئامادەیە.

        Args:
            title: Window title
            size: Default font size

        Returns:
            tk.Tk: A properly configured Tkinter root window
        """
        root = tk.Tk()
        root.title(title)
        KurdishTkinter.fix_window(root, size)
        return root

    @staticmethod
    def create_label(parent, text: str = "", size: int = 12, **kwargs) -> tk.Label:
        """
        Create a Label widget with proper Kurdish font.
        دروستکردنی لەیبڵ بە فۆنتی کوردی.
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        return tk.Label(parent, text=text, **kwargs)

    @staticmethod
    def create_entry(parent, size: int = 12, **kwargs) -> tk.Entry:
        """
        Create an Entry widget with proper Kurdish font.
        دروستکردنی ئینتری بە فۆنتی کوردی.
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        return tk.Entry(parent, **kwargs)

    @staticmethod
    def create_text(parent, size: int = 12, **kwargs) -> tk.Text:
        """
        Create a Text widget with proper Kurdish font.
        دروستکردنی ویجتی تێکست بە فۆنتی کوردی.
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        return tk.Text(parent, **kwargs)

    @staticmethod
    def create_button(parent, text: str = "", size: int = 10, **kwargs) -> tk.Button:
        """
        Create a Button widget with proper Kurdish font.
        دروستکردنی دوگمە بە فۆنتی کوردی.
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        return tk.Button(parent, text=text, **kwargs)

    @staticmethod
    def display_message(message: str, title: str = "پەیام"):
        """
        Display a simple message box with Kurdish text.
        پیشاندانی سندوقێکی پەیام بە نامەی کوردی.
        """
        root = KurdishTkinter.create_window(title)
        root.geometry("400x200")

        label = KurdishTkinter.create_label(
            root, text=message, size=14,
            wraplength=350, justify="right"
        )
        label.pack(padx=20, pady=30, expand=True)

        btn = KurdishTkinter.create_button(
            root, text="باشە", size=11,
            command=root.destroy
        )
        btn.pack(pady=10)

        root.mainloop()
