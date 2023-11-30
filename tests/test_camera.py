import unittest
import pytrace.camera
from pytrace.tuple import Point, Vector
from pytrace.matrix_transforms import rotation_y, translation
import numpy as np

class CameraTestCase(unittest.TestCase):
    def test_init_camera(self):
        c = pytrace.camera.Camera(160, 120, np.pi / 2)
        self.assertEqual(c.hsize, 160)
        self.assertEqual(c.vsize, 120)
        self.assertAlmostEqual(c.fov, np.pi / 2)
        self.assertTrue(np.all(c.transform == np.eye(4)))

    def test_pixel_size_horizontal_canvas(self):
        c = pytrace.camera.Camera(200, 125, np.pi / 2)
        self.assertAlmostEqual(c.pixel_size, 0.01)
    
    def test_pixel_size_vertical_canvas(self):
        c = pytrace.camera.Camera(125, 200, np.pi / 2)
        self.assertAlmostEqual(c.pixel_size, 0.01)

    def test_ray_through_center_of_canvas(self):
        c = pytrace.camera.Camera(201, 101, np.pi / 2)
        r = c.ray_for_pixel(100, 50)
        self.assertTrue(r.origin == Point(0, 0, 0))
        self.assertTrue(r.direction == Vector(0, 0, -1))
    
    def test_ray_through_corner_of_canvas(self):
        c = pytrace.camera.Camera(201, 101, np.pi / 2)
        r = c.ray_for_pixel(0, 0)
        self.assertTrue(r.origin == Point(0, 0, 0))
        self.assertAlmostEqual(r.direction.x, 0.66519, 5)
        self.assertAlmostEqual(r.direction.y, 0.33259, 5)
        self.assertAlmostEqual(r.direction.z, -0.66851, 5)
    
    def test_ray_when_camera_transformed(self):
        c = pytrace.camera.Camera(201, 101, np.pi / 2)
        c.transform = rotation_y(np.pi / 4) @ translation(0, -2, 5)
        r = c.ray_for_pixel(100, 50)
        self.assertTrue(r.origin == Point(0, 2, -5))
        self.assertAlmostEqual(r.direction.x, np.sqrt(2) / 2)
        self.assertAlmostEqual(r.direction.y, 0)
        self.assertAlmostEqual(r.direction.z, -np.sqrt(2) / 2)