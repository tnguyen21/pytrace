import unittest
import pytrace.matrix_transforms as transforms
from pytrace.tuple import Point, Vector
from pytrace.ray import Ray, Intersection, Intersections, Computations
from pytrace.objects import Sphere

class RayTestCase(unittest.TestCase):
    def test_ray_construction(self):
        origin = Point(1, 2, 3)
        direction = Vector(4, 5, 6)

        r = Ray(origin, direction)
        self.assertTrue(r.origin == origin)
        self.assertTrue(r.direction == direction)

    def test_compute_point_from_ray(self):
        r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
        self.assertTrue(r.position(0) == Point(2, 3, 4))
        self.assertTrue(r.position(1) == Point(3, 3, 4))
        self.assertTrue(r.position(-1) == Point(1, 3, 4))
        self.assertTrue(r.position(2.5) == Point(4.5, 3, 4))

    def test_ray_intersection_two_points(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 2)
        self.assertTrue(xs[0].t == 4.0)
        self.assertTrue(xs[1].t == 6.0)

    def test_ray_intersection_tangent(self):
        r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 2)
        self.assertTrue(xs[0].t == 5.0)
        self.assertTrue(xs[1].t == 5.0)

    def test_ray_misses_object(self):
        r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 0)

    def test_ray_starts_inside_object(self):
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 2)
        self.assertTrue(xs[0].t == -1.0)
        self.assertTrue(xs[1].t == 1.0)

    def test_object_behind_ray(self):
        r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 2)
        self.assertTrue(xs[0].t == -6.0)
        self.assertTrue(xs[1].t == -4.0)

    def test_intersect_also_sets_object(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 2)
        self.assertTrue(xs[0].obj == s)
        self.assertTrue(xs[1].obj == s)


    def test_aggregating_intersections(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i1, i2)
        self.assertTrue(len(xs.xs) == 2)
        self.assertTrue(xs.xs[0].t == 1)
        self.assertTrue(xs.xs[1].t == 2)

    # === tests to identify hits from intersections ===
    def test_hits_from_positive_t(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections(i2, i1)
        i = xs.hit()
        self.assertTrue(i == i1)

    def test_hits_some_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections(i2, i1)
        i = xs.hit()
        self.assertTrue(i == i2)

    def test_hits_all_negative_t(self):
        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = Intersections(i2, i1)
        i = xs.hit()
        self.assertTrue(i == None)

    def test_hit_is_lowest_nonnegative_int(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections(i1, i2, i3, i4)
        i = xs.hit()
        self.assertTrue(i == i4)

    # === test ray transformations ===
    def test_translating_ray(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = transforms.translation(3, 4, 5)
        r2 = r.transform(m)
        self.assertTrue(r2.origin == Point(4, 6, 8))
        self.assertTrue(r2.direction == Vector(0, 1, 0))

    def test_scaling_ray(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        m = transforms.scaling(2, 3, 4)
        r2 = r.transform(m)
        self.assertTrue(r2.origin == Point(2, 6, 12))
        self.assertTrue(r2.direction == Vector(0, 3, 0))

    def test_intersecting_scaled_sphere(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.set_transform(transforms.scaling(2, 2, 2))
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 2)
        self.assertTrue(xs[0].t == 3)
        self.assertTrue(xs[1].t == 7)

    def test_intersecting_translated_sphere(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.set_transform(transforms.translation(5, 0, 0))
        xs = r.intersect(s)
        self.assertTrue(len(xs) == 0)

    def test_prepare_computations(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        i = Intersection(4, s)
        comps = Computations.prepare_computations(i, r)
        self.assertTrue(comps.t == i.t)
        self.assertTrue(comps.obj == i.obj)
        self.assertTrue(comps.point == Point(0, 0, -1))
        self.assertTrue(comps.eye_vector == Vector(0, 0, -1))
        self.assertTrue(comps.normal_vector == Vector(0, 0, -1))