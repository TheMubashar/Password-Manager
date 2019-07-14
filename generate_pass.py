"""
Contributer: awr417h
Description: Generates random password using the stored characters
"""

def generate_password(length):
    """
    : @param: Length -> the length of characters that it should generate.
    : @return: returns a string of randomly generated characters.
    """
    if not isinstance(length, int) or length < 8:
        raise ValueError("temp password must have positive length")

    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789~`!@#$%^&*()_+=;:'?<>,."
    from os import urandom
    return "".join(chars[ord(c) % len(chars)] for c in urandom(length))