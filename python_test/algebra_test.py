import unittest

from python_test.algebra import addition, subtraction, division, mutiplication, to_lower_case, to_upper_case, \
    to_sentence_case, to_camel_case


class AlgebraTestCase(unittest.TestCase):

    def test_add(self):
        result = addition(5, 10)
        self.assertEqual(result, 15)

    def test_minus(self):
        result = subtraction(5, 10)
        self.assertEqual(result, 5)

    def test_division(self):
        result = division(12, 6)
        self.assertEqual(result, 2)

    def test_mutiplication(self):
        result = mutiplication(2, 3)
        self.assertEqual(result, 6)

    def test_to_lower_case(self):
        user_input = "BUDDY"
        result = to_lower_case(user_input)
        self.assertEqual(result, "buddy")

    def test_to_upper_case(self):
        user_input = 'buddy'
        result = to_upper_case(user_input)
        self.assertEqual(result, 'BUDDY')

    def test_to_sentence_test(self):
        user_input = 'buddy'
        result = to_sentence_case(user_input)
        self.assertEqual(result, 'Buddy')

    def test_to_change_a_sentence_case_test(self):
        user_input = 'a man from ghana'
        result = to_sentence_case(user_input)
        self.assertEqual(result, 'A Man From Ghana')

    def test_to_camel_case_test(self):
        user_input = 'buddy come visit me'
        result = to_camel_case(user_input)
        self.assertEqual(result,"bUDDYcOMEvISITmE")

