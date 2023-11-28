# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# #hack to get imports working in package
# #pylint: disable=wrong-import-position
# #pylint: disable=import-error
# from tuple import Tuple, Point, Vector

from .tuple import Color

class Material:
    def __init__(
        self,
        color: Color = Color(1, 1, 1),
        ambient: float = 0.1,
        diffuse: float = 0.9,
        specular: float = 0.9,
        shininess: float = 200.0
    ):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __eq__(self, other):
        return (
            self.color == other.color and
            self.ambient == other.ambient and
            self.diffuse == other.diffuse and
            self.specular == other.specular and
            self.shininess == other.shininess
        )
