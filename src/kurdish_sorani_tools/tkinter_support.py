"""
Kurdish Tkinter Support - پشتگیری تکینتەر بۆ کوردی
Auto-fix Kurdish character rendering and INPUT in Tkinter applications.

Fixes the Tcl/Tk 8.6 bug on Windows where Kurdish keyboard input
is misidentified and converted to '?' characters.
"""

import sys
import tkinter as tk
from tkinter import font as tkfont


# All Kurdish Sorani characters
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

# Special keys to ignore in the input fix
_SKIP_KEYCODES = {16, 17, 18, 20, 144}  # Shift, Ctrl, Alt, CapsLock, NumLock
_SKIP_KEYSYMS = {
    "Return", "BackSpace", "Delete", "Left", "Right", "Up", "Down",
    "Home", "End", "Tab", "Escape", "space", "Control_L", "Control_R",
    "Alt_L", "Alt_R", "Shift_L", "Shift_R", "Caps_Lock",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
}


def _get_unicode_char_win32(keycode):
    """
    Use Windows ToUnicodeEx API to get the real Unicode character
    from a keycode, bypassing Tcl/Tk's broken Kurdish keyboard handling.
    """
    if sys.platform != "win32":
        return None
    try:
        import ctypes
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32

        buf = ctypes.create_unicode_buffer(5)
        keyboard_state = (ctypes.c_ubyte * 256)()
        user32.GetKeyboardState(keyboard_state)

        thread_id = kernel32.GetCurrentThreadId()
        hkl = user32.GetKeyboardLayout(thread_id)

        result = user32.ToUnicodeEx(
            keycode, keycode, keyboard_state, buf, 5, 0, hkl
        )
        if result > 0:
            return buf.value[:result]
    except Exception:
        pass
    return None


def _kurdish_key_handler(event, widget):
    """
    Handle keyboard input for a widget, fixing Kurdish character input.
    Returns "break" if the character was handled, None otherwise.
    """
    # Skip special keys
    if event.keycode in _SKIP_KEYCODES:
        return None
    if event.keysym in _SKIP_KEYSYMS:
        return None

    # If Tkinter gave us '?' but the keycode suggests a real character
    if event.char == "?" or (event.char and ord(event.char) == 63):
        char = _get_unicode_char_win32(event.keycode)
        if char and char != "?":
            widget.insert(tk.INSERT, char)
            return "break"

    # If Tkinter gave us a character with wrong encoding (Cyrillic etc.)
    if event.char and ord(event.char) > 127:
        char = _get_unicode_char_win32(event.keycode)
        if char and char != event.char and ord(char[0]) > 127:
            widget.insert(tk.INSERT, char)
            return "break"

    return None


class KurdishTkinter:
    """
    Helper class for proper Kurdish character display AND input in Tkinter.
    کڵاسی یاریدەدەر بۆ پیشاندان و ئینپووتی دروستی پیتەکانی کوردی لە تکینتەر.

    Usage:
        from kurdish_sorani_tools import KurdishTkinter

        root = KurdishTkinter.create_window("ئەپی من")
        entry = KurdishTkinter.create_entry(root)
        entry.pack()
        root.mainloop()
    """

    _cached_font = None

    @staticmethod
    def get_best_font(size: int = 12) -> tuple:
        """
        Find the best available font for Kurdish characters.
        دۆزینەوەی باشترین فۆنتی بەردەست بۆ پیتەکانی کوردی.
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
        Fix an existing Tkinter window for Kurdish display.
        Sets default fonts to Kurdish-compatible font.
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
    def fix_input(widget):
        """
        Fix Kurdish keyboard input for a specific widget (Entry or Text).
        چاککردنی ئینپووتی کیبۆردی کوردی بۆ ویجتێک.

        This fixes the Tcl/Tk bug where Kurdish characters are
        converted to '?' on Windows.

        Args:
            widget: A tk.Entry or tk.Text widget
        """
        if sys.platform != "win32":
            return  # Only needed on Windows

        def handler(event):
            return _kurdish_key_handler(event, widget)

        widget.bind("<Key>", handler)

    @staticmethod
    def create_window(title: str = "Kurdish App", size: int = 12) -> tk.Tk:
        """
        Create a new Tkinter window configured for Kurdish.
        """
        root = tk.Tk()
        root.title(title)
        KurdishTkinter.fix_window(root, size)
        return root

    @staticmethod
    def create_label(parent, text: str = "", size: int = 12, **kwargs) -> tk.Label:
        """Create a Label with proper Kurdish font."""
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        return tk.Label(parent, text=text, **kwargs)

    @staticmethod
    def create_entry(parent, size: int = 12, fix_input: bool = True, **kwargs) -> tk.Entry:
        """
        Create an Entry with proper Kurdish font AND input fix.
        دروستکردنی ئینتری بە فۆنتی کوردی و چاککردنی ئینپووت.
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        entry = tk.Entry(parent, **kwargs)
        if fix_input and sys.platform == "win32":
            KurdishTkinter.fix_input(entry)
        return entry

    @staticmethod
    def create_text(parent, size: int = 12, fix_input: bool = True, **kwargs) -> tk.Text:
        """
        Create a Text widget with proper Kurdish font AND input fix.
        """
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        text = tk.Text(parent, **kwargs)
        if fix_input and sys.platform == "win32":
            KurdishTkinter.fix_input(text)
        return text

    @staticmethod
    def create_button(parent, text: str = "", size: int = 10, **kwargs) -> tk.Button:
        """Create a Button with proper Kurdish font."""
        font_name, _ = KurdishTkinter.get_best_font(size)
        kwargs.setdefault("font", (font_name, size))
        return tk.Button(parent, text=text, **kwargs)

    @staticmethod
    def display_message(message: str, title: str = "پەیام"):
        """Display a simple message box with Kurdish text."""
        root = KurdishTkinter.create_window(title)
        root.geometry("400x200")
        label = KurdishTkinter.create_label(
            root, text=message, size=14, wraplength=350, justify="right"
        )
        label.pack(padx=20, pady=30, expand=True)
        btn = KurdishTkinter.create_button(root, text="باشە", size=11, command=root.destroy)
        btn.pack(pady=10)
        root.mainloop()
