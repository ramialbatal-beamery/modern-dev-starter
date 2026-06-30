from textutils import truncate


def test_short_text_unchanged():
    assert truncate("Hello", 10) == "Hello"


def test_exact_length_boundary():
    assert truncate("Hello", 5) == "Hello"


def test_long_text_truncated_with_ellipsis():
    # "Hello,…" is 7 chars, fits within limit=8
    assert truncate("Hello, World!", 8) == "Hello,…"


def test_empty_string_returns_empty():
    assert truncate("", 10) == ""


def test_word_boundary_respected():
    # "Hello W" cut at limit-1=7 chars; last space at pos 5 -> "Hello" + "…"
    assert truncate("Hello World", 8) == "Hello…"


def test_no_space_cuts_at_character_boundary():
    # No space in "Superlongword", so cut at available chars directly
    result = truncate("Superlongword", 6)
    assert result == "Super…"
    assert len(result) <= 6
