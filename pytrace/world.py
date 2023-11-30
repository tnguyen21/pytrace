import numpy as np

from .objects import Sphere
from .tuple import Color, Point
from .lighting import PointLight, lighting
from .matrix_transforms import scaling, translation
from .ray import Intersections, Computations

class World:
    def __init__(self):
        self.objects = []
        self.light_source = None
    
    def _init_default_world(self):
        s1 = Sphere()
        s1.material.color = Color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2
        self.objects.append(s1)
        s2 = Sphere()
        s2.transform = scaling(0.5, 0.5, 0.5)
        self.objects.append(s2)
        self.light_source = PointLight(Point(-10, 10, -10), Color(1, 1, 1))

    def intersect(self, ray):
        intersections = []
        for obj in self.objects:
            intersections.extend(ray.intersect(obj))
        intersections.sort(key=lambda x: x.t)
        return intersections

    def shade_hit(self, comps):
        return lighting(
            comps.obj.material,
            self.light_source,
            comps.point,
            comps.eye_vector,
            comps.normal_vector
        )

    def color_at(self, ray):
        intersections = self.intersect(ray)
        hit = Intersections(*intersections).hit()
        if hit is None:
            return Color(0, 0, 0)
        comps = Computations.prepare_computations(hit, ray)
        return self.shade_hit(comps)
