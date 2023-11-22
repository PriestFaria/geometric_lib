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

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = area(10,10)
        self.assertEqual(res, 100)
      
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