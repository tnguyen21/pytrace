import unittest
from pytrace.tuple import Color, Point
from pytrace.world import World
from pytrace.matrix_transforms import scaling
import numpy as np

class WorldTestCase(unittest.TestCase):
    def test_init_world(self):
        w = World()
        self.assertListEqual(w.objects, [])
        self.assertIsNone(w.light_source)

    def test_default_world(self):
        w = World()
        w._init_default_world()
        self.assertEqual(len(w.objects), 2)
        self.assertEqual(w.objects[0].material.color, Color(0.8, 1.0, 0.6))
        self.assertEqual(w.objects[0].material.diffuse, 0.7)
        self.assertEqual(w.objects[0].material.specular, 0.2)
        self.assertTrue(np.all(w.objects[1].transform == scaling(0.5, 0.5, 0.5)))
        self.assertEqual(w.light_source.position, Point(-10, 10, -10))
        self.assertEqual(w.light_source.intensity, Color(1, 1, 1))
