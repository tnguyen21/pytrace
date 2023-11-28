# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# #hack to get imports working in package
# #pylint: disable=wrong-import-position
# #pylint: disable=import-error
# from tuple import Point

from .tuple import Point
from .material import Material
import numpy as np

class SceneObject:
    def __init__(self, position: Point = Point(0, 0, 0), material: Material = Material()):
        self.position = position
        self.transform = np.eye(4)
        self.material = material

    def set_transform(self, m: np.array):
        """ m: 4x4 array representing transform """
        self.transform = m

    def normal_at(self, world_point: Point):
        raise NotImplementedError("Please implement this method")

class Sphere(SceneObject):
    def __init__(self, position: Point = Point(0, 0, 0), radius: float = 1):
        super().__init__(position)
        self.radius = radius

    def normal_at(self, world_point: Point):
        object_point = world_point @ np.linalg.inv(self.transform)
        object_normal = object_point - Point(0, 0, 0)
        world_normal = object_normal @ np.linalg.inv(self.transform).transpose()

        # this is a hack since technically to calculate this normal we need
        # to inverse and transpose a 3x3 submatrix of our transformation
        # to hack w being changed by the 4x4 matmuls, set it to 0 here
        world_normal.w = 0

        return world_normal.normalize()
