import unittest
from lab01 import falling, divisible_by_k, sum_digits, double_eights


class TestFalling(unittest.TestCase):

    def test_value(self):
        self.assertEqual(falling(6, 3), 120, "Should be 120")
        self.assertEqual(falling(4, 3), 24, "Should be 24")
        self.assertEqual(falling(4, 1), 4, "Should be 4")
        self.assertEqual(falling(4, 0), 1, "Should be 1")


class TestDivbyk(unittest.TestCase):

    def test_value(self):
        self.assertEqual(divisible_by_k(10, 2), 5, 'Should be 5.')
        self.assertEqual(divisible_by_k(3, 1), 3, 'Should be 3.')
        self.assertEqual(divisible_by_k(6, 7), 0, 'Should be 0.')

class TestSumDigits(unittest.TestCase):

    def test_value(self):
        self.assertEqual(sum_digits(10), 1, 'Should be 1.')
        self.assertEqual(sum_digits(100), 1, 'Should be 1.')
        self.assertEqual(sum_digits(1234567890), 45, 'Should be 45.')
        self.assertEqual(sum_digits(0), 0, 'Should be 0.')


class TestDoubleEights(unittest.TestCase):
    def test_single_eight(self):
        self.assertFalse(double_eights(8))  # Single 8 should return False

    def test_two_eights(self):
        self.assertTrue(double_eights(88))  # Double 8 should return True

    def test_eights_with_other_digits(self):
        self.assertTrue(double_eights(2882))  # Double 8 in the middle should return True
        self.assertTrue(double_eights(880088))  # Multiple double 8s should return True
        self.assertFalse(double_eights(80808080))  # No consecutive 8s should return False

    def test_no_eights(self):
        self.assertFalse(double_eights(12345))  # No 8s should return False

    def test_large_number(self):
        self.assertTrue(double_eights(123888456))  # Double 8 in a large number should return True

    def test_leading_eights(self):
        self.assertTrue(double_eights(8812345))  # Double 8 at the start should return True


if __name__ == '__main__':
    unittest.main()

