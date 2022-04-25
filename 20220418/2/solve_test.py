import unittest
from unittest.mock import MagicMock
from solve import solve, SquareIO

class SquareEquationTestCase(unittest.TestCase):
    def setUp(self):
        def inputCoeff(c):
            return self.coeffs[c]
        def printResult(x):
            self.x = x
        SquareIO.inputCoeff = MagicMock(side_effect=inputCoeff)
        SquareIO.printResult = MagicMock(side_effect=printResult) 
    
    def lin_test(self):
        self.coeffs = {'a': '0', 'b': '10', 'c': '-5'}
        solve()
        self.assertEqual(self.x, 2)
    
    def sq_test(self):
        self.coeffs = {'a': '4', 'b': '3', 'c': '-1'}
        solve()
        self.assertEqual(self.x, (-1, 0.25))

    def degen_test(self):
        self.coeffs = {'a': '0', 'b': '0', 'c': '1'}
        solve()
        self.assertIsNone(self.x)

if __name__ == "__main__":
    unittest.main()
