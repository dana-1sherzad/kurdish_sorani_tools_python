"""
Kurdish Sorani Tools - Kivy Mobile App
Uses the kurdish-sorani-tools package.
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

import arabic_reshaper
from bidi.algorithm import get_display

# Register Kurdish font
FONT_PATH = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "tahoma.ttf")
if os.path.exists(FONT_PATH):
    LabelBase.register(name="Kurdish", fn_regular=FONT_PATH)
    DEFAULT_FONT = "Kurdish"
else:
    DEFAULT_FONT = "Roboto"

from kurdish_sorani_tools import (
    convert_en_to_ku, convert_ku_to_en, add_commas,
    number_to_words, words_to_number,
    is_kurdish, has_kurdish, fix_url, KurdishOrdinal,
    KurdishDateTime, KurdishKeyboard, KurdishNormalizer,
    KurdishCurrency, CurrencyType, KurdishTextDirection,
    KurdishPlural, plural_definite, plural_indefinite,
    KurdishStringUtils, kurdish_relative_time,
    KurdishPhone, KurdishNumberRange, KurdishSentence,
    KurdishNumberValidator, KurdishValidators,
    KurdishGreeting, kurdish_greeting, KurdishCountSuffix,
    KurdishCalendar, KurdishColor, digit_to_word, StrType,
)

ACCENT = get_color_from_hex("#4fc3f7")
GREEN = get_color_from_hex("#76ff03")
WHITE = get_color_from_hex("#ffffff")


def ku(text):
    """Reshape Kurdish text for correct RTL display in Kivy."""
    if not text:
        return ""
    reshaped = arabic_reshaper.reshape(str(text))
    return get_display(reshaped)


class KurdishToolsApp(App):
    def build(self):
        self.title = "Kurdish Sorani Tools"
        root = BoxLayout(orientation="vertical")

        # Header
        greeting = kurdish_greeting()
        date = KurdishDateTime.today("EEEE, dd MMMM yyyy")
        header = Label(
            text=ku(f"{greeting} - {date}"),
            font_name=DEFAULT_FONT, font_size=sp(15),
            color=ACCENT, bold=True,
            size_hint_y=None, height=dp(60)
        )
        root.add_widget(header)

        # Tabs
        tp = TabbedPanel(do_default_tab=False, tab_width=dp(100))
        tabs = [
            ("Number", self._tab_number),
            ("Digits", self._tab_digits),
            ("Keyboard", self._tab_keyboard),
            ("Normalize", self._tab_normalizer),
            ("Phone", self._tab_phone),
            ("Detect", self._tab_detect),
            ("Currency", self._tab_currency),
            ("Plural", self._tab_plural),
            ("Calendar", self._tab_calendar),
        ]
        for name, builder in tabs:
            tab = TabbedPanelItem(text=name)
            scroll = ScrollView()
            layout = BoxLayout(orientation="vertical", padding=dp(12),
                               spacing=dp(8), size_hint_y=None)
            layout.bind(minimum_height=layout.setter("height"))
            builder(layout)
            scroll.add_widget(layout)
            tab.add_widget(scroll)
            tp.add_widget(tab)

        root.add_widget(tp)
        return root

    def _inp(self, layout, hint=""):
        inp = TextInput(
            hint_text=hint, font_name=DEFAULT_FONT, font_size=sp(15),
            size_hint_y=None, height=dp(48), multiline=False,
            background_color=get_color_from_hex("#0f3460"),
            foreground_color=WHITE, cursor_color=ACCENT,
            padding=[dp(10), dp(12)]
        )
        layout.add_widget(inp)
        return inp

    def _result(self, layout):
        lbl = Label(
            text="", font_name=DEFAULT_FONT, font_size=sp(15),
            color=GREEN, halign="center", valign="middle",
            size_hint_y=None, height=dp(80)
        )
        lbl.bind(size=lambda *a: setattr(lbl, 'text_size', (lbl.width, None)))
        layout.add_widget(lbl)
        return lbl

    def _btn(self, layout, texts_and_fns):
        cols = min(len(texts_and_fns), 3)
        grid = GridLayout(cols=cols, size_hint_y=None,
                          height=dp(50 * ((len(texts_and_fns) + cols - 1) // cols)),
                          spacing=dp(4))
        for text, fn in texts_and_fns:
            b = Button(text=text, font_name=DEFAULT_FONT, font_size=sp(12),
                       background_color=get_color_from_hex("#0f3460"),
                       color=ACCENT, bold=True, size_hint_y=None, height=dp(44))
            b.bind(on_press=fn)
            grid.add_widget(b)
        layout.add_widget(grid)

    def _tab_number(self, layout):
        inp = self._inp(layout, "Enter number (12345)")
        res = self._result(layout)

        def v1(_):
            try: res.text = ku(number_to_words(int(inp.text.replace(",", ""))))
            except: res.text = "Enter a valid number"

        def v2(_):
            r = digit_to_word(inp.text, StrType.STR_WORD)
            res.text = ku(r) if r else "Enter a number"

        def ordinal(_):
            try: res.text = ku(KurdishOrdinal.from_number(int(inp.text.replace(",", ""))))
            except: res.text = "Enter a number"

        self._btn(layout, [("To Words V1", v1), ("To Words V2", v2), ("Ordinal", ordinal)])

    def _tab_digits(self, layout):
        inp = self._inp(layout, "Enter number or text")
        res = self._result(layout)

        def to_ku(_): res.text = ku(convert_en_to_ku(inp.text))
        def to_en(_): res.text = convert_ku_to_en(inp.text)
        def comma(_): res.text = add_commas(inp.text.replace(",", ""))
        def w2n(_):
            r = words_to_number(inp.text)
            res.text = str(r) if r is not None else "Could not convert"

        self._btn(layout, [("To Kurdish", to_ku), ("To English", to_en),
                           ("Commas", comma), ("Words->Num", w2n)])

    def _tab_keyboard(self, layout):
        inp = self._inp(layout, "Type English (slaw)")
        res = self._result(layout)

        def en2ku(_): res.text = ku(KurdishKeyboard.en_to_ku(inp.text))
        def ku2en(_): res.text = KurdishKeyboard.ku_to_en(inp.text)

        self._btn(layout, [("EN -> Kurdish", en2ku), ("Kurdish -> EN", ku2en)])

    def _tab_normalizer(self, layout):
        inp = self._inp(layout, "Enter text or URL")
        res = self._result(layout)

        def norm(_): res.text = ku(KurdishNormalizer.normalize(inp.text))
        def norm_all(_): res.text = ku(KurdishNormalizer.normalize_all(inp.text))
        def slug(_): res.text = KurdishStringUtils.to_slug(inp.text)
        def url(_): res.text = fix_url(inp.text)

        self._btn(layout, [("Normalize", norm), ("Full Normalize", norm_all),
                           ("Slug", slug), ("Fix URL", url)])

    def _tab_phone(self, layout):
        inp = self._inp(layout, "07501234567")
        res = self._result(layout)

        def check(_):
            p = inp.text
            valid = KurdishPhone.is_valid(p)
            op = KurdishPhone.get_operator(p) or "Unknown"
            intl = KurdishPhone.to_international(p) if valid else "-"
            txt = f"Format: {KurdishPhone.format(p)}\nOperator: {ku(op)}\nValid: {'Yes' if valid else 'No'}\nIntl: {intl}"
            res.text = txt

        self._btn(layout, [("Check Phone", check)])

    def _tab_detect(self, layout):
        inp = self._inp(layout, "Enter text")
        res = self._result(layout)

        def check_ku(_):
            t = inp.text
            if is_kurdish(t): res.text = ku("تەواوی دەقەکە کوردییە")
            elif has_kurdish(t): res.text = ku("هەندێک پیتی کوردی تێدایە")
            else: res.text = "No Kurdish detected"

        def direction(_):
            d = KurdishTextDirection.detect_direction(inp.text)
            res.text = f"Direction: {d.upper()}"

        def count(_):
            t = inp.text
            res.text = f"Words: {KurdishStringUtils.word_count(t)} | Chars: {KurdishStringUtils.char_count(t)} | Sentences: {KurdishSentence.sentence_count(t)}"

        def numval(_):
            t = inp.text
            if KurdishNumberValidator.is_kurdish_number(t): res.text = "Kurdish number"
            elif KurdishNumberValidator.is_number(t): res.text = "Valid number"
            else: res.text = "Not a number"

        self._btn(layout, [("Is Kurdish?", check_ku), ("Direction", direction),
                           ("Count", count), ("Number?", numval)])

    def _tab_currency(self, layout):
        inp = self._inp(layout, "Amount (1500000)")
        res = self._result(layout)

        def iqd(_):
            try:
                a = float(inp.text.replace(",", ""))
                res.text = ku(KurdishCurrency.format(a, show_name=True))
            except: res.text = "Enter a number"

        def usd(_):
            try:
                a = float(inp.text.replace(",", ""))
                res.text = KurdishCurrency.format(a, currency=CurrencyType.USD, show_name=True, decimal_places=2)
            except: res.text = "Enter a number"

        def ku_d(_):
            try:
                a = float(inp.text.replace(",", ""))
                res.text = ku(KurdishCurrency.format(a, use_kurdish_digits=True, show_name=True))
            except: res.text = "Enter a number"

        self._btn(layout, [("IQD", iqd), ("USD", usd), ("Kurdish Digits", ku_d)])

    def _tab_plural(self, layout):
        inp = self._inp(layout, "Word (or: 5 word)")
        res = self._result(layout)

        def plural(_):
            w = inp.text
            res.text = ku(f"{w} -> {plural_definite(w)} / {plural_indefinite(w)}")

        def sing(_):
            w = inp.text
            res.text = ku(f"{w} -> {KurdishPlural.singular(w)} (plural: {KurdishPlural.is_plural(w)})")

        def cnt(_):
            try:
                parts = inp.text.split()
                n, w = int(parts[0]), parts[1] if len(parts) > 1 else "item"
                res.text = ku(KurdishCountSuffix.count(n, w, use_kurdish_digits=True))
            except: res.text = "Enter: number word"

        self._btn(layout, [("Pluralize", plural), ("Singularize", sing), ("Count", cnt)])

    def _tab_calendar(self, layout):
        res = self._result(layout)

        def today(_):
            now = datetime.now()
            g = KurdishDateTime.format(now, "EEEE, dd MMMM yyyy")
            h = KurdishCalendar.format_hijri(now)
            k = KurdishCalendar.format_kurdish(now)
            res.text = f"{ku(g)}\n{ku(h)}\n{ku(k)}"

        def relative(_):
            now = datetime.now()
            r1 = kurdish_relative_time(now - timedelta(minutes=5))
            r2 = kurdish_relative_time(now - timedelta(hours=3))
            r3 = kurdish_relative_time(now + timedelta(days=1))
            res.text = f"{ku(r1)}\n{ku(r2)}\n{ku(r3)}"

        def color(_):
            import random
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            res.text = f"RGB({r},{g},{b}) = {ku(KurdishColor.get_closest_name(r, g, b))}"

        def ranges(_):
            res.text = f"1-5: {ku(KurdishNumberRange.to_words(1, 5))}\n10-100: {ku(KurdishNumberRange.to_words(10, 100))}"

        def greet(_):
            res.text = ku(KurdishGreeting.with_name("Dana"))

        def validators(_):
            e1 = KurdishValidators.email("test@x.com") or "Valid"
            e2 = KurdishValidators.email("bad")
            p1 = KurdishValidators.phone("07501234567") or "Valid"
            res.text = f"Email: {e1}\nBad email: {ku(e2)}\nPhone: {p1}"

        self._btn(layout, [("Today", today), ("Relative", relative),
                           ("Color", color), ("Ranges", ranges),
                           ("Greeting", greet), ("Validators", validators)])


if __name__ == "__main__":
    KurdishToolsApp().run()
