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

from typing import Dict, Optional, Set, Tuple, List

from .base import Language

#
# CONSTANTS for Italian
#

MULTIPLIERS = {
    "mila": 1000,
    "mille": 1000,
    "milioni": 1000000,
    "milione": 1000000,
    "miliardo": 1000000000,
    "miliardi": 1000000000,
}

UNITS: Dict[str, int] = {
    word: value
    for value, word in enumerate(
        "uno due tre quattro cinque sei sette otto nove".split(), 1
    )
}


STENS: Dict[str, int] = {
word: value
    for value, word in enumerate(
        "dieci undici dodici tredici quattordici quindici sedici diciassette diciotto diciannove"
        .split(),
        10,
        )
}

MTENS: Dict[str, int] = {
    word: value * 10
    for value, word in enumerate(
        "venti trenta quaranta cinquanta sessanta settanta ottanta novanta".split(), 2
    )
}

MTENS_WSTENS: Set[str] = set()

HUNDRED = {
    "cento": 100,
    "duecento": 200,
    "trecento": 300,
    "quattrocento": 400,
    "cinquecento": 500,
    "seicento": 600,
    "settecento": 700,
    "ottocento": 800,
    "novecento": 900,
}

COMPOSITES: Dict[str, int] = {}

NUMBERS = MULTIPLIERS.copy()
NUMBERS.update(UNITS)
NUMBERS.update(STENS)
NUMBERS.update(MTENS)
NUMBERS.update(HUNDRED)
NUMBERS.update(COMPOSITES)

class Italian(Language):

    MULTIPLIERS = MULTIPLIERS
    UNITS = UNITS
    STENS = STENS
    MTENS = MTENS
    MTENS_WSTENS = MTENS_WSTENS
    HUNDRED = HUNDRED
    NUMBERS = NUMBERS

    SIGN = {"più": "+", "meno": "-"}
    ZERO = {"zero"}
    DECIMAL_SEP = "virgola"
    DECIMAL_SYM = "."

    AND_NUMS = {
        "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"
    }
    AND = "e"
    NEVER_IF_ALONE = {"un", "uno", "una"}

    RELAXED: Dict[str, Tuple[str, str]] = {}

    # TODO
    def ord2card(self, word: str) -> Optional[str]:
        """Convert ordinal number to cardinal.
        Return None if word is not an ordinal or is better left in letters
        as is the case for first and second.
        """
        # This will require specific implementation based on Italian ordinal rules.
        return None

    def num_ord(self, digits: str, original_word: str) -> str:
        """Add suffix to number in digits to make an ordinal"""
        # This will require specific rules for Italian ordinal suffixes.
        return f"{digits}º" if original_word.endswith("o") else f"{digits}ª"

    def normalize(self, word: str) -> str:
        return word.lower()
    



class iWtoN:
    UNIT = {
        'zero': 0,
        'uno': 1,
        'due': 2,
        'tre': 3,
        'tré': 3,
        'quattro': 4,
        'cinque': 5,
        'sei': 6,
        'sette': 7,
        'otto': 8,
        'nove': 9,
        'dieci': 10,
        'undici': 11,
        'dodici': 12,
        'tredici': 13,
        'quattordici': 14,
        'quindici': 15,
        'sedici': 16,
        'diciassette': 17,
        'diciotto': 18,
        'diciannove': 19,
        'venti': 20,
        'vent': 20,
        'trenta': 30,
        'trent': 30,
        'quaranta': 40,
        'quarant': 40,
        'cinquanta': 50,
        'sessant': 60,
        'sessanta': 60,
        'settanta': 70,
        'settant': 70,
        'ottanta': 80,
        'ottant': 80,
        'novanta': 90,
        'novant': 90,
    }

    TEN = {
        'venti': 20,
        'vent': 20,
        'trenta': 30,
        'trent': 30,
        'quaranta': 40,
        'quarant': 40,
        'cinquanta': 50,
        'cinquanta': 50,
        'sessanta': 60,
        'sessant': 60,
        'settanta': 70,
        'settant': 70,
        'ottanta': 80,
        'ottant': 80,
        'novanta': 90,
        'novant': 90
    }

    JOINER = 'e'
    NEGATIVE = 'meno'
    TEN_KEYS = ['venti', 'vent', 'trenta', 'trent', 'quaranta', 'quarant', 'cinquanta', 'cinquant', 'sessanta', 'sessant', 'settanta', 'settant', 'ottanta', 'ottant', 'novanta', 'novant']
    MAGNITUDE = {
        'cento': 100,
        'mille': 1000,
        'milione': 1000000
    }

    @staticmethod
    def convert(words: str) -> int:
        if not words:
            raise ValueError('Initial string must not be empty or undefined')

        if words.startswith(iWtoN.NEGATIVE):
            return -iWtoN.compute(iWtoN.tokenize(words[len(iWtoN.NEGATIVE):]))
        else:
            return iWtoN.compute(iWtoN.tokenize(words))

    @staticmethod
    def tokenize(words: str) -> List[object]:
        array = words.split(' ')
        result: List[object] = []

        for string in array:
            if string.isdigit():
                result.append(int(string))
            elif string != iWtoN.JOINER:
                result.append(string)

        return result if result else [array]

    @staticmethod
    def compute(tokens: List[object]) -> int:
        obj = {
            'sum': 0
        }

        leftover = ''

        for token in tokens:
            obj['str'] = token

            if isinstance(token, int):
                obj['sum'] += token
            else:
                obj = iWtoN.getMillion(obj['str'], obj['sum'])
                leftover += obj['str']

        if leftover:
            raise ValueError('Failed to completely convert string to number')

        return obj['sum']

    @staticmethod
    def getMillion(string: str, sum: int) -> Dict[str, int]:
        if 'milione' in string:
            sum *= iWtoN.MAGNITUDE['milione']
            string = string.replace('milione', '')
        elif 'milioni' in string:
            sum *= iWtoN.MAGNITUDE['milione']
            string = string.replace('milioni', '')

        if string:
            return iWtoN.getThousands(string, sum)
        else:
            return {'str': string, 'sum': sum}

    @staticmethod
    def getThousands(string: str, sum: int) -> Dict[str, int]:
        if 'mille' in string:
            sum += iWtoN.MAGNITUDE['mille']
            string = string.replace('mille', '')
        elif 'mila' in string:
            sum += iWtoN.getHundreds(string[:string.index('mila')], 0)['sum'] * iWtoN.MAGNITUDE['mille']
            string = string[string.index('mila') + 4:]

        if string:
            return iWtoN.getHundreds(string, sum)
        else:
            return {'str': string, 'sum': sum}

    @staticmethod
    def getHundreds(string: str, sum: int) -> Dict[str, int | str]:
        if 'cento' in string:
            sum += (1 if string.index('cento') == 0 else iWtoN.getUnit(string[:string.index('cento')], 0)['sum']) * iWtoN.MAGNITUDE['cento']
            string = string[string.index('cento') + 5:]

        if string:
            return iWtoN.getTens(string, sum)
        else:
            return {'str': string, 'sum': sum}

    @staticmethod
    def getTens(string: str, sum: int) -> Dict[str, int | str]:
        found = False
        for key in iWtoN.TEN_KEYS:
            if key in string:
                sum += iWtoN.TEN[key]
                string = string.replace(key, '')
                found = True
                break

        if string:
            return iWtoN.getUnit(string, sum)
        else:
            return {'str': string, 'sum': sum}

    @staticmethod
    def getUnit(string: str, sum: int) -> Dict[str, int | str]:
        if string in iWtoN.UNIT:
            sum += iWtoN.UNIT[string]
            string = string.replace(string, '')
        else:
            sum += 0

        return {'str': string, 'sum': sum}



