import unittest
import numpy as np
from src.pytrace.tuple import Tuple, Point, Vector, Color

class TupleTestCase(unittest.TestCase):
    """
    TODO
    """

    def test_tuple_constructor(self):
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(a.x, 4.3)
        self.assertEqual(a.y, -4.2)
        self.assertEqual(a.z, 3.1)
        self.assertEqual(a.w, 1.0)

    def test_point_constructor(self):
        a = Point(4, -4, 3)
        b = Tuple(4, -4, 3, 1)
        self.assertEqual(a, b)

    def test_vector_constructor(self):
        a = Vector(4, -4, 3)
        b = Tuple(4, -4, 3, 0)
        self.assertEqual(a, b)

    def test_add_tuples(self):
        a = Tuple(3, -2, 5, 1)
        b = Tuple(-2, 3, 1, 0)
        self.assertTrue(a + b == Tuple(1, 1, 6, 1))

    def test_subtract_two_points(self):
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        self.assertTrue(p1 - p2 == Vector(-2, -4, -6))

    def test_subtract_vector_from_point(self):
        p = Point(3, 2, 1)
        v = Vector(5, 6, 7)
        self.assertTrue(p - v == Point(-2, -4, -6))

    def test_subtract_two_vector(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        self.assertTrue(v1 - v2 == Vector(-2, -4, -6))

    def test_negate_tuple(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue(-a == Tuple(-1, 2, -3, 4))

    def test_multiply_tuple_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue(a * 3.5 == Tuple(3.5, -7, 10.5, -14))

    def test_multiply_tuple_by_fraction(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue(a * 0.5 == Tuple(0.5, -1, 1.5, -2))

    def test_multiply_tuple_by_matrix(self):
        eye = np.eye(4)
        a = Tuple(1, 2, 3, 4)
        self.assertTrue(a @ eye == a)

    def test_dividing_tuple_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        self.assertTrue(a / 2 == Tuple(0.5, -1, 1.5, -2))

    def test_magnitude_x_only(self):
        v = Vector(1, 0, 0)
        self.assertTrue(v.magnitude() == 1)

    def test_magnitude_y_only(self):
        v = Vector(0, 1, 0)
        self.assertTrue(v.magnitude() == 1)

    def test_magnitude_z_only(self):
        v = Vector(0, 0, 1)
        self.assertTrue(v.magnitude() == 1)

    def test_magnitude_positive_vector(self):
        v = Vector(1, 2, 3)
        self.assertTrue(v.magnitude() == np.sqrt(14))

    def test_magnitude_negative_vector(self):
        v = Vector(-1, -2, -3)
        self.assertTrue(v.magnitude() == np.sqrt(14))

    def test_single_direction_normalization(self):
        v = Vector(4, 0, 0)
        self.assertTrue(v.normalize() == Vector(1, 0, 0))

    def test_normalize_vector(self):
        v = Vector(1, 2, 3)
        root14 = np.sqrt(14)
        self.assertTrue(v.normalize() == Vector(1 / root14, 2 / root14, 3 / root14))

    def test_magnitude_of_normalized_vector(self):
        v = Vector(1, 2, 3)
        self.assertTrue(v.normalize().magnitude() == 1)

    def test_dot_product_vectors(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertTrue(a.dot(b) == 20)

    def test_cross_product_vectors(self):
        a = Vector(1, 2, 3)
        b = Vector(2, 3, 4)
        self.assertTrue(a.cross(b) == Vector(-1, 2, -1))
        self.assertTrue(b.cross(a) == Vector(1, -2, 1))

class ColorTestCase(unittest.TestCase):
    """
    TODO
    """

    def test_color_construction(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertEqual(c.x, -0.5)
        self.assertEqual(c.y, 0.4)
        self.assertEqual(c.z, 1.7)
        self.assertEqual(c.w, 0.0) # * colors like vectors

    def test_add_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertTrue(c1 + c2 == Color(1.6, 0.7, 1.0))

    def test_sub_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        c3 = c1 - c2
        expected_color = Color(0.2, 0.5, 0.5)

        # almost equals because of floating point round off errors
        self.assertAlmostEqual(c3.x, expected_color.x)
        self.assertAlmostEqual(c3.y, expected_color.y)
        self.assertAlmostEqual(c3.z, expected_color.z)

    def test_scalar_mult_color(self):
        c = Color(0.2, 0.3, 0.4)
        self.assertTrue(c * 2 ==  Color(0.4, 0.6, 0.8))

    def test_color_mult_color(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        c3 = c1 * c2
        expected_color = Color(0.9, 0.2, 0.04)

        # almost equals because of floating point round off errors
        self.assertAlmostEqual(c3.x, expected_color.x)
        self.assertAlmostEqual(c3.y, expected_color.y)
        self.assertAlmostEqual(c3.z, expected_color.z)
