import unittest
from math_module import math #import math.py

class TestMathModule(unittest.TestCase):

    def test_constants(self):
        self.assertEqual(math.pi, 3.141592653589793)
        self.assertEqual(math.e, 2.718281828459045)
        self.assertTrue(math.isinf(math.inf))
        self.assertTrue(math.isnan(math.nan))
        self.assertEqual(math.tau, 6.283185307179586)

    def test_ceil(self):
        self.assertEqual(math.ceil(4.2), 5)
        self.assertEqual(math.ceil(4.7), 5)

    def test_floor(self):
        self.assertEqual(math.floor(4.2), 4)
        self.assertEqual(math.floor(4.7), 4)

    def test_factorial(self):
        self.assertEqual(math.factorial(5), 120)
        self.assertRaises(ValueError, math.factorial, -5)

    def test_exp(self):
        self.assertEqual(math.exp(1), 2.718281828459045)
        self.assertEqual(math.exp(0), 1)

    def test_log(self):
        self.assertEqual(math.log(1), 0)
        self.assertEqual(math.log(10, 10), 1)
        self.assertRaises(ValueError, math.log, -1)

    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4)
        self.assertRaises(ValueError, math.sqrt, -16)

    def test_pow(self):
        self.assertEqual(math.pow(2, 3), 8)
        self.assertEqual(math.pow(3, 2), 9)

    def test_sin(self):
        self.assertEqual(math.sin(math.radians(90)), 1)

    def test_cos(self):
        self.assertEqual(math.cos(math.radians(0)), 1)

    def test_tan(self):
        # Utilisation de assertAlmostEqual avec une tolérance
        self.assertAlmostEqual(math.tan(math.radians(45)), 1, places=7)

    def test_radians(self):
        self.assertEqual(math.radians(180), 3.141592653589793)

    def test_degrees(self):
        self.assertEqual(math.degrees(math.pi), 180)

    def test_asin(self):
        self.assertEqual(math.asin(1), math.pi / 2)

    def test_acos(self):
        self.assertEqual(math.acos(1), 0)

    def test_atan(self):
        self.assertEqual(math.atan(1), math.pi / 4)

    def test_gcd(self):
        self.assertEqual(math.gcd(8, 12), 4)
        self.assertEqual(math.gcd(7, 13), 1)

    def test_comb(self):
        self.assertEqual(math.comb(5, 3), 10)
        # math.comb(3, 5) devrait retourner 0, pas lever une exception
        self.assertEqual(math.comb(3, 5), 0)

    def test_perm(self):
        self.assertEqual(math.perm(5, 3), 60)
        # math.perm(3, 5) devrait retourner 0, pas lever une exception
        self.assertEqual(math.perm(3, 5), 0)

if __name__ == "__main__":
    unittest.main()
