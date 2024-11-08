import unittest
from math_quiz import generate_random_integer, select_random_operator, create_math_problem

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if generate_random_integer generates a number within the specified range."""
        min_value = 1
        max_value = 10
        for _ in range(100):  # Run multiple times to check randomness
            result = generate_random_integer(min_value, max_value)
            self.assertGreaterEqual(result, min_value)  # Check if result >= min_value
            self.assertLessEqual(result, max_value)  # Check if result <= max_value

    def test_select_random_operator(self):
        """Test if select_random_operator returns one of the expected operators."""
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Run multiple times to check randomness
            operator = select_random_operator()
            self.assertIn(operator, valid_operators)  # Check if operator is in valid_operators

    def test_create_math_problem(self):
        """Test if create_math_problem returns the correct problem string and answer."""
        # Test addition
        problem, answer = create_math_problem(3, 5, '+')
        self.assertEqual(problem, "3 + 5")
        self.assertEqual(answer, 8)

        # Test subtraction
        problem, answer = create_math_problem(10, 4, '-')
        self.assertEqual(problem, "10 - 4")
        self.assertEqual(answer, 6)

        # Test multiplication
        problem, answer = create_math_problem(6, 7, '*')
        self.assertEqual(problem, "6 * 7")
        self.assertEqual(answer, 42)

# Run the tests
if __name__ == '__main__':
    unittest.main()
