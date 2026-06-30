from textutils import mask_email


def test_masks_a_normal_email():
    assert mask_email("rami@beamery.com") == "ram***@beamery.com"