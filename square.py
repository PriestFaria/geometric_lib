import unittest
def area(a):
    """Принимает значение a, возвращает значение площади квадрата со стороной a"""
    return a * a


def perimeter(a):
    """Принимает значение a, возвращает значение периметра квадрата со стороной a"""
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_nul_mul(self):
        res1 = area(0)
        res2 = perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)

    def test_mul(self):
        res1 = area(10)
        res2 = perimeter(10)
        self.assertEqual(res1, 100)
        self.assertEqual(res2, 40)
