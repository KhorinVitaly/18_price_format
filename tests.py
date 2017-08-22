import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_format_float(self):
        self.assertEqual(format_price(25565.20), '25 565.2')

    def test_format_integer(self):
        self.assertEqual(format_price(25565), '25 565')

    def test_format_not_number(self):
        self.assertEqual(format_price('g34'), None)


if __name__ == '__main__':
    unittest.main()
