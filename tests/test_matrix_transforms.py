import unittest
import numpy as np
import pytrace.matrix_transforms as transforms
from pytrace.tuple import Point, Vector

PI = np.pi

class MatrixTransformsTestCase(unittest.TestCase):
    def test_translation_on_point(self):
        transform = transforms.translation(5, -3, 2)
        p = Point(-3, 4, 5)
        self.assertTrue(p @ transform == Point(2, 1, 7))

    def test_inversing_translation(self):
        transform = transforms.translation(5, -3, 2)
        inv = np.linalg.inv(transform)
        p = Point(-3, 4, 5)
        self.assertTrue(p @ inv == Point(-8, 7, 3))

    def test_translation_on_vector(self):
        transform = transforms.translation(5, -3, 2)
        v = Vector(-3, 4, 5)
        self.assertTrue(v @ transform == v)

    def test_scaling_on_point(self):
        transform = transforms.scaling(2, 3, 4)
        p = Point(-4, 6, 8)
        self.assertTrue(p @ transform == Point(-8, 18, 32))

    def test_scaling_on_vector(self):
        transform = transforms.scaling(2, 3, 4)
        v = Vector(-4, 6, 8)
        self.assertTrue(v @ transform == Vector(-8, 18, 32))

    def test_inversing_scaling(self):
        transform = transforms.scaling(2, 3, 4)
        inv = np.linalg.inv(transform)
        v = Vector(-4, 6, 8)
        self.assertTrue(v @ inv == Vector(-2, 2, 2))

    def test_reflection_by_scaling(self):
        transform = transforms.scaling(-1, 1, 1)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(-2, 3, 4))

    def test_rotate_x(self):
        p = Point(0, 1, 0)
        half_quarter = transforms.rotation_x(PI / 4)
        full_quarter = transforms.rotation_x(PI / 2)

        half_quarter_rotation = p @ half_quarter
        expected_half_quarter = Point(0, np.sqrt(2)/2, np.sqrt(2)/2)
        self.assertAlmostEqual(half_quarter_rotation.x, expected_half_quarter.x)
        self.assertAlmostEqual(half_quarter_rotation.y, expected_half_quarter.y)
        self.assertAlmostEqual(half_quarter_rotation.z, expected_half_quarter.z)

        full_quarter_rotation = p @ full_quarter
        expected_full_quarter = Point(0, 0, 1)
        self.assertAlmostEqual(full_quarter_rotation.x, expected_full_quarter.x)
        self.assertAlmostEqual(full_quarter_rotation.y, expected_full_quarter.y)
        self.assertAlmostEqual(full_quarter_rotation.z, expected_full_quarter.z)

    def test_inverse_rotate_x(self):
        p = Point(0, 1, 0)
        half_quarter = transforms.rotation_x(PI / 4)
        inv = np.linalg.inv(half_quarter)

        half_quarter_rotation = p @ inv
        expected_half_quarter = Point(0, np.sqrt(2)/2, -np.sqrt(2)/2)
        self.assertAlmostEqual(half_quarter_rotation.x, expected_half_quarter.x)
        self.assertAlmostEqual(half_quarter_rotation.y, expected_half_quarter.y)
        self.assertAlmostEqual(half_quarter_rotation.z, expected_half_quarter.z)

    def test_rotate_y(self):
        p = Point(0, 0, 1)
        half_quarter = transforms.rotation_y(PI / 4)
        full_quarter = transforms.rotation_y(PI / 2)

        half_quarter_rotation = p @ half_quarter
        expected_half_quarter = Point(np.sqrt(2)/2, 0, np.sqrt(2)/2)
        self.assertAlmostEqual(half_quarter_rotation.x, expected_half_quarter.x)
        self.assertAlmostEqual(half_quarter_rotation.y, expected_half_quarter.y)
        self.assertAlmostEqual(half_quarter_rotation.z, expected_half_quarter.z)

        full_quarter_rotation = p @ full_quarter
        expected_full_quarter = Point(1, 0, 0)
        self.assertAlmostEqual(full_quarter_rotation.x, expected_full_quarter.x)
        self.assertAlmostEqual(full_quarter_rotation.y, expected_full_quarter.y)
        self.assertAlmostEqual(full_quarter_rotation.z, expected_full_quarter.z)

    def test_rotate_z(self):
        p = Point(0, 1, 0)
        half_quarter = transforms.rotation_z(PI / 4)
        full_quarter = transforms.rotation_z(PI / 2)

        half_quarter_rotation = p @ half_quarter
        expected_half_quarter = Point(-np.sqrt(2)/2, np.sqrt(2)/2, 0)
        self.assertAlmostEqual(half_quarter_rotation.x, expected_half_quarter.x)
        self.assertAlmostEqual(half_quarter_rotation.y, expected_half_quarter.y)
        self.assertAlmostEqual(half_quarter_rotation.z, expected_half_quarter.z)

        full_quarter_rotation = p @ full_quarter
        expected_full_quarter = Point(-1, 0, 0)
        self.assertAlmostEqual(full_quarter_rotation.x, expected_full_quarter.x)
        self.assertAlmostEqual(full_quarter_rotation.y, expected_full_quarter.y)
        self.assertAlmostEqual(full_quarter_rotation.z, expected_full_quarter.z)

    def test_shear_x_to_y(self):
        transform = transforms.shearing(1, 0, 0, 0, 0, 0)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(5, 3, 4))

    def test_shear_x_to_z(self):
        transform = transforms.shearing(0, 1, 0, 0, 0, 0)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(6, 3, 4))

    def test_shear_y_to_x(self):
        transform = transforms.shearing(0, 0, 1, 0, 0, 0)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(2, 5, 4))

    def test_shear_y_to_z(self):
        transform = transforms.shearing(0, 0, 0, 1, 0, 0)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(2, 7, 4))

    def test_shear_z_to_x(self):
        transform = transforms.shearing(0, 0, 0, 0, 1, 0)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(2, 3, 6))

    def test_shear_z_to_y(self):
        transform = transforms.shearing(0, 0, 0, 0, 0, 1)
        p = Point(2, 3, 4)
        self.assertTrue(p @ transform == Point(2, 3, 7))
