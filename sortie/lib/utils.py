"""Various utilities that don't fit into other categories."""

import unicodedata


def strip_accents(text):
    """Remove accents from a unicode string."""
    def _not_combining(char):
        return unicodedata.category(char) != 'Mn'
    unicode_text = unicodedata.normalize('NFD', text)
    return filter(_not_combining, unicode_text)
