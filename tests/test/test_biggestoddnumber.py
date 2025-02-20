from unittest import TestCase
from biggestoddnumber import biggest_odd_number,equal_strings

class TestBigOdd(TestCase):
    def test_biggest_odd_function_exists(self):
        self.assertEqual(biggest_odd_number("23956"),9)

    def test_same_character(self):
        self.assertEqual(equal_strings('love','evol'),True)
        self.assertEqual(equal_strings('love','evolu'),False)
