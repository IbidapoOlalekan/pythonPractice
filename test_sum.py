import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")

    def lower_case(self):
        s = 'HELLO'
        self.assertEqual(s.lower(), 'hello', "Should be in lower case")


if __name__ == '__main__':
    unittest.main()
