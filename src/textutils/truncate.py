"""Shorten long strings for display, appending an ellipsis when text is cut."""

_ELLIPSIS = "…"


def truncate(text: str, limit: int) -> str:
    """Shorten ``text`` to at most ``limit`` characters, breaking on word boundaries.

    Args:
        text: The string to shorten.
        limit: Maximum character count of the returned string (inclusive of the
            ellipsis when one is added).

    Returns:
        ``text`` unchanged when it already fits within ``limit``.  Otherwise a
        shortened string ending with ``…``, trimmed on the last space that fits
        so words are not cut in half.

    Examples:
        >>> truncate("Hello, World!", 8)
        'Hello,…'
        >>> truncate("Hello World", 8)
        'Hello…'
        >>> truncate("Hello", 10)
        'Hello'
        >>> truncate("", 10)
        ''
    """
    if not text:
        return ""
    if len(text) <= limit:
        return text
    if limit <= 0:
        return ""

    available = limit - 1  # one char reserved for the ellipsis
    if available == 0:
        return _ELLIPSIS

cut = text[:available]
space_pos = cut.rfind(" ")
if space_pos > 0:
    cut = cut[:space_pos]

    return cut + _ELLIPSIS
