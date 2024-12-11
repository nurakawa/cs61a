import unittest
from hw01.hw01 import a_plus_abs_b, two_of_three, largest_factor, hailstone


class TestAplusB(unittest.TestCase):

    def test_value(self):
        self.assertEqual(a_plus_abs_b(2, 3), 5, 'Should be 5.')
        self.assertEqual(a_plus_abs_b(2, -3), 5, 'Should be 5.')
        self.assertEqual(a_plus_abs_b(-1, 4), 3, 'Should be 3.')
        self.assertEqual(a_plus_abs_b(-1, -4), 3, 'Should be 5.')

class TestTwoOfThree(unittest.TestCase):

    def test_value(self):
        self.assertEqual(two_of_three(1, 2, 3), 5, 'Should be 5.')
        self.assertEqual(two_of_three(5, 3, 1), 10, 'Should be 10.')
        self.assertEqual(two_of_three(10, 2, 8), 68, 'Should be 68.')
        self.assertEqual(two_of_three(5, 5, 5), 50, 'Should be 50.')

class TestLargestFactor(unittest.TestCase):

    def test_value(self):
        self.assertEqual(largest_factor(15), 5, 'Should be 5.')
        self.assertEqual(largest_factor(80), 40, 'Should be 40.')
        self.assertEqual(largest_factor(13), 1, 'Should be 1.')

class TestHailstone(unittest.TestCase):

    def test_value(self):
        self.assertEqual(hailstone(10), 7, 'Should be 7.')
        self.assertEqual(hailstone(1), 1, 'Should be 1.')
        self.assertEqual(hailstone(27), 112, 'Should be 112.')
        
        

if __name__ == '__main__':
    unittest.main()
