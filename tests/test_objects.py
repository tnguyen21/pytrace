import unittest
import numpy as np
import src.pytrace.matrix_transforms as transforms
from src.pytrace.tuple import Point, Vector
from src.pytrace.objects import Sphere

class ObjectsTestCase(unittest.TestCase):
    def test_default_obj_transformation(self):
        s = Sphere()
        self.assertTrue((s.transform == np.eye(4)).all())

    def test_set_obj_transformation(self):
        s = Sphere()
        t = transforms.translation(2, 3, 4)
        s.set_transform(t)
        self.assertTrue((s.transform == t).all())

    # === test normal_at on spheres ===
    def test_normal_sphere_x_axis(self):
        s = Sphere()
        n = s.normal_at(Point(1, 0, 0))
        self.assertTrue(n == Vector(1, 0, 0))

    def test_normal_sphere_y_axis(self):
        s = Sphere()
        n = s.normal_at(Point(0, 1, 0))
        self.assertTrue(n == Vector(0, 1, 0))

    def test_normal_sphere_z_axis(self):
        s = Sphere()
        n = s.normal_at(Point(0, 0, 1))
        self.assertTrue(n == Vector(0, 0, 1))

    def test_normal_sphere_nonaxial_point(self):
        s = Sphere()
        n = s.normal_at(Point(np.sqrt(3)/3, np.sqrt(3)/3, np.sqrt(3)/3))
        self.assertTrue(n == Vector(np.sqrt(3)/3, np.sqrt(3)/3, np.sqrt(3)/3))

    def test_normal_is_normalized(self):
        s = Sphere()
        n = s.normal_at(Point(np.sqrt(3)/3, np.sqrt(3)/3, np.sqrt(3)/3))
        self.assertTrue(n == n.normalize())

    def test_normal_on_translated_sphere(self):
        s = Sphere()
        s.set_transform(transforms.translation(0, 1, 0))
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        expected_n = Vector(0, 0.70711, -0.70711)
        # * this is hacky, but good enough
        self.assertAlmostEqual(n.x, expected_n.x, places=5)
        self.assertAlmostEqual(n.y, expected_n.y, places=5)
        self.assertAlmostEqual(n.z, expected_n.z, places=5)
        self.assertAlmostEqual(n.w, expected_n.w, places=5)

    def test_normal_on_transformed_sphere(self):
        s = Sphere()
        m = transforms.scaling(1, 0.5, 1) @ transforms.rotation_z(np.pi / 5)
        s.set_transform(m)
        n = s.normal_at(Point(0, np.sqrt(2)/2, -np.sqrt(2)/2))
        expected_n = Vector(0, 0.97014, -0.24254)
        self.assertAlmostEqual(n.x, expected_n.x, places=5)
        self.assertAlmostEqual(n.y, expected_n.y, places=5)
        self.assertAlmostEqual(n.z, expected_n.z, places=5)
        self.assertAlmostEqual(n.w, expected_n.w, places=5)
