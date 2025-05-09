import unittest
import cdcl
from literal import Literal
from clause import Clause
from formula import Formula
from assignment import Assignment
from assignments import Assignments

class MyTestCase(unittest.TestCase):
    def test_eliminate_pure_literals(self):
        formula = cdcl.parse_dimacs_cnf("p cnf 3 2\n1 2 -3 0\n-1 -2 3 0")
        assignments = Assignments()
        cdcl.eliminate_pure_literals(formula, assignments)
        self.assertEqual(0,len(assignments))
        formula = cdcl.parse_dimacs_cnf("p cnf 6 3\n1 2 -3 -5 6 0\n-1 -2 3 -4 6 0\n1 2 -3 -4 5 0")
        cdcl.eliminate_pure_literals(formula, assignments)
        self.assertEqual(2,len(assignments))
        self.assertTrue(6 in assignments and 4 in assignments)
        self.assertTrue(assignments[6].value and not assignments[4].value)

if __name__ == '__main__':
    unittest.main()
