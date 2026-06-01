"""
Kurdish Sorani Tools - Kivy Mobile App
Ø¦Ø§Ù…Ø±Ø§Ø²Û•Ú©Ø§Ù†ÛŒ Ú©ÙˆØ±Ø¯ÛŒ Ø³Û†Ø±Ø§Ù†ÛŒ - Ø¦Û•Ù¾ÛŒ Ù…Û†Ø¨Ø§ÛŒÙ„

Uses the kurdish-sorani-tools package.
Works on Android, iOS, Windows, Linux, macOS.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from kivy.metrics import sp, dp
from datetime import datetime, timedelta

from kurdish_sorani_tools import (
    convert_en_to_ku, convert_ku_to_en,
    add_commas, remove_commas,
    number_to_words, number_to_words_string,
    words_to_number, words_to_number_string,
    is_kurdish, has_kurdish,
    fix_url,
    KurdishOrdinal,
    KurdishDateTime, kurdish_date_format,
    KurdishKeyboard,
    KurdishNormalizer,
    KurdishCurrency, CurrencyType,
    KurdishTextDirection,
    KurdishPlural, plural_definite, plural_indefinite,
    KurdishStringUtils,
    KurdishRelativeTime, kurdish_relative_time,
    KurdishPhone, format_phone,
    KurdishNumberRange,
    KurdishSentence,
    KurdishNumberValidator,
    KurdishValidators,
    KurdishGreeting, kurdish_greeting,
    KurdishCountSuffix,
    KurdishCalendar,
    KurdishColor,
    digit_to_word, StrType,
)


# Colors
BG_DARK = get_color_from_hex("#1a1a2e")
BG_CARD = get_color_from_hex("#16213e")
ACCENT = get_color_from_hex("#4fc3f7")
GREEN = get_color_from_hex("#76ff03")
WHITE = get_color_from_hex("#ffffff")


class ResultLabel(Label):
    """Styled result label."""
    def __init__(self, **kwargs):
        kwargs.setdefault("color", GREEN)
        kwargs.setdefault("font_size", sp(16))
        kwargs.setdefault("halign", "right")
        kwargs.setdefault("valign", "middle")
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(60))
        kwargs.setdefault("text_size", (None, None))
        super().__init__(**kwargs)
        self.bind(size=self._update_text_size)

    def _update_text_size(self, *args):
        self.text_size = (self.width - dp(20), None)


class KurdishInput(TextInput):
    """Styled text input for Kurdish."""
    def __init__(self, **kwargs):
        kwargs.setdefault("font_size", sp(16))
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(50))
        kwargs.setdefault("multiline", False)
        kwargs.setdefault("halign", "right")
        kwargs.setdefault("background_color", get_color_from_hex("#0f3460"))
        kwargs.setdefault("foreground_color", WHITE)
        kwargs.setdefault("cursor_color", ACCENT)
        kwargs.setdefault("hint_text_color", get_color_from_hex("#666666"))
        kwargs.setdefault("padding", [dp(10), dp(12)])
        super().__init__(**kwargs)


class KurdishButton(Button):
    """Styled action button."""
    def __init__(self, **kwargs):
        kwargs.setdefault("font_size", sp(13))
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(45))
        kwargs.setdefault("background_color", get_color_from_hex("#0f3460"))
        kwargs.setdefault("color", ACCENT)
        kwargs.setdefault("bold", True)
        super().__init__(**kwargs)


def make_tab_content(title, widgets_fn):
    """Create a scrollable tab content."""
    scroll = ScrollView()
    layout = BoxLayout(orientation="vertical", padding=dp(15),
                       spacing=dp(10), size_hint_y=None)
    layout.bind(minimum_height=layout.setter("height"))

    # Header
    header = Label(text=title, font_size=sp(18), color=ACCENT,
                   bold=True, size_hint_y=None, height=dp(40),
                   halign="center")
    header.bind(size=lambda *a: setattr(header, 'text_size', (header.width, None)))
    layout.add_widget(header)

    widgets_fn(layout)

    scroll.add_widget(layout)
    return scroll


class KurdishToolsApp(App):
    title = "Ø¦Ø§Ù…Ø±Ø§Ø²Û•Ú©Ø§Ù†ÛŒ Ú©ÙˆØ±Ø¯ÛŒ Ø³Û†Ø±Ø§Ù†ÛŒ"

    def build(self):
        self.root_layout = BoxLayout(orientation="vertical")

        # Header
        header = BoxLayout(size_hint_y=None, height=dp(70),
                           padding=[dp(10), dp(10)])
        greeting = kurdish_greeting()
        date = KurdishDateTime.today("EEEEØŒ dd MMMM yyyy")
        header_label = Label(
            text=f"[b]{greeting}[/b] â€” {date}",
            markup=True, font_size=sp(15), color=ACCENT,
            halign="center"
        )
        header_label.bind(size=lambda *a: setattr(
            header_label, 'text_size', (header_label.width, None)))
        header.add_widget(header_label)
        self.root_layout.add_widget(header)

        # Tabbed Panel
        tp = TabbedPanel(do_default_tab=False, tab_width=dp(90))

        # Tab 1: Number to Words
        tab1 = TabbedPanelItem(text="Ú˜Ù…Ø§Ø±Û• Ø¨Û† ÙˆØ´Û•")
        tab1.add_widget(make_tab_content(
            "Ú¯Û†Ú•ÛŒÙ†ÛŒ Ú˜Ù…Ø§Ø±Û• Ø¨Û† Ù†ÙˆÙˆØ³ÛŒÙ†ÛŒ Ú©ÙˆØ±Ø¯ÛŒ", self._build_number_tab))
        tp.add_widget(tab1)

        # Tab 2: Digits & Commas
        tab2 = TabbedPanelItem(text="Ú¯Û†Ú•ÛŒÙ†ÛŒ Ú˜Ù…Ø§Ø±Û•")
        tab2.add_widget(make_tab_content(
            "Ú¯Û†Ú•ÛŒÙ†ÛŒ Ú˜Ù…Ø§Ø±Û• Ùˆ ÙØ§Ø±ÛŒØ²Û•", self._build_digits_tab))
        tp.add_widget(tab2)

        # Tab 3: Keyboard
        tab3 = TabbedPanelItem(text="Ú©ÛŒØ¨Û†Ø±Ø¯")
        tab3.add_widget(make_tab_content(
            "Ú¯Û†Ú•ÛŒÙ†ÛŒ Ù„Û•ÛŒØ§ÙˆØªÛŒ Ú©ÛŒØ¨Û†Ø±Ø¯", self._build_keyboard_tab))
        tp.add_widget(tab3)

        # Tab 4: Normalizer
        tab4 = TabbedPanelItem(text="Ù†Û†Ø±Ù…Ø§Ù„Ú©Ø±Ø¯Ù†")
        tab4.add_widget(make_tab_content(
            "Ù†Û†Ø±Ù…Ø§Ù„Ú©Ø±Ø¯Ù†ÛŒ Ø¯Û•Ù‚ Ùˆ Ú†Ø§Ú©Ú©Ø±Ø¯Ù†ÛŒ Ù„ÛŒÙ†Ú©", self._build_normalizer_tab))
        tp.add_widget(tab4)

        # Tab 5: Phone
        tab5 = TabbedPanelItem(text="Ù…Û†Ø¨Ø§ÛŒÙ„")
        tab5.add_widget(make_tab_content(
            "Ú˜Ù…Ø§Ø±Û•ÛŒ Ù…Û†Ø¨Ø§ÛŒÙ„ÛŒ Ø¹Ø±Ø§Ù‚ÛŒ", self._build_phone_tab))
        tp.add_widget(tab5)

        # Tab 6: Detection
        tab6 = TabbedPanelItem(text="Ø¯Û†Ø²ÛŒÙ†Û•ÙˆÛ•")
        tab6.add_widget(make_tab_content(
            "Ù¾Ø´Ú©Ù†ÛŒÙ†ÛŒ Ø¯Û•Ù‚", self._build_detection_tab))
        tp.add_widget(tab6)

        # Tab 7: Currency
        tab7 = TabbedPanelItem(text="Ø¯Ø±Ø§Ùˆ")
        tab7.add_widget(make_tab_content(
            "ÙÛ†Ø±Ù…Ø§ØªÚ©Ø±Ø¯Ù†ÛŒ Ø¯Ø±Ø§Ùˆ", self._build_currency_tab))
        tp.add_widget(tab7)

        # Tab 8: Plural
        tab8 = TabbedPanelItem(text="Ú©Û†Ú©Ø±Ø¯Ù†Û•ÙˆÛ•")
        tab8.add_widget(make_tab_content(
            "Ú©Û†Ú©Ø±Ø¯Ù†Û•ÙˆÛ•ÛŒ ÙˆØ´Û•Ú©Ø§Ù†", self._build_plural_tab))
        tp.add_widget(tab8)

        # Tab 9: Calendar
        tab9 = TabbedPanelItem(text="Ú•Û†Ú˜Ú˜Ù…ÛŽØ±")
        tab9.add_widget(make_tab_content(
            "Ú•Û†Ú˜Ú˜Ù…ÛŽØ± Ùˆ Ú©Ø§ØªÛŒ Ù†Ø³Ø¨ÛŒ", self._build_calendar_tab))
        tp.add_widget(tab9)

        self.root_layout.add_widget(tp)
        return self.root_layout

    # â”€â”€â”€ Tab Builders â”€â”€â”€

    def _build_number_tab(self, layout):
        inp = KurdishInput(hint_text="Ú˜Ù…Ø§Ø±Û• Ø¨Ù†ÙˆÙˆØ³Û•... (12345)")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(5))

        def convert_v1(_):
            try:
                num = int(inp.text.replace(",", ""))
                result.text = number_to_words(num)
            except ValueError:
                result.text = "âš ï¸ Ú˜Ù…Ø§Ø±Û•ÛŒÛ•Ú©ÛŒ Ú•Ø§Ø³Øª Ø¨Ù†ÙˆÙˆØ³Û•"

        def convert_v2(_):
            r = digit_to_word(inp.text, StrType.STR_WORD)
            result.text = r if r else "âš ï¸ Ú˜Ù…Ø§Ø±Û• Ø¨Ù†ÙˆÙˆØ³Û•"

        def to_ordinal(_):
            try:
                num = int(inp.text.replace(",", ""))
                result.text = KurdishOrdinal.from_number(num)
            except ValueError:
                result.text = "âš ï¸ Ú˜Ù…Ø§Ø±Û• Ø¨Ù†ÙˆÙˆØ³Û•"

        b1 = KurdishButton(text="Ú¯Û†Ú•ÛŒÙ† V1")
        b1.bind(on_press=convert_v1)
        b2 = KurdishButton(text="Ú¯Û†Ú•ÛŒÙ† V2")
        b2.bind(on_press=convert_v2)
        b3 = KurdishButton(text="Ú•ÛŽØ²Ø¨Û•Ù†Ø¯ÛŒ")
        b3.bind(on_press=to_ordinal)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_digits_tab(self, layout):
        inp = KurdishInput(hint_text="Ú˜Ù…Ø§Ø±Û• ÛŒØ§Ù† ÙˆØ´Û• Ø¨Ù†ÙˆÙˆØ³Û•...")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(5))

        def to_ku(_): result.text = convert_en_to_ku(inp.text)
        def to_en(_): result.text = convert_ku_to_en(inp.text)
        def to_comma(_): result.text = add_commas(inp.text.replace(",", ""))
        def to_num(_):
            r = words_to_number(inp.text)
            result.text = str(r) if r is not None else "âš ï¸"

        b1 = KurdishButton(text="Ø¨Û† Ú©ÙˆØ±Ø¯ÛŒ Ù¡Ù¢Ù£")
        b1.bind(on_press=to_ku)
        b2 = KurdishButton(text="Ø¨Û† Ø¦ÛŒÙ†Ú¯Ù„ÛŒØ²ÛŒ 123")
        b2.bind(on_press=to_en)
        b3 = KurdishButton(text="ÙØ§Ø±ÛŒØ²Û• 1,000")
        b3.bind(on_press=to_comma)
        b4 = KurdishButton(text="ÙˆØ´Û• â†’ Ú˜Ù…Ø§Ø±Û•")
        b4.bind(on_press=to_num)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)
        btns.add_widget(b4)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_keyboard_tab(self, layout):
        inp = KurdishInput(hint_text="Ø¯Û•Ù‚ÛŒ Ø¦ÛŒÙ†Ú¯Ù„ÛŒØ²ÛŒ Ø¨Ù†ÙˆÙˆØ³Û•... (slaw)")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(50), spacing=dp(5))

        def en_to_ku(_): result.text = KurdishKeyboard.en_to_ku(inp.text)
        def ku_to_en(_): result.text = KurdishKeyboard.ku_to_en(inp.text)

        b1 = KurdishButton(text="Ø¦ÛŒÙ†Ú¯Ù„ÛŒØ²ÛŒ â†’ Ú©ÙˆØ±Ø¯ÛŒ")
        b1.bind(on_press=en_to_ku)
        b2 = KurdishButton(text="Ú©ÙˆØ±Ø¯ÛŒ â†’ Ø¦ÛŒÙ†Ú¯Ù„ÛŒØ²ÛŒ")
        b2.bind(on_press=ku_to_en)
        btns.add_widget(b1)
        btns.add_widget(b2)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_normalizer_tab(self, layout):
        inp = KurdishInput(hint_text="Ø¯Û•Ù‚ ÛŒØ§Ù† Ù„ÛŒÙ†Ú© Ø¨Ù†ÙˆÙˆØ³Û•...")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(5))

        def normalize(_): result.text = KurdishNormalizer.normalize(inp.text)
        def normalize_all(_): result.text = KurdishNormalizer.normalize_all(inp.text)
        def slug(_): result.text = KurdishStringUtils.to_slug(inp.text)
        def url(_): result.text = fix_url(inp.text)

        b1 = KurdishButton(text="Ù†Û†Ø±Ù…Ø§Ù„")
        b1.bind(on_press=normalize)
        b2 = KurdishButton(text="Ù†Û†Ø±Ù…Ø§Ù„ÛŒ ØªÛ•ÙˆØ§Ùˆ")
        b2.bind(on_press=normalize_all)
        b3 = KurdishButton(text="Slug")
        b3.bind(on_press=slug)
        b4 = KurdishButton(text="Ú†Ø§Ú©Ú©Ø±Ø¯Ù†ÛŒ Ù„ÛŒÙ†Ú©")
        b4.bind(on_press=url)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)
        btns.add_widget(b4)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_phone_tab(self, layout):
        inp = KurdishInput(hint_text="07501234567")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        def check(_):
            phone = inp.text
            formatted = KurdishPhone.format(phone)
            valid = KurdishPhone.is_valid(phone)
            operator = KurdishPhone.get_operator(phone) or "Ù†Û•Ù†Ø§Ø³Ø±Ø§Ùˆ"
            intl = KurdishPhone.to_international(phone) if valid else "â€”"
            result.text = (
                f"ÙÛ†Ø±Ù…Ø§Øª: {formatted}\n"
                f"Ø¦Û†Ù¾Û•Ø±Û•ÛŒØªÛ•Ø±: {operator}\n"
                f"Ú•Ø§Ø³ØªÛ•ØŸ: {'Ø¨Û•ÚµÛŽ âœ…' if valid else 'Ù†Û•Ø®ÛŽØ± âŒ'}\n"
                f"Ù†ÛŽÙˆØ¯Û•ÙˆÚµÛ•ØªÛŒ: {intl}"
            )

        btn = KurdishButton(text="Ù¾Ø´Ú©Ù†ÛŒÙ† ðŸ“±")
        btn.bind(on_press=check)
        layout.add_widget(btn)
        layout.add_widget(result)

    def _build_detection_tab(self, layout):
        inp = KurdishInput(hint_text="Ø¯Û•Ù‚ÛŽÚ© Ø¨Ù†ÙˆÙˆØ³Û•...")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(5))

        def check_kurdish(_):
            text = inp.text
            if is_kurdish(text):
                result.text = "âœ… ØªÛ•ÙˆØ§ÙˆÛŒ Ø¯Û•Ù‚Û•Ú©Û• Ú©ÙˆØ±Ø¯ÛŒÛŒÛ•"
            elif has_kurdish(text):
                result.text = "âš ï¸ Ù‡Û•Ù†Ø¯ÛŽÚ© Ù¾ÛŒØªÛŒ Ú©ÙˆØ±Ø¯ÛŒ ØªÛŽØ¯Ø§ÛŒÛ•"
            else:
                result.text = "âŒ Ù‡ÛŒÚ† Ù¾ÛŒØªÛŒ Ú©ÙˆØ±Ø¯ÛŒ ØªÛŽØ¯Ø§ Ù†ÛŒÛŒÛ•"

        def check_dir(_):
            d = KurdishTextDirection.detect_direction(inp.text)
            result.text = f"Ø¦Ø§Ú•Ø§Ø³ØªÛ•: {'RTL â†' if d == 'rtl' else 'LTR â†’'}"

        def count(_):
            text = inp.text
            wc = KurdishStringUtils.word_count(text)
            cc = KurdishStringUtils.char_count(text)
            sc = KurdishSentence.sentence_count(text)
            result.text = f"ÙˆØ´Û•: {wc} | Ù¾ÛŒØª: {cc} | Ú•Ø³ØªÛ•: {sc}"

        def validate_num(_):
            text = inp.text
            if KurdishNumberValidator.is_kurdish_number(text):
                result.text = "âœ… Ú˜Ù…Ø§Ø±Û•ÛŒ Ú©ÙˆØ±Ø¯ÛŒÛŒÛ•"
            elif KurdishNumberValidator.is_number(text):
                result.text = "âœ… Ú˜Ù…Ø§Ø±Û•ÛŒÛ•"
            else:
                result.text = "âŒ Ú˜Ù…Ø§Ø±Û• Ù†ÛŒÛŒÛ•"

        b1 = KurdishButton(text="Ú©ÙˆØ±Ø¯ÛŒÛŒÛ•ØŸ ðŸ”")
        b1.bind(on_press=check_kurdish)
        b2 = KurdishButton(text="Ø¦Ø§Ú•Ø§Ø³ØªÛ• â†”")
        b2.bind(on_press=check_dir)
        b3 = KurdishButton(text="Ú˜Ù…Ø±Ø¯Ù† ðŸ“Š")
        b3.bind(on_press=count)
        b4 = KurdishButton(text="Ú˜Ù…Ø§Ø±Û•ØŸ ðŸ”¢")
        b4.bind(on_press=validate_num)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)
        btns.add_widget(b4)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_currency_tab(self, layout):
        inp = KurdishInput(hint_text="Ø¨Ú• Ø¨Ù†ÙˆÙˆØ³Û•... (1500000)")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(5))

        def iqd(_):
            try:
                amount = float(inp.text.replace(",", ""))
                result.text = KurdishCurrency.format(amount, show_name=True)
            except ValueError:
                result.text = "âš ï¸ Ú˜Ù…Ø§Ø±Û• Ø¨Ù†ÙˆÙˆØ³Û•"

        def usd(_):
            try:
                amount = float(inp.text.replace(",", ""))
                result.text = KurdishCurrency.format(
                    amount, currency=CurrencyType.USD,
                    show_name=True, decimal_places=2)
            except ValueError:
                result.text = "âš ï¸ Ú˜Ù…Ø§Ø±Û• Ø¨Ù†ÙˆÙˆØ³Û•"

        def ku_digits(_):
            try:
                amount = float(inp.text.replace(",", ""))
                result.text = KurdishCurrency.format(
                    amount, use_kurdish_digits=True, show_name=True)
            except ValueError:
                result.text = "âš ï¸ Ú˜Ù…Ø§Ø±Û• Ø¨Ù†ÙˆÙˆØ³Û•"

        b1 = KurdishButton(text="Ø¯ÛŒÙ†Ø§Ø±")
        b1.bind(on_press=iqd)
        b2 = KurdishButton(text="Ø¯Û†Ù„Ø§Ø±")
        b2.bind(on_press=usd)
        b3 = KurdishButton(text="Ú©ÙˆØ±Ø¯ÛŒ")
        b3.bind(on_press=ku_digits)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_plural_tab(self, layout):
        inp = KurdishInput(hint_text="ÙˆØ´Û• Ø¨Ù†ÙˆÙˆØ³Û•... (Ú©ØªÛŽØ¨)")
        result = ResultLabel(text="")
        layout.add_widget(inp)

        btns = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(5))

        def definite(_):
            w = inp.text
            result.text = (
                f"ØªØ§Ú©: {w}\n"
                f"Ú©Û† (Ø¯ÛŒØ§Ø±ÛŒ): {plural_definite(w)}\n"
                f"Ú©Û† (Ù†Ø§Ø¯ÛŒØ§Ø±ÛŒ): {plural_indefinite(w)}"
            )

        def singular(_):
            w = inp.text
            result.text = (
                f"Ú©Û†: {w}\n"
                f"ØªØ§Ú©: {KurdishPlural.singular(w)}\n"
                f"Ú©Û†ÛŒÛ•ØŸ: {'Ø¨Û•ÚµÛŽ' if KurdishPlural.is_plural(w) else 'Ù†Û•Ø®ÛŽØ±'}"
            )

        def count_word(_):
            try:
                parts = inp.text.split()
                num = int(parts[0])
                word = parts[1] if len(parts) > 1 else "Ø´Øª"
                result.text = KurdishCountSuffix.count(
                    num, word, use_kurdish_digits=True)
            except (ValueError, IndexError):
                result.text = "âš ï¸ Ú˜Ù…Ø§Ø±Û• Ùˆ ÙˆØ´Û• Ø¨Ù†ÙˆÙˆØ³Û• (5 Ú©ØªÛŽØ¨)"

        b1 = KurdishButton(text="Ú©Û†Ú©Ø±Ø¯Ù†Û•ÙˆÛ•")
        b1.bind(on_press=definite)
        b2 = KurdishButton(text="ØªØ§Ú©Ú©Ø±Ø¯Ù†Û•ÙˆÛ•")
        b2.bind(on_press=singular)
        b3 = KurdishButton(text="Ú˜Ù…Ø§Ø±Û•+ÙˆØ´Û•")
        b3.bind(on_press=count_word)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)

        layout.add_widget(btns)
        layout.add_widget(result)

    def _build_calendar_tab(self, layout):
        result = ResultLabel(text="")

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(150), spacing=dp(5))

        def show_today(_):
            now = datetime.now()
            gregorian = KurdishDateTime.format(now, "EEEEØŒ dd MMMM yyyy")
            hijri = KurdishCalendar.format_hijri(now)
            kurdish_cal = KurdishCalendar.format_kurdish(now)
            result.text = (
                f"ðŸ“… Ú¯Ø±ÛŒÚ¯Û†Ø±ÛŒ: {gregorian}\n"
                f"ðŸ•Œ Ù‡ÛŒØ¬Ø±ÛŒ: {hijri}\n"
                f"â˜€ï¸ Ú©ÙˆØ±Ø¯ÛŒ: {kurdish_cal}"
            )

        def show_relative(_):
            now = datetime.now()
            result.text = (
                f"Ù¥ Ø®ÙˆÙ„Û•Ú© Ù„Û•Ù…Û•ÙˆÙ¾ÛŽØ´: {kurdish_relative_time(now - timedelta(minutes=5))}\n"
                f"Ù£ Ú©Ø§ØªÚ˜Ù…ÛŽØ± Ù„Û•Ù…Û•ÙˆÙ¾ÛŽØ´: {kurdish_relative_time(now - timedelta(hours=3))}\n"
                f"Ø¯ÙˆÛŽÙ†ÛŽ: {kurdish_relative_time(now - timedelta(days=1))}\n"
                f"Ø³Ø¨Û•ÛŒÙ†ÛŽ: {kurdish_relative_time(now + timedelta(days=1))}"
            )

        def show_color(_):
            import random
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            name = KurdishColor.get_closest_name(r, g, b)
            result.text = f"ðŸŽ¨ RGB({r},{g},{b}) = {name}"

        def show_range(_):
            result.text = (
                f"1-5: {KurdishNumberRange.to_words(1, 5)}\n"
                f"10-100: {KurdishNumberRange.to_words(10, 100)}\n"
                f"1-1000: {KurdishNumberRange.to_words(1, 1000)}"
            )

        def show_greeting(_):
            result.text = (
                f"Ø¨Û•ÛŒØ§Ù†ÛŒ: {KurdishGreeting.from_hour(8)}\n"
                f"Ù†ÛŒÙˆÛ•Ú•Û†: {KurdishGreeting.from_hour(14)}\n"
                f"Ø¦ÛŽÙˆØ§Ø±Û•: {KurdishGreeting.from_hour(19)}\n"
                f"Ø´Û•Ùˆ: {KurdishGreeting.from_hour(23)}\n"
                f"Ø¦ÛŽØ³ØªØ§: {KurdishGreeting.with_name('Ø¯Ø§Ù†Ø§')}"
            )

        def show_validators(_):
            result.text = (
                f"Ø¦ÛŒÙ…Û•ÛŒÙ„ test@x.com: {KurdishValidators.email('test@x.com') or 'âœ…'}\n"
                f"Ø¦ÛŒÙ…Û•ÛŒÙ„ bad: {KurdishValidators.email('bad')}\n"
                f"Ù…Û†Ø¨Ø§ÛŒÙ„ 07501234567: {KurdishValidators.phone('07501234567') or 'âœ…'}\n"
                f"Ù…Û†Ø¨Ø§ÛŒÙ„ 123: {KurdishValidators.phone('123')}"
            )

        b1 = KurdishButton(text="Ø¨Û•Ø±ÙˆØ§Ø±ÛŒ Ø¦Û•Ù…Ú•Û† ðŸ“…")
        b1.bind(on_press=show_today)
        b2 = KurdishButton(text="Ú©Ø§ØªÛŒ Ù†Ø³Ø¨ÛŒ â°")
        b2.bind(on_press=show_relative)
        b3 = KurdishButton(text="Ú•Û•Ù†Ú¯ ðŸŽ¨")
        b3.bind(on_press=show_color)
        b4 = KurdishButton(text="Ú•ÛŒØ²ÛŒ Ú˜Ù…Ø§Ø±Û•")
        b4.bind(on_press=show_range)
        b5 = KurdishButton(text="Ø³ÚµØ§ÙˆÚ©Ø±Ø¯Ù† ðŸ‘‹")
        b5.bind(on_press=show_greeting)
        b6 = KurdishButton(text="Ù¾Ø´Ú©Ù†ÛŒÙ†ÛŒ ÙÛ†Ø±Ù… âœ“")
        b6.bind(on_press=show_validators)
        btns.add_widget(b1)
        btns.add_widget(b2)
        btns.add_widget(b3)
        btns.add_widget(b4)
        btns.add_widget(b5)
        btns.add_widget(b6)

        layout.add_widget(btns)
        layout.add_widget(result)


if __name__ == "__main__":
    KurdishToolsApp().run()

