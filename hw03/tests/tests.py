import unittest
from hw03 import (
    num_eights,
    digit_distance,
    interleaved_sum,
    next_larger_coin,
    next_smaller_coin,
    count_coins,
    move_stack,
    make_anonymous_factorial,
)

class TestFunctions(unittest.TestCase):
    def test_num_eights(self):
        self.assertEqual(num_eights(3), 0)
        self.assertEqual(num_eights(8), 1)
        self.assertEqual(num_eights(88888888), 8)
        self.assertEqual(num_eights(2638), 1)
        self.assertEqual(num_eights(86380), 2)
        self.assertEqual(num_eights(12345), 0)
        self.assertEqual(num_eights(8782089), 3)

    def test_digit_distance(self):
        self.assertEqual(digit_distance(3), 0)
        self.assertEqual(digit_distance(777), 0)
        self.assertEqual(digit_distance(314), 5)
        self.assertEqual(digit_distance(31415926535), 32)
        self.assertEqual(digit_distance(3464660003), 16)

    def test_interleaved_sum(self):
        identity = lambda x: x
        square = lambda x: x * x
        triple = lambda x: x * 3
        self.assertEqual(interleaved_sum(5, identity, square), 29)
        self.assertEqual(interleaved_sum(5, square, identity), 41)
        self.assertEqual(interleaved_sum(4, triple, square), 32)
        self.assertEqual(interleaved_sum(4, square, triple), 28)

    def test_next_larger_coin(self):
        self.assertEqual(next_larger_coin(1), 5)
        self.assertEqual(next_larger_coin(5), 10)
        self.assertEqual(next_larger_coin(10), 25)
        self.assertIsNone(next_larger_coin(2))

    def test_next_smaller_coin(self):
        self.assertEqual(next_smaller_coin(25), 10)
        self.assertEqual(next_smaller_coin(10), 5)
        self.assertEqual(next_smaller_coin(5), 1)
        self.assertIsNone(next_smaller_coin(2))

    def test_count_coins(self):
        self.assertEqual(count_coins(15), 6)
        self.assertEqual(count_coins(10), 4)
        self.assertEqual(count_coins(20), 9)
        self.assertEqual(count_coins(100), 242)
        self.assertEqual(count_coins(200), 1463)

    def test_move_stack(self):
        with self.assertLogs() as log:
            move_stack(1, 1, 3)
        self.assertIn("Move the top disk from rod 1 to rod 3", log.output[0])

        with self.assertLogs() as log:
            move_stack(2, 1, 3)
        self.assertIn("Move the top disk from rod 1 to rod 3", log.output)
        self.assertIn("Move the top disk from rod 2 to rod 3", log.output)

        with self.assertLogs() as log:
            move_stack(3, 1, 3)
        self.assertIn("Move the top disk from rod 1 to rod 3", log.output)
        self.assertIn("Move the top disk from rod 2 to rod 3", log.output)

    def test_make_anonymous_factorial(self):
        fact = make_anonymous_factorial()
        self.assertEqual(fact(5), 120)

if __name__ == "__main__":
    unittest.main()
