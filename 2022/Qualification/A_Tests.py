import unittest
from A_SecondHands import Solution

class TestSolveFunction(unittest.TestCase):
    
    def setUp(self):
        # This method will run before each test case.
        self.func = lambda n, k, parts: Solution.solve(n, k, parts)
    
    def test_case1(self):
        # Test where 2*k < n
        n, k = 10, 4
        parts = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
        self.assertFalse(self.func(n, k, parts))
    
    def test_case2(self):
        # Test where 2*k >= n and no part appears more than twice
        n, k = 10, 5
        parts = [1, 2, 1, 2, 3, 4, 3, 4, 5, 5]
        self.assertTrue(self.func(n, k, parts))
    
    def test_case3(self):
        # Test where a part appears more than twice
        n, k = 10, 5
        parts = [1, 2, 1, 2, 3, 4, 3, 4, 5, 1]
        self.assertFalse(self.func(n, k, parts))
    
    def test_case4(self):
        # Test where each part appears exactly once
        n, k = 10, 7
        parts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(self.func(n, k, parts))
    

    def test_case6(self):
        # Test where all parts are the same
        n, k = 2, 1
        parts = [1, 1]
        self.assertTrue(self.func(n, k, parts))

    def test_case7(self):
        # Test minimum edge case
        n, k = 1, 1
        parts = [1]
        self.assertTrue(self.func(n, k, parts))
    
    def test_case8(self):
        # Test part appears exactly twice
        n, k = 4, 2
        parts = [1, 2, 1, 2]
        self.assertTrue(self.func(n, k, parts))


if __name__ == '__main__':
    unittest.main()