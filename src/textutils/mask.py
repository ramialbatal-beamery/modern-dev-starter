"""Mask the local part of an email address for display.

This helper hides the local part of an email so full addresses are never
shown in the UI. It does light *structural* validation only (is this shaped
like an email?) and deliberately does NOT try to fully validate that an
address is real or deliverable — that belongs wherever emails enter the
system, not in a display helper.
"""

_MASK = "***"


def mask_email(email: str) -> str:
    """Mask the local part of an email address.

      >>> mask_email("rami@beamery.com")
      '***@beamery.com'
      """
    if not isinstance(email, str):
        raise TypeError(f"email must be a string, got {type(email).__name__}")

    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError(f"not a valid email address: {email!r}")

    _, domain = parts
    return f"{_MASK}@{domain}"