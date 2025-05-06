import sys
import random
from pprint import pprint
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional, Iterator
from clause import Clause



@dataclass
class Assignment:
    value: bool
    antecedent: Optional[Clause]
    dl: int  # decision level