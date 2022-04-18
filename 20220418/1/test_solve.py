import unittest
import solve 

class TestSolver(unittest.TestCase):

    def test_pos_desc(self):
        self.assertEqual(solve.solveSquare(2, 3, -2), (-2, 0.5))

    def test_zero_desc(self):
        self.assertEqual(solve.solveSquare(1, 4, 4), (-2, -2))

    def test_neg_desc(self):
        self.assertEqual(solve.solveSquare(1, 1, 1), None)
