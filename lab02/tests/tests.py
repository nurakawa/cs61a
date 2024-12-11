import unittest
from lab02 import composer, composite_identity, sum_digits, is_prime, count_cond, multiple, cycle

class TestFunctions(unittest.TestCase):
    def test_composer(self):
        add_one = lambda x: x + 1
        square = lambda x: x**2
        mul_three = lambda x: x * 3

        a1 = composer(square, add_one)
        self.assertEqual(a1(4), 25)

        a2 = composer(mul_three, a1)
        self.assertEqual(a2(4), 75)
        self.assertEqual(a2(5), 108)

    def test_composite_identity(self):
        add_one = lambda x: x + 1
        square = lambda x: x**2

        b1 = composite_identity(square, add_one)
        self.assertTrue(b1(0))  # (0 + 1) ** 2 == 0 ** 2 + 1
        self.assertFalse(b1(4)) # (4 + 1) ** 2 != 4 ** 2 + 1

    def test_count_cond(self):
        count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
        self.assertEqual(count_fives(10), 1)  # 50 (10 * 5)
        self.assertEqual(count_fives(50), 4)  # 50, 500, 1400, 2300

        is_i_prime = lambda n, i: is_prime(i)
        count_primes = count_cond(is_i_prime)
        self.assertEqual(count_primes(2), 1)  # 2
        self.assertEqual(count_primes(3), 2)  # 2, 3
        self.assertEqual(count_primes(4), 2)  # 2, 3
        self.assertEqual(count_primes(5), 3)  # 2, 3, 5
        self.assertEqual(count_primes(20), 8)  # 2, 3, 5, 7, 11, 13, 17, 19

    def test_multiple(self):
        self.assertEqual(multiple(3, 4), 12)
        self.assertEqual(multiple(14, 21), 42)

    def test_cycle(self):
        def add1(x):
            return x + 1

        def times2(x):
            return x * 2

        def add3(x):
            return x + 3

        my_cycle = cycle(add1, times2, add3)

        identity = my_cycle(0)
        self.assertEqual(identity(5), 5)

        add_one_then_double = my_cycle(2)
        self.assertEqual(add_one_then_double(1), 4)

        do_all_functions = my_cycle(3)
        self.assertEqual(do_all_functions(2), 9)

        do_more_than_a_cycle = my_cycle(4)
        self.assertEqual(do_more_than_a_cycle(2), 10)

        do_two_cycles = my_cycle(6)
        self.assertEqual(do_two_cycles(1), 19)

if __name__ == "__main__":
    unittest.main()
