import unittest

def area(a, b):
    """Принимает значения a и b, возвращает значение площади прямоугольника с данными сторонами"""
    return a * b 

def perimeter(a, b):
    """Принимает значения a и b, возвращает значение периметра прямоугольника с данными сторонами"""
    return (a + b)*2 

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = area(10,10)
        self.assertEqual(res, 100)
