import sys
import random
from pprint import pprint
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional, Iterator


# frozen to be hashable
@dataclass(frozen=True)
class Literal:
    variable: int
    negation: bool

    def __repr__(self):
        if self.negation:
            return '¬' + str(self.variable)
        else:
            return str(self.variable)

    def neg(self) -> 'Literal':
        """
        Return the negation of this literal.
        """
        return Literal(self.variable, not self.negation)

    def to_opb_string(self):
        if self.negation:
            return '1 ~x' + str(self.variable)
        else:
            return '1 x' + str(self.variable)