# MIT License

# Copyright (c) 2018-2019 Groupe Allo-Media

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Language support.
"""

from .base import Language  # noqa: F401
from .dutch import Dutch
from .french import French
from .english import English
from .spanish import Spanish
from .portuguese import Portuguese
from .german import German
from .catalan import Catalan
from .russian import Russian
from .italian import Italian
from .norwegian import Norwegian

LANG = {
    "fr": French(),
    "en": English(),
    "es": Spanish(),
    "pt": Portuguese(),
    "de": German(),
    "ca": Catalan(),
    "ru": Russian(),
    "it": Italian(),
    "nl": Dutch(),
    "no": Norwegian(),
}
