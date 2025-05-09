import sys
import random
from pprint import pprint
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional, Iterator
from literal import Literal
from clause import Clause


@dataclass
class Formula:
    clauses: List[Clause]
    __variables: Set[int]

    def __init__(self, clauses: List[Clause]):
        """
        Remove duplicate literals in clauses.
        """
        self.clauses = []
        self.__variables = set()
        for clause in clauses:
            self.clauses.append(Clause(list(set(clause))))
            for lit in clause:
                var = lit.variable
                self.__variables.add(var)

    def variables(self) -> Set[int]:
        """
        Return the set of variables contained in this formula.
        """
        return self.__variables

    def __repr__(self):
        return ' ∧ '.join(f'({clause})' for clause in self.clauses)

    def __iter__(self) -> Iterator[Clause]:
        return iter(self.clauses)

    def __len__(self):
        return len(self.clauses)

    def to_opb(self):
        return "".join([c.to_opb()+"\n" for c in self.clauses])