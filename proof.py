import sys
import random
from abc import abstractmethod
from pprint import pprint
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional, Iterator
from assignment import Assignment
from formula import Formula
from literal import Literal
from clause import Clause
from assignments import Assignments


class Proof:
    @abstractmethod
    def __init__(self):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Subclasses must implement this method")

class UnsatProof(Proof):
    pure_literals: List[Literal]
    learnt_clauses: List[Clause]

    # init does not create deep copies, does not really matter for our purpose
    def __init__(self, pure_literals, learnt_clauses):
        self.pure_literals = pure_literals
        self.learnt_clauses = learnt_clauses

    def __str__(self):
        return ("pseudo-Boolean proof version 2.0\n" +
                "* The formula is unsatisfiable, the following is a pseudo-Boolean proof:\n" +
                "".join(list(map(lambda c: c.to_rup()+"\n", self.learnt_clauses))) +
                "rup >= 1" +
                "\noutput NONE\nconclusion UNSAT\nend pseudo-Boolean proof")

class SatProof(Proof):
    assignments: Assignments

    # init does not create deep copies, does not really matter for our purpose
    def __init__(self,assignments):
        self.assignments = assignments

    def __str__(self):
        return ("pseudo-Boolean proof version 2.0\n" +
                "* The formula is satisfiable, a possible assignment is\n" +
                self.assignments.to_sol() +
                "\noutput NONE\nconclusion SAT\nend pseudo-Boolean proof")