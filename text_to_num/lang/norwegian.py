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
# Built once on import.
#

# 0
# Add "o" so the parser can recognize "o" as zero (some tests use it).
ZERO = {"null", "o"}

# Units (1–9). Note that Norwegian has "en" and "ett" both meaning 1 in different contexts.
UNITS: Dict[str, int] = {
    "en": 1,
    "ett": 1,
    "to": 2,
    "tre": 3,
    "fire": 4,
    "fem": 5,
    "seks": 6,
    "sju": 7,     # or "syv"
    "åtte": 8,
    "ni": 9,
}

# Single tens (10–19)
STENS: Dict[str, int] = {
    "ti": 10,
    "elleve": 11,
    "tolv": 12,
    "tretten": 13,
    "fjorten": 14,
    "femten": 15,
    "seksten": 16,
    "sytten": 17,
    "atten": 18,
    "nitten": 19,
}

# Multiples of ten (20, 30, 40, 50, 60, 70, 80, 90)
MTENS: Dict[str, int] = {
    "tjue": 20,
    "tretti": 30,
    "førti": 40,
    "femti": 50,
    "seksti": 60,
    "sytti": 70,
    "åtti": 80,
    "nitti": 90,
}

# Ten multiples that can combine with STENS in some languages; empty for Norwegian
MTENS_WSTENS: Set[str] = set()

# "hundre" (100). Indefinite plural can be "hundre" or "hundrer"
HUNDRED = {
    "hundre": 100,
    "hundrer": 100,
}

# Larger multipliers
MULTIPLIERS: Dict[str, int] = {
    "tusen": 1000,
    "tusener": 1000,
    "million": 1_000_000,
    "millioner": 1_000_000,
    "milliard": 1_000_000_000,
    "milliarder": 1_000_000_000,
    "billion": 1_000_000_000_000,
    "billioner": 1_000_000_000_000,
}

# Build composite forms for 21–99 in a single word: e.g., "tjueen" => 21, "tjueto" => 22, ...
# If you prefer a hyphen, you can do f"{ten_word}-{unit_word}". We do single-word here.
COMPOSITES: Dict[str, int] = {
    (ten_word + unit_word): ten_val + unit_val
    for ten_word, ten_val in MTENS.items()
    for unit_word, unit_val in UNITS.items()
}

# Combine everything into NUMBERS
NUMBERS: Dict[str, int] = {}
NUMBERS.update({"null": 0, "o": 0})  # from ZERO
NUMBERS.update(UNITS)
NUMBERS.update(STENS)
NUMBERS.update(MTENS)
NUMBERS.update(HUNDRED)
NUMBERS.update(MULTIPLIERS)
NUMBERS.update(COMPOSITES)

# Sign words
SIGN: Dict[str, str] = {
    "pluss": "+",
    "minus": "-",
}

# Decimal separator in Norwegian is typically "komma" in writing, but 
# the library wants final output with a dot => we set DECIMAL_SYM = "."
DECIMAL_SEP = "komma"
DECIMAL_SYM = "."

# “og” is often used, but not mandatory
AND = "og"
AND_NUMS: Set[str] = set()

# Words that you NEVER want to turn into a digit if they appear "alone"
# The English tests do a context-based approach for “one.” 
# We add "en" here so the parser can skip numeric conversion in article contexts 
# but can still parse it if it combines with another numeric token or word.
NEVER_IF_ALONE: Set[str] = {"en", "ett"}

# Relaxed composed numbers (two-words only); not commonly used in Norwegian,
# so we leave it empty:
RELAXED: Dict[str, Tuple[str, str]] = {}

# Ordinal -> Cardinal map: covers 1–19, tens, and 100. 
ORDINAL_MAP: Dict[str, str] = {
    "første": "en",
    "andre": "to",
    "tredje": "tre",
    "fjerde": "fire",
    "femte": "fem",
    "sjette": "seks",
    "sjuende": "sju",
    "syvende": "sju",  # alternative
    "åttende": "åtte",
    "niende": "ni",
    "tiende": "ti",
    "ellevte": "elleve",
    "tolvte": "tolv",
    "trettende": "tretten",
    "fjortende": "fjorten",
    "femtende": "femten",
    "sekstende": "seksten",
    "syttende": "sytten",
    "attende": "atten",
    "nittende": "nitten",
    "tjuende": "tjue",
    "trettiende": "tretti",
    "førtiende": "førti",
    "femtiende": "femti",
    "sekstiende": "seksti",
    "syttiende": "sytti",
    "åttiende": "åtti",
    "nittiende": "nitti",
    "hundrede": "hundre",
}


class Norwegian(Language):
    MULTIPLIERS = MULTIPLIERS
    UNITS = UNITS
    STENS = STENS
    MTENS = MTENS
    MTENS_WSTENS = MTENS_WSTENS
    HUNDRED = HUNDRED
    NUMBERS = NUMBERS

    SIGN = SIGN
    ZERO = ZERO
    DECIMAL_SEP = DECIMAL_SEP
    DECIMAL_SYM = DECIMAL_SYM

    AND = AND
    AND_NUMS = AND_NUMS
    NEVER_IF_ALONE = NEVER_IF_ALONE

    RELAXED = RELAXED

    def ord2card(self, word: str) -> Optional[str]:
        """
        Convert an ordinal word (e.g. 'første', 'andre') into its cardinal form ('en', 'to'), 
        returning None if it doesn't match or isn't found.
        """
        return ORDINAL_MAP.get(word, None)

    def num_ord(self, digits: str, original_word: str) -> str:
        """
        Create an ordinal form from numeric digits. Norwegian commonly 
        denotes ordinals by appending a dot, e.g. "1." = første, "2." = andre, etc.
        """
        return f"{digits}."

    def normalize(self, word: str) -> str:
        """
        Normalize a word if necessary (e.g., unify 'syv' -> 'sju').
        """
        if word.lower() == "syv":
            return "sju"
        return word

    def split_number_word(self, word: str) -> str:
        """
        In Norwegian, numbers like 'tjueen' (21) or 'tjuesju' (27) can appear as 
        a single word. If found, split it into separate tokens: e.g. 'tjue en'. 
        This is a minimal approach using the known dictionaries up to 99.

        Returns a single string with tokens separated by space if a match is found.
        If no compound match is found, returns the word unchanged.
        """
        # If the word is directly in NUMBERS, just return it
        if word in self.NUMBERS:
            return word

        # Try all composite forms up to two segments (e.g. 'tjue' + 'en')
        # that sum up to 99. If found, split them with a space.
        for ten_word in self.MTENS:
            if word.startswith(ten_word):
                remainder = word[len(ten_word):]
                if remainder in self.UNITS:
                    # e.g. "tjue" + "en" => "tjue en"
                    return f"{ten_word} {remainder}"

        # Also check single-tens range (STENS).
        for stens_word in self.STENS:
            if word.startswith(stens_word):
                remainder = word[len(stens_word):]
                if remainder in self.UNITS:
                    # e.g. "femten" + "en" => ...
                    return f"{stens_word} {remainder}"

        # If nothing matched, return unchanged
        return word
