"""
Kurdish Sorani Tools - Tkinter Desktop App
ئامرازەکانی کوردی سۆرانی - ئەپی دێسکتۆپ

Uses the kurdish-sorani-tools package (pip install kurdish-sorani-tools).
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Import everything from the package
from kurdish_sorani_tools import (
    # Digits
    convert_en_to_ku,
    convert_ku_to_en,
    # Commas
    add_commas,
    remove_commas,
    # Number to words
    number_to_words,
    number_to_words_string,
    # Words to number
    words_to_number,
    words_to_number_string,
    # Kurdish detection
    is_kurdish,
    has_kurdish,
    # URL fix
    fix_url,
    # Ordinal
    KurdishOrdinal,
    # Date/Time
    KurdishDateTime,
    kurdish_date_format,
    # Keyboard
    KurdishKeyboard,
    # Normalizer
    KurdishNormalizer,
    # Currency
    KurdishCurrency,
    CurrencyType,
    # Text direction
    KurdishTextDirection,
    # Pluralization
    KurdishPlural,
    plural_definite,
    plural_indefinite,
    # String utils
    KurdishStringUtils,
    # Relative time
    KurdishRelativeTime,
    kurdish_relative_time,
    # Phone
    KurdishPhone,
    format_phone,
    # Number range
    KurdishNumberRange,
    # Sentence
    KurdishSentence,
    # Number validator
    KurdishNumberValidator,
    # Validators
    KurdishValidators,
    # Greeting
    KurdishGreeting,
    kurdish_greeting,
    # Count suffix
    KurdishCountSuffix,
    # Calendar
    KurdishCalendar,
    HijriDate,
    KurdishDate,
    # Color
    KurdishColor,
    # Digit to word
    digit_to_word,
    StrType,
)


# ═══════════════════════════════════════════════════════
# Tkinter Application
# ═══════════════════════════════════════════════════════

class KurdishToolsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ئامرازەکانی کوردی سۆرانی")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(True, True)

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#1a1a2e")
        style.configure("TNotebook.Tab", padding=[10, 5],
                        font=("Segoe UI", 9))
        style.configure("TFrame", background="#16213e")
        style.configure("TLabel", background="#16213e",
                        foreground="#e0e0e0", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 10, "bold"),
                        padding=[10, 5])
        style.configure("Header.TLabel", font=("Segoe UI", 13, "bold"),
                        foreground="#4fc3f7")

        self._build_header()
        self._build_notebook()

    def _build_header(self):
        header = tk.Frame(self.root, bg="#0f3460", height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        greeting = kurdish_greeting()
        date = KurdishDateTime.today("EEEE، dd MMMM yyyy")

        tk.Label(header, text=f"🌟 {greeting} — {date}",
                 bg="#0f3460", fg="#4fc3f7",
                 font=("Segoe UI", 12, "bold")).pack(pady=15)

    def _build_notebook(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=8, pady=8)

        self._tab_number_to_words(notebook)
        self._tab_digit_converter(notebook)
        self._tab_keyboard(notebook)
        self._tab_normalizer(notebook)
        self._tab_phone(notebook)
        self._tab_detection(notebook)
        self._tab_currency(notebook)
        self._tab_plural(notebook)
        self._tab_relative_time(notebook)
        self._tab_calendar(notebook)

    # ─── Helpers ───
    def _make_frame(self, notebook, title):
        frame = ttk.Frame(notebook, padding=15)
        notebook.add(frame, text=title)
        return frame

    def _make_entry(self, parent, row, label_text, width=35):
        ttk.Label(parent, text=label_text).grid(
            row=row, column=0, sticky="e", padx=5, pady=6)
        entry = tk.Entry(parent, width=width, font=("Segoe UI", 12),
                         bg="#1a1a2e", fg="#ffffff",
                         insertbackground="#4fc3f7",
                         relief="flat", highlightthickness=1,
                         highlightcolor="#4fc3f7")
        entry.grid(row=row, column=1, sticky="w", padx=5, pady=6)
        return entry

    def _make_result(self, parent, row):
        result_var = tk.StringVar()
        lbl = tk.Label(parent, textvariable=result_var,
                       font=("Segoe UI", 12, "bold"),
                       bg="#16213e", fg="#76ff03", wraplength=500,
                       justify="right")
        lbl.grid(row=row, column=0, columnspan=3, pady=12, sticky="ew")
        return result_var

    # ─── Tab 1: Number to Words ───
    def _tab_number_to_words(self, notebook):
        frame = self._make_frame(notebook, "ژمارە بۆ وشە")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="گۆڕینی ژمارە بۆ نووسینی کوردی",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":ژمارە")
        result_var = self._make_result(frame, 4)

        def convert_v1():
            try:
                num = int(entry.get().replace(",", ""))
                result_var.set(number_to_words(num))
            except ValueError:
                result_var.set("⚠️ تکایە ژمارەیەکی ڕاست بنووسە")

        def convert_v2():
            text = entry.get()
            result = digit_to_word(text, StrType.STR_WORD)
            result_var.set(result if result else "⚠️ ژمارە بنووسە")

        def to_ordinal():
            try:
                num = int(entry.get().replace(",", ""))
                result_var.set(KurdishOrdinal.from_number(num))
            except ValueError:
                result_var.set("⚠️ ژمارە بنووسە")

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="گۆڕین V1", command=convert_v1).pack(
            side="left", padx=4)
        ttk.Button(btn_frame, text="گۆڕین V2", command=convert_v2).pack(
            side="left", padx=4)
        ttk.Button(btn_frame, text="ڕێزبەندی (ەم)", command=to_ordinal).pack(
            side="left", padx=4)

    # ─── Tab 2: Digit Converter ───
    def _tab_digit_converter(self, notebook):
        frame = self._make_frame(notebook, "گۆڕینی ژمارە")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="گۆڕینی ژمارە و فاریزە",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":ژمارە/دەق")
        result_var = self._make_result(frame, 4)

        def to_kurdish():
            result_var.set(convert_en_to_ku(entry.get()))

        def to_english():
            result_var.set(convert_ku_to_en(entry.get()))

        def to_commas():
            text = entry.get().replace(",", "")
            result_var.set(add_commas(text))

        def words_to_num():
            result = words_to_number(entry.get())
            result_var.set(str(result) if result is not None else "⚠️")

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="بۆ کوردی ١٢٣",
                   command=to_kurdish).pack(side="left", padx=3)
        ttk.Button(btn_frame, text="بۆ ئینگلیزی 123",
                   command=to_english).pack(side="left", padx=3)
        ttk.Button(btn_frame, text="فاریزە 1,000",
                   command=to_commas).pack(side="left", padx=3)
        ttk.Button(btn_frame, text="وشە→ژمارە",
                   command=words_to_num).pack(side="left", padx=3)

    # ─── Tab 3: Keyboard Converter ───
    def _tab_keyboard(self, notebook):
        frame = self._make_frame(notebook, "کیبۆرد")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="گۆڕینی لەیاوتی کیبۆرد",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":دەق")
        result_var = self._make_result(frame, 4)

        def en_to_ku():
            result_var.set(KurdishKeyboard.en_to_ku(entry.get()))

        def ku_to_en():
            result_var.set(KurdishKeyboard.ku_to_en(entry.get()))

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="ئینگلیزی → کوردی ⌨️",
                   command=en_to_ku).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="کوردی → ئینگلیزی ⌨️",
                   command=ku_to_en).pack(side="left", padx=5)

    # ─── Tab 4: Text Normalizer ───
    def _tab_normalizer(self, notebook):
        frame = self._make_frame(notebook, "نۆرمالکردن")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="نۆرمالکردنی دەقی کوردی",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":دەق")
        result_var = self._make_result(frame, 4)

        def normalize():
            result_var.set(KurdishNormalizer.normalize(entry.get()))

        def normalize_all():
            result_var.set(KurdishNormalizer.normalize_all(entry.get()))

        def to_slug():
            result_var.set(KurdishStringUtils.to_slug(entry.get()))

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="نۆرمال",
                   command=normalize).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="نۆرمالی تەواو",
                   command=normalize_all).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Slug بۆ URL",
                   command=to_slug).pack(side="left", padx=4)

    # ─── Tab 5: Phone Number ───
    def _tab_phone(self, notebook):
        frame = self._make_frame(notebook, "مۆبایل")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="فۆرماتکردنی ژمارەی مۆبایلی عراقی",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":ژمارە")
        result_var = self._make_result(frame, 3)

        def check():
            phone = entry.get()
            formatted = KurdishPhone.format(phone)
            valid = KurdishPhone.is_valid(phone)
            operator = KurdishPhone.get_operator(phone) or "نەناسراو"
            intl = KurdishPhone.to_international(phone) if valid else "—"
            lines = [
                f"فۆرمات: {formatted}",
                f"ئۆپەرەیتەر: {operator}",
                f"ڕاستە؟: {'بەڵێ ✅' if valid else 'نەخێر ❌'}",
                f"نێودەوڵەتی: {intl}",
            ]
            result_var.set("\n".join(lines))

        ttk.Button(frame, text="پشکنین 📱", command=check).grid(
            row=2, column=1, pady=8, sticky="w")

    # ─── Tab 6: Kurdish Detection ───
    def _tab_detection(self, notebook):
        frame = self._make_frame(notebook, "دۆزینەوە")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="پشکنینی دەق",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":دەق")
        result_var = self._make_result(frame, 4)

        def check_kurdish():
            text = entry.get()
            if is_kurdish(text):
                result_var.set("✅ تەواوی دەقەکە کوردییە")
            elif has_kurdish(text):
                result_var.set("⚠️ هەندێک پیتی کوردی تێدایە")
            else:
                result_var.set("❌ هیچ پیتی کوردی تێدا نییە")

        def check_direction():
            text = entry.get()
            direction = KurdishTextDirection.detect_direction(text)
            result_var.set(
                f"ئاڕاستە: {'ڕاست بۆ چەپ (RTL) ←' if direction == 'rtl' else 'چەپ بۆ ڕاست (LTR) →'}"
            )

        def word_count():
            text = entry.get()
            wc = KurdishStringUtils.word_count(text)
            cc = KurdishStringUtils.char_count(text)
            sc = KurdishSentence.sentence_count(text)
            result_var.set(
                f"وشە: {wc} | پیت: {cc} | ڕستە: {sc}"
            )

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="کوردییە؟ 🔍",
                   command=check_kurdish).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="ئاڕاستە ↔",
                   command=check_direction).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="ژمردن 📊",
                   command=word_count).pack(side="left", padx=4)

    # ─── Tab 7: Currency ───
    def _tab_currency(self, notebook):
        frame = self._make_frame(notebook, "دراو")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="فۆرماتکردنی دراو",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":بڕ")
        result_var = self._make_result(frame, 4)

        def format_iqd():
            try:
                amount = float(entry.get().replace(",", ""))
                result_var.set(KurdishCurrency.format(
                    amount, currency=CurrencyType.IQD, show_name=True))
            except ValueError:
                result_var.set("⚠️ ژمارە بنووسە")

        def format_usd():
            try:
                amount = float(entry.get().replace(",", ""))
                result_var.set(KurdishCurrency.format(
                    amount, currency=CurrencyType.USD,
                    show_name=True, decimal_places=2))
            except ValueError:
                result_var.set("⚠️ ژمارە بنووسە")

        def format_ku_digits():
            try:
                amount = float(entry.get().replace(",", ""))
                result_var.set(KurdishCurrency.format(
                    amount, currency=CurrencyType.IQD,
                    use_kurdish_digits=True, show_name=True))
            except ValueError:
                result_var.set("⚠️ ژمارە بنووسە")

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="دیناری عراقی",
                   command=format_iqd).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="دۆلار",
                   command=format_usd).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="بە ژمارەی کوردی",
                   command=format_ku_digits).pack(side="left", padx=4)

    # ─── Tab 8: Pluralization ───
    def _tab_plural(self, notebook):
        frame = self._make_frame(notebook, "کۆکردنەوە")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="کۆکردنەوەی وشەکان بە کوردی",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":وشە")
        result_var = self._make_result(frame, 4)

        def definite():
            result_var.set(
                f"تاک: {entry.get()}\n"
                f"کۆ (دیاری): {plural_definite(entry.get())}\n"
                f"کۆ (نادیاری): {plural_indefinite(entry.get())}"
            )

        def singular():
            word = entry.get()
            result_var.set(
                f"کۆ: {word}\n"
                f"تاک: {KurdishPlural.singular(word)}\n"
                f"کۆیە؟: {'بەڵێ' if KurdishPlural.is_plural(word) else 'نەخێر'}"
            )

        def count_word():
            try:
                parts = entry.get().split()
                num = int(parts[0])
                word = parts[1] if len(parts) > 1 else "شت"
                result_var.set(KurdishCountSuffix.count(num, word,
                               use_kurdish_digits=True))
            except (ValueError, IndexError):
                result_var.set("⚠️ ژمارە و وشە بنووسە (وەک: 5 کتێب)")

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="کۆکردنەوە",
                   command=definite).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="تاککردنەوە",
                   command=singular).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="ژمارە+وشە",
                   command=count_word).pack(side="left", padx=4)

    # ─── Tab 9: Relative Time ───
    def _tab_relative_time(self, notebook):
        frame = self._make_frame(notebook, "کاتی نسبی")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="کاتی نسبی بە کوردی",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        entry = self._make_entry(frame, 1, ":خولەک لەمەوپێش")
        result_var = self._make_result(frame, 4)

        def calc_past():
            try:
                minutes = int(entry.get())
                past = datetime.now() - timedelta(minutes=minutes)
                result_var.set(kurdish_relative_time(past))
            except ValueError:
                result_var.set("⚠️ ژمارەی خولەک بنووسە")

        def calc_future():
            try:
                minutes = int(entry.get())
                future = datetime.now() + timedelta(minutes=minutes)
                result_var.set(kurdish_relative_time(future))
            except ValueError:
                result_var.set("⚠️ ژمارەی خولەک بنووسە")

        def show_range():
            text = entry.get()
            result = KurdishNumberRange.parse_and_convert(text)
            if result:
                result_var.set(result)
            else:
                result_var.set("⚠️ ڕیز بنووسە وەک 1-10")

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="لەمەوپێش ⏪",
                   command=calc_past).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="لە داهاتوودا ⏩",
                   command=calc_future).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="ڕیز (1-10)",
                   command=show_range).pack(side="left", padx=4)

    # ─── Tab 10: Calendar ───
    def _tab_calendar(self, notebook):
        frame = self._make_frame(notebook, "ڕۆژژمێر")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="ڕۆژژمێری کوردی و هیجری",
                  style="Header.TLabel").grid(
            row=0, column=0, columnspan=3, pady=8)

        result_var = self._make_result(frame, 2)

        def show_today():
            now = datetime.now()
            gregorian = KurdishDateTime.format(now, "EEEE، dd MMMM yyyy")
            hijri = KurdishCalendar.format_hijri(now)
            kurdish_cal = KurdishCalendar.format_kurdish(now)
            greeting = KurdishGreeting.now()

            lines = [
                f"🌟 {greeting}",
                f"📅 گریگۆری: {gregorian}",
                f"🕌 هیجری: {hijri}",
                f"☀️ کوردی (ڕۆژهەڵاتی): {kurdish_cal}",
            ]
            result_var.set("\n".join(lines))

        def show_color():
            import random
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            name = KurdishColor.get_closest_name(r, g, b)
            hex_color = f"#{r:02x}{g:02x}{b:02x}"
            result_var.set(f"🎨 ڕەنگ: {hex_color} = {name}")

        def show_validators():
            lines = [
                f"ئیمەیل test@test.com: {KurdishValidators.email('test@test.com') or '✅ ڕاستە'}",
                f"ئیمەیل bad: {KurdishValidators.email('bad')}",
                f"مۆبایل 07501234567: {KurdishValidators.phone('07501234567') or '✅ ڕاستە'}",
                f"مۆبایل 12345: {KurdishValidators.phone('12345')}",
            ]
            result_var.set("\n".join(lines))

        btn_frame = tk.Frame(frame, bg="#16213e")
        btn_frame.grid(row=1, column=0, columnspan=3, pady=8)
        ttk.Button(btn_frame, text="بەرواری ئەمڕۆ 📅",
                   command=show_today).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="ڕەنگ 🎨",
                   command=show_color).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="پشکنینی فۆرم ✓",
                   command=show_validators).pack(side="left", padx=4)

    def run(self):
        self.root.mainloop()


# ═══════════════════════════════════════════════════════
# Entry Point
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    app = KurdishToolsApp()
    app.run()
