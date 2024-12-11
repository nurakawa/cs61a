import unittest
from lab00 import twenty_twenty_three, time_to_twenty_twenty_three


class TestTwentyTwentyThree(unittest.TestCase):

    def test_value(self):
        self.assertEqual(twenty_twenty_three(), 2023, "Should be 2023")

    def test_output_type(self):
        self.assertIsInstance(twenty_twenty_three(), int, "Should output type <class 'int'>")

class TestTimeToTwentyTwentyThree(unittest.TestCase):
    
    def test_exception(self):
        self.assertRaises(Exception, time_to_twenty_twenty_three, -1)
        self.assertRaises(Exception, time_to_twenty_twenty_three, -3001)

    def test_positive_value(self):
        data = 2024
        result = time_to_twenty_twenty_three(2024)
        self.assertEqual(result, 1)

    def test_negative_value(self):
        data = 2022
        result = time_to_twenty_twenty_three(2024)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

