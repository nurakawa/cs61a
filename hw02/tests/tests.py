import unittest
from operator import add, mul
from hw02 import square, identity, triple, increment, double, product, accumulate, summation_using_accumulate, funception, mul_by_num, add_results, mod_maker

class TestProductFunction(unittest.TestCase):  
    def test_identity(self):
        self.assertEqual(product(3, identity), 6)  # 1 * 2 * 3
        self.assertEqual(product(5, identity), 120)  # 1 * 2 * 3 * 4 * 5

    def test_square(self):
        self.assertEqual(product(3, square), 36)  # 1^2 * 2^2 * 3^2
        self.assertEqual(product(5, square), 14400)  # 1^2 * 2^2 * 3^2 * 4^2 * 5^2

    def test_increment(self):
        self.assertEqual(product(3, increment), 24)  # (1+1) * (2+1) * (3+1)

    def test_triple(self):
        self.assertEqual(product(3, triple), 162)  # 1*3 * 2*3 * 3*3

    def test_edge_case(self):
        self.assertEqual(product(1, identity), 1)  # Single term product
        self.assertEqual(product(1, square), 1)  # Single term square

class TestAccumulateFunction(unittest.TestCase):
    def test_add_with_identity(self):
        # Basic summation with identity
        self.assertEqual(accumulate(add, 0, 5, identity), 15)  # 0 + 1 + 2 + 3 + 4 + 5
        self.assertEqual(accumulate(add, 11, 5, identity), 26)  # 11 + 1 + 2 + 3 + 4 + 5
        self.assertEqual(accumulate(add, 11, 0, identity), 11)  # Base case: no terms

    def test_add_with_square(self):
        # Summation with square terms
        self.assertEqual(accumulate(add, 11, 3, square), 25)  # 11 + 1^2 + 2^2 + 3^2

    def test_multiply_with_square(self):
        # Multiplication with square terms
        self.assertEqual(accumulate(mul, 2, 3, square), 72)  # 2 * 1^2 * 2^2 * 3^2

    def test_custom_merger(self):
        # Custom merger function tests
        self.assertEqual(accumulate(lambda x, y: x + y + 1, 2, 3, square), 19)
        self.assertEqual(accumulate(lambda x, y: 2 * x * y, 2, 3, square), 576)

    def test_modulo_merger(self):
        # Modulo-based custom merger
        self.assertEqual(accumulate(lambda x, y: (x + y) % 17, 19, 20, square), 16)

    def test_edge_cases(self):
        # Edge cases: n = 1 or n = 0
        self.assertEqual(accumulate(add, 0, 0, identity), 0)  # No terms to add
        self.assertEqual(accumulate(mul, 1, 1, square), 1)  # 1^2

    def test_large_input(self):
        # Large inputs
        self.assertEqual(accumulate(add, 0, 100, identity), 5050)  # Sum of 1 to 100
        self.assertEqual(accumulate(mul, 1, 10, identity), 3628800)  # 1 * 2 * ... * 10


class TestSummationUsingAccumulate(unittest.TestCase):

    def test_value(self):
        self.assertEqual(summation_using_accumulate(5, square), 55)
        self.assertEqual(summation_using_accumulate(5, triple), 45)

class TestFunception(unittest.TestCase):    
    def test_increment_function(self):
        # Testing with increment function
        g1 = funception(increment, 0)
        self.assertEqual(g1(3), 6)  # increment(0) * increment(1) * increment(2) = 1 * 2 * 3 = 6
        self.assertEqual(g1(0), 1)  # begin >= end, return 1
        self.assertEqual(g1(-1), 1)  # begin >= end, return 1
        
        g3 = funception(increment, -3)
        self.assertEqual(g3(-1), 2)  # increment(-3) * increment(-2) = -2 * -1 = 2

    def test_double_function(self):
        # Testing with double function
        g2 = funception(double, 1)
        self.assertEqual(g2(3), 8)  # double(1) * double(2) = 2 * 4 = 8
        self.assertEqual(g2(4), 48)  # double(1) * double(2) * double(3) = 2 * 4 * 6 = 48
        self.assertEqual(g2(1), 1)  # begin >= end, return 1

    def test_edge_cases(self):
        # Edge cases
        g = funception(increment, 0)
        self.assertEqual(g(0), 1)  # begin == end
        self.assertEqual(g(-5), 1)  # begin > end

        g = funception(double, 5)
        self.assertEqual(g(5), 1)  # begin == end
        self.assertEqual(g(4), 1)  # begin > end

    def test_large_range(self):
        # Testing large ranges
        g = funception(increment, 1)
        self.assertEqual(g(10), 3628800)  # factorial of 9 (increment(1) to increment(9))

class TestMulByNum(unittest.TestCase):
    def test_mul_by_num(self):
        # Test cases derived from the docstring
        x = mul_by_num(5)
        y = mul_by_num(2)
        self.assertEqual(x(3), 15)  # 5 * 3 = 15
        self.assertEqual(y(-4), -8)  # 2 * -4 = -8

    def test_zero_multiplier(self):
        # Test case with zero multiplier
        zero = mul_by_num(0)
        self.assertEqual(zero(10), 0)  # 0 * 10 = 0
        self.assertEqual(zero(-10), 0)  # 0 * -10 = 0

    def test_negative_multiplier(self):
        # Test case with negative multiplier
        neg = mul_by_num(-3)
        self.assertEqual(neg(4), -12)  # -3 * 4 = -12
        self.assertEqual(neg(-2), 6)  # -3 * -2 = 6

    def test_identity_multiplier(self):
        # Test case with multiplier of 1
        identity = mul_by_num(1)
        self.assertEqual(identity(7), 7)  # 1 * 7 = 7
        self.assertEqual(identity(-5), -5)  # 1 * -5 = -5


class TestAddResults(unittest.TestCase):
    def test_docstring_cases(self):
        # Define test functions
        identity = lambda x: x
        square = lambda x: x**2
        
        # Case 1: Basic composition
        a1 = add_results(identity, square)  # x + x^2
        self.assertEqual(a1(4), 20)  # 4 + 4^2 = 20
        
        # Case 2: Nested composition
        a2 = add_results(a1, identity)  # (x + x^2) + x
        self.assertEqual(a2(4), 24)  # 4 + 4^2 + 4 = 24
        self.assertEqual(a2(5), 35)  # 5 + 5^2 + 5 = 35
        
        # Case 3: More nested composition
        a3 = add_results(a1, a2)  # (x + x^2) + (x + x^2 + x)
        self.assertEqual(a3(4), 44)  # (4 + 4^2) + (4 + 4^2 + 4) = 44

    def test_zero_input(self):
        # Test with input 0
        identity = lambda x: x
        square = lambda x: x**2
        
        a1 = add_results(identity, square)  # x + x^2
        self.assertEqual(a1(0), 0)  # 0 + 0^2 = 0
        
        a2 = add_results(a1, identity)  # (x + x^2) + x
        self.assertEqual(a2(0), 0)  # 0 + 0^2 + 0 = 0
        
        a3 = add_results(a1, a2)  # (x + x^2) + (x + x^2 + x)
        self.assertEqual(a3(0), 0)  # 0 + 0 + 0 = 0


class TestModMaker(unittest.TestCase):
    def test_docstring_cases(self):
        # Instantiate the mod_maker function
        mod = mod_maker()
        
        # Test cases from the docstring
        self.assertEqual(mod(7, 2), 1)  # 7 % 2 = 1
        self.assertEqual(mod(4, 8), 4)  # 4 % 8 = 4
        self.assertEqual(mod(8, 4), True)  # 8 % 4 = 0, divisible => True

    def test_zero_division(self):
        # Ensure no division by zero
        mod = mod_maker()
        with self.assertRaises(ZeroDivisionError):
            mod(5, 0)


if __name__ == "__main__":
    unittest.main()