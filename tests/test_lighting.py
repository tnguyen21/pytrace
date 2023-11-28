import unittest
import numpy as np
from pytrace.lighting import PointLight, lighting
from pytrace.material import Material
from pytrace.tuple import Color, Point, Vector

class LightingTestCase(unittest.TestCase):
    def test_pointlight_construction(self):
        position = Point(0, 0, 0)
        intensity = Color(1, 1, 1)
        light = PointLight(position, intensity)
        self.assertEqual(light.position, position)
        self.assertEqual(light.intensity, intensity)
    
    def test_lighting_with_eye_between_light_and_surface(self):
        m = Material()
        position = Point(0, 0, 0)
        eye_vector = Vector(0, 0, -1)
        normal_vector = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eye_vector, normal_vector)
        self.assertEqual(result, Color(1.9, 1.9, 1.9))

    def test_lighting_with_eye_opposite_surface_light_offset_45deg(self):
        m = Material()
        position = Point(0, 0, 0)
        eye_vector = Vector(0, 0, -1)
        normal_vector = Vector(0, 0, -1)
        light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eye_vector, normal_vector)
        expected_result = Color(0.7364, 0.7364, 0.7364)
        self.assertAlmostEqual(result.x, expected_result.x, places=5)
        self.assertAlmostEqual(result.y, expected_result.y, places=5)
        self.assertAlmostEqual(result.z, expected_result.z, places=5)
    
    def test_lighting_with_eye_in_path_of_reflection_vector(self):
        m = Material()
        position = Point(0, 0, 0)
        eye_vector = Vector(0, -np.sqrt(2)/2, -np.sqrt(2)/2)
        normal_vector = Vector(0, 0, -1)
        light = PointLight(Point(0, 10, -10), Color(1, 1, 1))
        result = lighting(m, light, position, eye_vector, normal_vector)
        expected_result = Color(1.6364, 1.6364, 1.6364)
        self.assertAlmostEqual(result.x, expected_result.x, places=5)
        self.assertAlmostEqual(result.y, expected_result.y, places=5)
        self.assertAlmostEqual(result.z, expected_result.z, places=5)
    
    def test_lighting_with_light_behind_surface(self):
        m = Material()
        position = Point(0, 0, 0)
        eye_vector = Vector(0, 0, -1)
        normal_vector = Vector(0, 0, -1)
        light = PointLight(Point(0, 0, 10), Color(1, 1, 1))
        result = lighting(m, light, position, eye_vector, normal_vector)
        self.assertTrue(result, Color(0.1, 0.1, 0.1))
