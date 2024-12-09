import unittest

def fib_list(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


class TestFibLib(unittest.TestCase):
    """Test the fib_lib function"""

    def test_0(self):
        """It should evaluate 0 to []"""
        self.assertEqual(fib_list(0), [])

    def test_1(self):
        """It should evaluate 1 to [0]"""
        self.assertEqual(fib_list(1), [0])

    def test_2(self):
        """It should evaluate 2 to [0, 1]"""
        self.assertEqual(fib_list(2), [0, 1])

    def test_3(self):
        """It should evaluate 3 to [0, 1, 1]"""
        self.assertEqual(fib_list(3), [0, 1, 1])

    def test_4(self):
        """It should evaluate 4 to [0, 1, 1, 2]"""
        self.assertEqual(fib_list(4), [0, 1, 1, 2])

    def test_5(self):
        """It should evaluate 5 to [0, 1, 1, 2, 3]"""
        self.assertEqual(fib_list(5), [0, 1, 1, 2, 3])

    def test_9(self):
        """It should evaluate 9 to [0, 1, 1, 2, 3, 5, 8, 13, 21]"""
        self.assertEqual(fib_list(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])


if __name__ == "__main__":
    unittest.main()
