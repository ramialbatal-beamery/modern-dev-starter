"""Turn arbitrary text into a URL-safe slug.

This is the kind of small, self-contained unit of work that maps nicely
to a single ticket and a single pull request.
"""

import re
import unicodedata

_NON_WORD = re.compile(r"[^\w\s-]")
_WHITESPACE = re.compile(r"[-\s]+")


def slugify(text: str, max_length: int | None = None) -> str:
    """Convert ``text`` into a lowercase, hyphen-separated slug.

    Args:
        text: Any input string, e.g. an article title.
        max_length: Optional cap on the slug length. The result is trimmed
            on a hyphen boundary so words are never cut in half.

    Returns:
        A slug containing only ``a-z``, ``0-9`` and single hyphens, with no
        leading or trailing hyphen.

    Examples:
        >>> slugify("Hello, World!")
        'hello-world'
        >>> slugify("  Crème brûlée  ")
        'creme-brulee'
        >>> slugify("Modern Dev: PRs & CI/CD", max_length=12)
        'modern-dev'
    """
    if not text:
        return ""

    # Normalise accented characters down to plain ASCII (é -> e).
    normalised = unicodedata.normalize("NFKD", text)
    ascii_text = normalised.encode("ascii", "ignore").decode("ascii")

    # Drop anything that isn't a word char, whitespace or hyphen, then
    # collapse runs of whitespace/hyphens into a single hyphen.
    cleaned = _NON_WORD.sub("", ascii_text).strip().lower()
    slug = _WHITESPACE.sub("-", cleaned)

    if max_length is not None and len(slug) > max_length:
        slug = slug[:max_length].rsplit("-", 1)[0]

    # Strip any leading or trailing hyphens that may have been introduced by trimming.
    return slug.strip("-")
