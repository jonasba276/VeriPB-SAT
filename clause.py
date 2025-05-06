import sys
import random
from pprint import pprint
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional, Iterator
from literal import Literal


@dataclass
class Clause:
    literals: List[Literal]

    def __repr__(self):
        return '∨'.join(map(str, self.literals))

    def __iter__(self) -> Iterator[Literal]:
        return iter(self.literals)

    def __len__(self):
        return len(self.literals)
