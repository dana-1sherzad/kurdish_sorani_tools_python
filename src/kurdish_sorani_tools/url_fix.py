"""
URL Fix - چاککردنی لینک
Fix spaces in URLs by replacing them with %20.
"""

import re
from urllib.parse import unquote


def fix_url(url: str) -> str:
    """
    Fix a URL by replacing spaces with %20.
    لینکێک دابنێ گەر کێشەی هەبوو خۆی ئۆتۆماتیکی %20ی بۆ دادەنێت

    >>> fix_url("https://example.com/my file.pdf")
    'https://example.com/my%20file.pdf'
    """
    url_pattern = r"(http\S+|ws\S+)"
    is_url = bool(re.search(url_pattern, url))
    url = unquote(url)
    if is_url:
        url = re.sub(r"\s", "%20", url)
    return url
