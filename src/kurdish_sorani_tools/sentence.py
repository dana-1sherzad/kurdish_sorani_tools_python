"""
Kurdish Sentence Utilities - ئامرازەکانی ڕستە
Sentence manipulation for Kurdish text.
"""

import re


class KurdishSentence:
    """Kurdish sentence utilities."""

    @staticmethod
    def split_sentences(text: str) -> list[str]:
        """
        Split text into sentences.
        جیاکردنەوەی ڕستەکان

        >>> KurdishSentence.split_sentences("سڵاو. چۆنی؟")
        ['سڵاو', 'چۆنی']
        """
        if not text:
            return []
        return [
            s.strip()
            for s in re.split(r"[.!?؟۔]\s*", text)
            if s.strip()
        ]

    @staticmethod
    def sentence_count(text: str) -> int:
        """
        Count sentences in text.
        ژمردنی ڕستەکان
        """
        return len(KurdishSentence.split_sentences(text))

    @staticmethod
    def ensure_end_punctuation(text: str, mark: str = ".") -> str:
        """
        Add end punctuation if missing.
        زیادکردنی خاڵی کۆتایی ئەگەر نەبوو
        """
        if not text:
            return text
        trimmed = text.rstrip()
        if trimmed and trimmed[-1] in ".!?؟":
            return text
        return f"{trimmed}{mark}"
