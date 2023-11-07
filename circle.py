import math
import unittest


def area(r):
    """Принимает число r, возвращает значение площади круга с радиусом r"""
    return math.pi * r * r


def perimeter(r):
    """Принимает число r, возвращает значение длины окружности радиусом r"""
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0)
        res2 = perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    def test_mul(self):
        res1 = area(10)
        res2 = perimeter(10)
        self.assertEqual(res1, 314.1592653589793)
        self.assertEqual(res2, 62.83185307179586)
