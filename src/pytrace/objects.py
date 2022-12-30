# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# #hack to get imports working in package
# #pylint: disable=wrong-import-position
# #pylint: disable=import-error
# from tuple import Point

from .tuple import Point
import numpy as np

class SceneObject:
    def __init__(self, position: Point = Point(0, 0, 0)):
        self.position = position
        self.transform = np.eye(4)

    def set_transform(self, m: np.array):
        """ m: 4x4 array representing transform """
        self.transform = m

class Sphere(SceneObject):
    def __init__(self, position: Point = Point(0, 0, 0), radius: float = 1):
        super().__init__(position)
        self.radius = radius
