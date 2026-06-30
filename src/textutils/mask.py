"""Mask the local part of an email address for display."""


def mask_email(email):
    local, domain = email.split("@")
    masked = local[:3] + "***"
    return masked + "@" + domain