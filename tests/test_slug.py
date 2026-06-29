"""Tests for textutils.slugify.

A test file is a contract: each test states "given this input, I expect
this output". CI runs these on every push, so a green tick on your PR
means none of these contracts were broken.
"""

from textutils import slugify


def test_basic_lowercasing_and_spaces():
    assert slugify("Hello World") == "hello-world"


def test_strips_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_handles_accented_characters():
    assert slugify("Crème brûlée") == "creme-brulee"


def test_collapses_repeated_separators():
    assert slugify("a   b---c") == "a-b-c"


def test_trims_leading_and_trailing_hyphens():
    assert slugify("--hello--") == "hello"


def test_empty_string_returns_empty():
    assert slugify("") == ""


def test_max_length_trims_on_word_boundary():
    # Should not cut a word in half: "modern-dev-prs" capped at 12 -> "modern-dev".
    assert slugify("Modern Dev PRs", max_length=12) == "modern-dev"
