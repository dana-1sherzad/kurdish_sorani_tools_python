"""
Kurdish Sorani Tools - Kivy Mobile App
Uses the kurdish-sorani-tools package.
Works on Android, iOS, Windows, Linux, macOS.
"""

import os
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

# Register Kurdish-compatible font
FONT_PATH = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "tahoma.ttf")
if os.path.exists(FONT_PATH):
    LabelBase.register(name="Kurdish", fn_regular=FONT_PATH)
    DEFAULT_FONT = "Kurdish"
else:
    DEFAULT_FONT = "Roboto"

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
    def __init__(self, **kwargs):
        kwargs.setdefault("color", GREEN)
        kwargs.setdefault("font_size", sp(16))
        kwargs.setdefault("font_name", DEFAULT_FONT)
        kwargs.setdefault("halign", "right")
        kwargs.setdefault("valign", "middle")
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(80))
        super().__init__(**kwargs)
        self.bind(size=self._update)

    def _update(self, *a):
        self.text_size = (self.width - dp(20), None)


class KurdishInput(TextInput):
    def __init__(self, **kwargs):
        kwargs.setdefault("font_size", sp(16))
        kwargs.setdefault("font_name", DEFAULT_FONT)
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(50))
        kwargs.setdefault("multiline", False)
        kwargs.setdefault("halign", "right")
        kwargs.setdefault("background_color", get_color_from_hex("#0f3460"))
        kwargs.setdefault("foreground_color", WHITE)
        kwargs.setdefault("cursor_color", ACCENT)
        kwargs.setdefault("hint_text_color", get_color_from_hex("#888888"))
        kwargs.setdefault("padding", [dp(10), dp(12)])
        super().__init__(**kwargs)


class KurdishButton(Button):
    def __init__(self, **kwargs):
        kwargs.setdefault("font_size", sp(13))
        kwargs.setdefault("font_name", DEFAULT_FONT)
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(45))
        kwargs.setdefault("background_color", get_color_from_hex("#0f3460"))
        kwargs.setdefault("color", ACCENT)
        kwargs.setdefault("bold", True)
        super().__init__(**kwargs)


def make_tab_content(title, widgets_fn):
    scroll = ScrollView()
    layout = BoxLayout(orientation="vertical", padding=dp(15),
                       spacing=dp(10), size_hint_y=None)
    layout.bind(minimum_height=layout.setter("height"))

    header = Label(text=title, font_size=sp(18), font_name=DEFAULT_FONT,
                   color=ACCENT, bold=True, size_hint_y=None, height=dp(40))
    header.bind(size=lambda *a: setattr(header, 'text_size', (header.width, None)))
    layout.add_widget(header)

    widgets_fn(layout)
    scroll.add_widget(layout)
    return scroll


class KurdishToolsApp(App):

    def build(self):
        self.title = "Kurdish Sorani Tools"
        root = BoxLayout(orientation="vertical")

        # Header
        greeting = kurdish_greeting()
        date = KurdishDateTime.today("EEEE, dd MMMM yyyy")
        header = Label(
            text=f"{greeting} - {date}",
            font_name=DEFAULT_FONT, font_size=sp(15),
            color=ACCENT, bold=True,
            size_hint_y=None, height=dp(60)
        )
        root.add_widget(header)

        # Tabs
        tp = TabbedPanel(do_default_tab=False, tab_width=dp(100))

        t1 = TabbedPanelItem(text="Number")
        t1.add_widget(make_tab_content(
            "Number to Kurdish Words", self._tab_number))
        tp.add_widget(t1)

        t2 = TabbedPanelItem(text="Digits")
        t2.add_widget(make_tab_content(
            "Digit Conversion", self._tab_digits))
        tp.add_widget(t2)

        t3 = TabbedPanelItem(text="Keyboard")
        t3.add_widget(make_tab_content(
            "Keyboard Converter", self._tab_keyboard))
        tp.add_widget(t3)

        t4 = TabbedPanelItem(text="Normalize")
        t4.add_widget(make_tab_content(
            "Text Normalizer", self._tab_normalizer))
        tp.add_widget(t4)

        t5 = TabbedPanelItem(text="Phone")
        t5.add_widget(make_tab_content(
            "Iraqi Phone Number", self._tab_phone))
        tp.add_widget(t5)

        t6 = TabbedPanelItem(text="Detect")
        t6.add_widget(make_tab_content(
            "Text Detection", self._tab_detect))
        tp.add_widget(t6)

        t7 = TabbedPanelItem(text="Currency")
        t7.add_widget(make_tab_content(
            "Currency Formatter", self._tab_currency))
        tp.add_widget(t7)

        t8 = TabbedPanelItem(text="Plural")
        t8.add_widget(make_tab_content(
            "Pluralization", self._tab_plural))
        tp.add_widget(t8)

        t9 = TabbedPanelItem(text="Calendar")
        t9.add_widget(make_tab_content(
            "Calendar & More", self._tab_calendar))
        tp.add_widget(t9)

        root.add_widget(tp)
        return root

    def _tab_number(self, layout):
        inp = KurdishInput(hint_text="Enter number... (12345)")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(5))

        def v1(_):
            try:
                result.text = number_to_words(int(inp.text.replace(",", "")))
            except: result.text = "Enter a valid number"

        def v2(_):
            r = digit_to_word(inp.text, StrType.STR_WORD)
            result.text = r if r else "Enter a number"

        def ordinal(_):
            try:
                result.text = KurdishOrdinal.from_number(int(inp.text.replace(",", "")))
            except: result.text = "Enter a number"

        b1 = KurdishButton(text="To Words V1"); b1.bind(on_press=v1)
        b2 = KurdishButton(text="To Words V2"); b2.bind(on_press=v2)
        b3 = KurdishButton(text="Ordinal"); b3.bind(on_press=ordinal)
        btns.add_widget(b1); btns.add_widget(b2); btns.add_widget(b3)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_digits(self, layout):
        inp = KurdishInput(hint_text="Enter number or text...")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(5))

        def to_ku(_): result.text = convert_en_to_ku(inp.text)
        def to_en(_): result.text = convert_ku_to_en(inp.text)
        def comma(_): result.text = add_commas(inp.text.replace(",", ""))
        def w2n(_):
            r = words_to_number(inp.text)
            result.text = str(r) if r is not None else "Could not convert"

        b1 = KurdishButton(text="To Kurdish 123"); b1.bind(on_press=to_ku)
        b2 = KurdishButton(text="To English 123"); b2.bind(on_press=to_en)
        b3 = KurdishButton(text="Add Commas"); b3.bind(on_press=comma)
        b4 = KurdishButton(text="Words to Num"); b4.bind(on_press=w2n)
        btns.add_widget(b1); btns.add_widget(b2)
        btns.add_widget(b3); btns.add_widget(b4)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_keyboard(self, layout):
        inp = KurdishInput(hint_text="Type English... (slaw)")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(50), spacing=dp(5))
        def en2ku(_): result.text = KurdishKeyboard.en_to_ku(inp.text)
        def ku2en(_): result.text = KurdishKeyboard.ku_to_en(inp.text)
        b1 = KurdishButton(text="EN -> Kurdish"); b1.bind(on_press=en2ku)
        b2 = KurdishButton(text="Kurdish -> EN"); b2.bind(on_press=ku2en)
        btns.add_widget(b1); btns.add_widget(b2)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_normalizer(self, layout):
        inp = KurdishInput(hint_text="Enter text or URL...")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(5))
        def norm(_): result.text = KurdishNormalizer.normalize(inp.text)
        def norm_all(_): result.text = KurdishNormalizer.normalize_all(inp.text)
        def slug(_): result.text = KurdishStringUtils.to_slug(inp.text)
        def url(_): result.text = fix_url(inp.text)
        b1 = KurdishButton(text="Normalize"); b1.bind(on_press=norm)
        b2 = KurdishButton(text="Normalize All"); b2.bind(on_press=norm_all)
        b3 = KurdishButton(text="URL Slug"); b3.bind(on_press=slug)
        b4 = KurdishButton(text="Fix URL"); b4.bind(on_press=url)
        btns.add_widget(b1); btns.add_widget(b2)
        btns.add_widget(b3); btns.add_widget(b4)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_phone(self, layout):
        inp = KurdishInput(hint_text="07501234567")
        result = ResultLabel()
        layout.add_widget(inp)

        def check(_):
            p = inp.text
            valid = KurdishPhone.is_valid(p)
            op = KurdishPhone.get_operator(p) or "Unknown"
            intl = KurdishPhone.to_international(p) if valid else "-"
            result.text = (
                f"Format: {KurdishPhone.format(p)}\n"
                f"Operator: {op}\n"
                f"Valid: {'Yes' if valid else 'No'}\n"
                f"International: {intl}"
            )

        btn = KurdishButton(text="Check Phone"); btn.bind(on_press=check)
        layout.add_widget(btn)
        layout.add_widget(result)

    def _tab_detect(self, layout):
        inp = KurdishInput(hint_text="Enter text...")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=2, size_hint_y=None, height=dp(100), spacing=dp(5))

        def kurdish(_):
            t = inp.text
            if is_kurdish(t): result.text = "All Kurdish"
            elif has_kurdish(t): result.text = "Contains Kurdish"
            else: result.text = "No Kurdish"

        def direction(_):
            d = KurdishTextDirection.detect_direction(inp.text)
            result.text = f"Direction: {d.upper()}"

        def count(_):
            t = inp.text
            result.text = (
                f"Words: {KurdishStringUtils.word_count(t)}\n"
                f"Chars: {KurdishStringUtils.char_count(t)}\n"
                f"Sentences: {KurdishSentence.sentence_count(t)}"
            )

        def numval(_):
            t = inp.text
            if KurdishNumberValidator.is_kurdish_number(t):
                result.text = "Kurdish number"
            elif KurdishNumberValidator.is_number(t):
                result.text = "Valid number"
            else:
                result.text = "Not a number"

        b1 = KurdishButton(text="Is Kurdish?"); b1.bind(on_press=kurdish)
        b2 = KurdishButton(text="Direction"); b2.bind(on_press=direction)
        b3 = KurdishButton(text="Count"); b3.bind(on_press=count)
        b4 = KurdishButton(text="Number?"); b4.bind(on_press=numval)
        btns.add_widget(b1); btns.add_widget(b2)
        btns.add_widget(b3); btns.add_widget(b4)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_currency(self, layout):
        inp = KurdishInput(hint_text="Amount... (1500000)")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(5))

        def iqd(_):
            try:
                a = float(inp.text.replace(",", ""))
                result.text = KurdishCurrency.format(a, show_name=True)
            except: result.text = "Enter a number"

        def usd(_):
            try:
                a = float(inp.text.replace(",", ""))
                result.text = KurdishCurrency.format(
                    a, currency=CurrencyType.USD, show_name=True, decimal_places=2)
            except: result.text = "Enter a number"

        def ku(_):
            try:
                a = float(inp.text.replace(",", ""))
                result.text = KurdishCurrency.format(
                    a, use_kurdish_digits=True, show_name=True)
            except: result.text = "Enter a number"

        b1 = KurdishButton(text="IQD"); b1.bind(on_press=iqd)
        b2 = KurdishButton(text="USD"); b2.bind(on_press=usd)
        b3 = KurdishButton(text="Kurdish"); b3.bind(on_press=ku)
        btns.add_widget(b1); btns.add_widget(b2); btns.add_widget(b3)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_plural(self, layout):
        inp = KurdishInput(hint_text="Word or '5 book'...")
        result = ResultLabel()
        layout.add_widget(inp)

        btns = GridLayout(cols=3, size_hint_y=None, height=dp(50), spacing=dp(5))

        def plural(_):
            w = inp.text
            result.text = (
                f"Singular: {w}\n"
                f"Definite: {plural_definite(w)}\n"
                f"Indefinite: {plural_indefinite(w)}"
            )

        def sing(_):
            w = inp.text
            result.text = (
                f"Plural: {w}\n"
                f"Singular: {KurdishPlural.singular(w)}\n"
                f"Is plural: {KurdishPlural.is_plural(w)}"
            )

        def cnt(_):
            try:
                parts = inp.text.split()
                n = int(parts[0])
                w = parts[1] if len(parts) > 1 else "item"
                result.text = KurdishCountSuffix.count(n, w, use_kurdish_digits=True)
            except:
                result.text = "Enter: number word (e.g. 5 book)"

        b1 = KurdishButton(text="Pluralize"); b1.bind(on_press=plural)
        b2 = KurdishButton(text="Singularize"); b2.bind(on_press=sing)
        b3 = KurdishButton(text="Count+Word"); b3.bind(on_press=cnt)
        btns.add_widget(b1); btns.add_widget(b2); btns.add_widget(b3)
        layout.add_widget(btns)
        layout.add_widget(result)

    def _tab_calendar(self, layout):
        result = ResultLabel()
        btns = GridLayout(cols=2, size_hint_y=None, height=dp(150), spacing=dp(5))

        def today(_):
            now = datetime.now()
            result.text = (
                f"Gregorian: {KurdishDateTime.format(now, 'EEEE, dd MMMM yyyy')}\n"
                f"Hijri: {KurdishCalendar.format_hijri(now)}\n"
                f"Kurdish: {KurdishCalendar.format_kurdish(now)}"
            )

        def relative(_):
            now = datetime.now()
            result.text = (
                f"5 min ago: {kurdish_relative_time(now - timedelta(minutes=5))}\n"
                f"3 hrs ago: {kurdish_relative_time(now - timedelta(hours=3))}\n"
                f"Yesterday: {kurdish_relative_time(now - timedelta(days=1))}\n"
                f"Tomorrow: {kurdish_relative_time(now + timedelta(days=1))}"
            )

        def color(_):
            import random
            r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
            result.text = f"RGB({r},{g},{b}) = {KurdishColor.get_closest_name(r,g,b)}"

        def ranges(_):
            result.text = (
                f"1-5: {KurdishNumberRange.to_words(1, 5)}\n"
                f"10-100: {KurdishNumberRange.to_words(10, 100)}\n"
                f"1-1000: {KurdishNumberRange.to_words(1, 1000)}"
            )

        def greet(_):
            result.text = (
                f"Morning: {KurdishGreeting.from_hour(8)}\n"
                f"Noon: {KurdishGreeting.from_hour(14)}\n"
                f"Evening: {KurdishGreeting.from_hour(19)}\n"
                f"Night: {KurdishGreeting.from_hour(23)}\n"
                f"Now: {KurdishGreeting.with_name('Dana')}"
            )

        def validators(_):
            result.text = (
                f"Email test@x.com: {KurdishValidators.email('test@x.com') or 'Valid'}\n"
                f"Email bad: {KurdishValidators.email('bad')}\n"
                f"Phone 07501234567: {KurdishValidators.phone('07501234567') or 'Valid'}\n"
                f"Phone 123: {KurdishValidators.phone('123')}"
            )

        b1 = KurdishButton(text="Today"); b1.bind(on_press=today)
        b2 = KurdishButton(text="Relative Time"); b2.bind(on_press=relative)
        b3 = KurdishButton(text="Color"); b3.bind(on_press=color)
        b4 = KurdishButton(text="Ranges"); b4.bind(on_press=ranges)
        b5 = KurdishButton(text="Greeting"); b5.bind(on_press=greet)
        b6 = KurdishButton(text="Validators"); b6.bind(on_press=validators)
        btns.add_widget(b1); btns.add_widget(b2)
        btns.add_widget(b3); btns.add_widget(b4)
        btns.add_widget(b5); btns.add_widget(b6)
        layout.add_widget(btns)
        layout.add_widget(result)


if __name__ == "__main__":
    KurdishToolsApp().run()
