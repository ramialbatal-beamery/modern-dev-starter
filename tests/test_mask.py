import pytest

from textutils import mask_email


def test_masks_a_normal_email():
    assert mask_email("rami@beamery.com") == "***@beamery.com"


def test_masks_a_short_local_part_completely():
    assert mask_email("ram@beamery.com") == "***@beamery.com"
    assert mask_email("a@beamery.com") == "***@beamery.com"


def test_rejects_string_without_at_sign():
    with pytest.raises(ValueError):
        mask_email("notanemail")


def test_rejects_string_with_multiple_at_signs():
    with pytest.raises(ValueError):
        mask_email("a@b@c.com")


def test_rejects_empty_local_or_domain():
    with pytest.raises(ValueError):
        mask_email("@beamery.com")
    with pytest.raises(ValueError):
        mask_email("rami@")


def test_rejects_non_string_input():
    with pytest.raises(TypeError):
        mask_email(None)
    with pytest.raises(TypeError):
        mask_email(12345)