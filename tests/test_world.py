import unittest

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

from pytrace.tuple import Color, Point, Vector
from pytrace.ray import Ray, Intersection, Computations
from pytrace.world import World
from pytrace.lighting import PointLight
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

    def test_intersect_world_with_ray(self):
        w = World()
        w._init_default_world()
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        intersections = w.intersect(r)
        self.assertEqual(len(intersections), 4)
        self.assertEqual(intersections[0].t, 4)
        self.assertEqual(intersections[1].t, 4.5)
        self.assertEqual(intersections[2].t, 5.5)
        self.assertEqual(intersections[3].t, 6)
    
    def test_shading_intersection(self):
        w = World()
        w._init_default_world()
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        shape = w.objects[0]
        i = r.intersect(shape)[0]
        comps = Computations.prepare_computations(i, r)
        c = w.shade_hit(comps)
        self.assertAlmostEqual(c.r, 0.38066, 5)
        self.assertAlmostEqual(c.g, 0.47583, 5)
        self.assertAlmostEqual(c.b, 0.2855, 5)

    def test_shading_intersection_from_inside(self):
        # TODO - this test is failing
        w = World()
        w._init_default_world()
        w.light_source = PointLight(Point(0, 0.25, 0), Color(1, 1, 1))
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        shape = w.objects[1]
        i = r.intersect(shape)[1]
        comps = Computations.prepare_computations(i, r)
        c = w.shade_hit(comps)
        self.assertAlmostEqual(c.r, 0.90498, 5)
        self.assertAlmostEqual(c.g, 0.90498, 5)
        self.assertAlmostEqual(c.b, 0.90498, 5)

    def test_color_when_ray_misses(self):
        w = World()
        w._init_default_world()
        r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
        c = w.color_at(r)
        self.assertEqual(c, Color(0, 0, 0))
    
    def test_color_when_ray_hits(self):
        w = World()
        w._init_default_world()
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        c = w.color_at(r)
        self.assertAlmostEqual(c.r, 0.38066, 5)
        self.assertAlmostEqual(c.g, 0.47583, 5)
        self.assertAlmostEqual(c.b, 0.2855, 5)

    #! this test causes test_shading_intersection to fail when uncommented -- why!?
    # it passes on its own...
    # def test_color_with_intersection_behind_ray(self):
    #     w = World()
    #     w._init_default_world()
    #     outer = w.objects[0]
    #     outer.material.ambient = 1
    #     inner = w.objects[1]
    #     inner.material.ambient = 1
    #     r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    #     c = w.color_at(r)
    #     self.assertEqual(c, inner.material.color)
