import unittest
def area(a, h):
    """Принимает значения a и h, возвращает площадь треугольника с высотой h и основанием a"""
    return a * h / 2 

def perimeter(a, b, c):
    """Принимает значения a, b и c, возвращает периметр треугольника с данными сторонами"""
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(100, 0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        res = perimeter(10,15,20)
        self.assertEqual(res, 45)
