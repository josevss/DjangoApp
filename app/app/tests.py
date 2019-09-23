from django.test import TestCase
from app.calc import add, substract


class calcTests(TestCase):
    def test_add_numbers(self):
        "test adding calculation"
        self.assertEqual(add(3, 4), 7)

    def test_subtractnumbers(self):
        "test that values are subs and return"
        self.assertEqual(substract(5, 11), -6)
