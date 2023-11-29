# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# #hack to get imports working in package
# #pylint: disable=wrong-import-position
# #pylint: disable=import-error
# from tuple import Point, Vector
# from objects import SceneObject

from .tuple import Point, Vector
from .objects import SceneObject
import numpy as np

class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> Point:
        return self.origin + self.direction * t

    def intersect(self, obj: SceneObject) -> list[float]:
        """ returns collection of t values where ray intersects object """
        r2 = self.transform(np.linalg.inv(obj.transform))
        object_to_ray = r2.origin - obj.position # vector
        a = r2.direction.dot(r2.direction)
        b = 2 * r2.direction.dot(object_to_ray)
        c = object_to_ray.dot(object_to_ray) - 1
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return []
        t1 = (-b - np.sqrt(discriminant)) / (2 * a)
        t2 = (-b + np.sqrt(discriminant)) / (2 * a)
        i1 = Intersection(t1, obj)
        i2 = Intersection(t2, obj)
        return [i1, i2]

    def transform(self, m: np.array):
        new_origin = self.origin @ m
        new_direction = self.direction @ m
        return Ray(new_origin, new_direction)

class Intersection:
    def __init__(self, t: float, obj: SceneObject):
        self.t = t
        self.obj = obj

    def __eq__(self, other):
        return (self.t == other.t) and (self.obj == other.obj)

class Intersections:
    def __init__(self, *intersections: Intersection):
        self.xs = list(intersections)

    def hit(self) -> Intersection:
        """ return lowest nonegative intersection from collection """
        nonnegative_xs = filter(lambda x: x.t > 0, self.xs)
        sorted_xs = sorted(nonnegative_xs, key=lambda x: x.t)
        if len(sorted_xs) == 0:
            return None
        return sorted_xs[0]
    
class Computations:
    def __init__(self):
        self.t = None
        self.obj = None
        self.point = None
        self.eye_vector = None
        self.normal_vector = None
        self.inside = None
        self.over_point = None
        self.under_point = None
        self.reflect_vector = None

    @staticmethod
    def prepare_computations(i: Intersection, r: Ray):
        comps = Computations()
        comps.t = i.t
        comps.obj = i.obj
        comps.point = r.position(comps.t)
        comps.eye_vector = -r.direction
        comps.normal_vector = comps.obj.normal_at(comps.point)
        # if comps.normal_vector.dot(comps.eye_vector) < 0:
        #     comps.inside = True
        #     comps.normal_vector = -comps.normal_vector
        # else:
        #     comps.inside = False
        # comps.over_point = comps.point + comps.normal_vector * 0.0001
        # comps.under_point = comps.point - comps.normal_vector * 0.0001
        # comps.reflect_vector = r.direction.reflect(comps.normal_vector)
        return comps