# MIT License
#
# Copyright (c) 2018-2019 Groupe Allo-Media
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Dict, Optional, Set, Tuple

from .base import Language

#
# CONSTANTS
#

MULTIPLIERS = {
    "duizend": 1000,
    "duizenden": 1000,
    "miljoen": 1_000_000,
    "miljoenen": 1_000_000,
    "miljard": 1_000_000_000,
    "miljarden": 1_000_000_000,
    "biljoen": 1_000_000_000_000,
    "biljoenen": 1_000_000_000_000,
}

UNITS: Dict[str, int] = {
    "een": 1,
    "twee": 2,
    "drie": 3,
    "vier": 4,
    "vijf": 5,
    "zes": 6,
    "zeven": 7,
    "acht": 8,
    "negen": 9,
}

STENS: Dict[str, int] = {
    "tien": 10,
    "elf": 11,
    "twaalf": 12,
    "dertien": 13,
    "veertien": 14,
    "vijftien": 15,
    "zestien": 16,
    "zeventien": 17,
    "achttien": 18,
    "negentien": 19,
}

MTENS: Dict[str, int] = {
    "twintig": 20,
    "dertig": 30,
    "veertig": 40,
    "vijftig": 50,
    "zestig": 60,
    "zeventig": 70,
    "tachtig": 80,
    "negentig": 90,
}

HUNDRED = {
    "honderd": 100,
    "honderden": 100,
}

# In Dutch, composite numbers like “21” = “eenentwintig”
# We’ll build them programmatically for 21..99 (excluding the teen range).
COMPOSITES: Dict[str, int] = {}
for ten_word, ten_val in MTENS.items():
    for unit_word, unit_val in UNITS.items():
        # Basic pattern is “een + en + twintig” => “eenentwintig”
        # For correct spelling with diacritics (e.g. tweeëntwintig), you’d
        # normally insert ë for “twee”/“drie”/etc. Here we simplify.
        composite_word = unit_word + "en" + ten_word
        composite_val = ten_val + unit_val
        COMPOSITES[composite_word] = composite_val

# Combine all into one dictionary for quick lookups.
NUMBERS = {}
NUMBERS.update(MULTIPLIERS)
NUMBERS.update(UNITS)
NUMBERS.update(STENS)
NUMBERS.update(MTENS)
NUMBERS.update(HUNDRED)
NUMBERS.update(COMPOSITES)

# This maps certain “radical” stems used in ordinals to their base cardinal.
# In English, the code uses e.g. fif->five, eigh->eight, etc.
# You can expand or modify if desired in Dutch. 
RAD_MAP = {}

# Dutch ordinals can be tricky because of suffixes:
# -de or -ste, plus irregulars like ‘eerste’, ‘tweede’, ‘derde’.
# We'll capture the most common ones directly in a dictionary.
ORDINALS_MAP = {
    # Irregular forms:
    "eerste": "een",
    "tweede": "twee",
    "derde": "drie",
    # Then typically: vierde, vijfde, zesde, zevende, achtste, negende, etc.
    "vierde": "vier",
    "vijfde": "vijf",
    "zesde": "zes",
    "zevende": "zeven",
    "achtste": "acht",
    "negende": "negen",
    "tiende": "tien",
    "elfde": "elf",
    "twaalfde": "twaalf",
    "dertiende": "dertien",
    "veertiende": "veertien",
    "vijftiende": "vijftien",
    "zestiende": "zestien",
    "zeventiende": "zeventien",
    "achttiende": "achttien",
    "negentiende": "negentien",
    # Some tens:
    "twintigste": "twintig",
    "dertigste": "dertig",
    "veertigste": "veertig",
    "vijftigste": "vijftig",
    "zestigste": "zestig",
    "zeventigste": "zeventig",
    "tachtigste": "tachtig",
    "negentigste": "negentig",
    # You can add hundreds, thousands, etc. if you like.
}


# Some sets for advanced usage, parallel to the English version:
MTENS_WSTENS: Set[str] = set()
AND_NUMS: Set[str] = set()
RELAXED: Dict[str, Tuple[str, str]] = {}


class Dutch(Language):
    MULTIPLIERS = MULTIPLIERS
    UNITS = UNITS
    STENS = STENS
    MTENS = MTENS
    MTENS_WSTENS = MTENS_WSTENS
    HUNDRED = HUNDRED
    NUMBERS = NUMBERS

    SIGN = {"plus": "+", "minus": "-"}
    ZERO = {"nul"}
    # Dutch might say “komma” for the decimal point or “punt” – adapt as needed.
    DECIMAL_SEP = "komma"
    DECIMAL_SYM = ","

    AND = "en"  # Dutch sometimes omits it, but we mirror the English structure.
    AND_NUMS: Set[str] = AND_NUMS
    NEVER_IF_ALONE = {"een"}  # Just like "one" in English

    # Relaxed multiword forms (optional):
    RELAXED: Dict[str, Tuple[str, str]] = RELAXED

    def ord2card(self, word: str) -> Optional[str]:
        """
        Convert an ordinal number word (e.g. 'tweede', 'dertiende') 
        to its cardinal form (e.g. 'twee', 'dertien').
        Return None if the word is not recognized as an ordinal or 
        if it’s better left in letters.
        """
        # Directly check dictionary first:
        if word in ORDINALS_MAP:
            return ORDINALS_MAP[word]

        # If not in the direct map, maybe it has 'ste' or 'de' suffix we can strip,
        # then see if the remainder is in NUMBERS.
        possible_suffixes = ("ste", "de")
        for suffix in possible_suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                # Strip suffix
                stripped = word[: -len(suffix)]
                # If there's a known radical mapping, apply that:
                if stripped in RAD_MAP:
                    stripped = RAD_MAP[stripped]
                # Check if the stripped form is in NUMBERS
                if stripped in self.NUMBERS:
                    return stripped

        return None

    def num_ord(self, digits: str, original_word: str) -> str:
        """
        Create an ordinal form from digit-based cardinal. 
        E.g., if digits='21' and the original word was 'eenentwintigste',
        we might return '21ste'. Minimally, we can just default to '…e'. 
        You can also detect whether to use 'de' or 'ste'.
        """
        # Very rough approach:
        # - “1” → “1e” or “1ste”
        # - “2” → “2e” or “2de”
        # - etc.
        # If you want to mimic actual Dutch rules, you can examine the original word:
        if original_word.endswith("ste"):
            return f"{digits}ste"
        elif original_word.endswith("de"):
            return f"{digits}de"
        # fallback
        return f"{digits}e"

    def normalize(self, word: str) -> str:
        """
        Hook to normalize or rewrite words before parsing.
        For instance, you can lowercase them or remove diacritics here.
        """
        return word.lower()
