import sys
import random
from pprint import pprint
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional, Iterator
from assignment import Assignment
from formula import Formula
from literal import Literal
from clause import Clause


class Assignments(dict):
    """
    The assignments, also stores the current decision level.
    """
    def __init__(self):
        super().__init__()

        # the decision level
        self.dl = 0

    def value(self, literal: Literal) -> bool:
        """
        Return the value of the literal with respect the current assignments.
        """
        if literal.negation:
            return not self[literal.variable].value
        else:
            return self[literal.variable].value

    def assign(self, variable: int, value: bool, antecedent: Optional[Clause]):
        self[variable] = Assignment(value, antecedent, self.dl)

    def unassign(self, variable: int):
        self.pop(variable)

    def satisfy(self, formula: Formula) -> bool:
        """
        Check whether the assignments actually satisfies the formula.
        """
        for clause in formula:
            if True not in [self.value(lit) for lit in clause]:
                return False

        return True

    def to_sol(self):
        literals = [Literal(k,not self[k].value) for k in self.keys()]
        strings = []
        res = "sol"
        for k in self.keys():
            if self[k].value:
                res = res + " x" + str(k)
            else:
                res = res + " ~x" + str(k)
        return res