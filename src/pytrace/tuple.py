import numpy as np
from math import floor

class Tuple:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z) and (self.w == other.w)

    def __add__(self, other):
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar: float):
        # TODO look into defining mult and div between scalars and tuple
        # atm, Tuple * scalar works, scalar * Tuple is undefined -- inconvenient
        if not isinstance(scalar, (float, int)):
            raise TypeError
        return Tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def __truediv__(self, scalar: float):
        if not isinstance(scalar, (float, int)):
            raise TypeError
        return Tuple(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __str__(self):
        return f"Tuple<x={self.x}, y={self.y}, z={self.z}, w={self.w}>"

    def magnitude(self):
        return np.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w))

    def normalize(self):
        mag = self.magnitude()
        return Tuple(self.x / mag, self.y / mag, self.z / mag, self.w / mag)

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z) + (self.w * other.w)


class Point(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0)

class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 0.0)

    def cross(self, other):
        """ only def for vector, no notion of cross product for point """
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        return Vector(new_x, new_y, new_z)

class Color(Tuple):
    def __init__(self, r: float, g: float, b: float):
        super().__init__(r, g, b, 0.0)

    def __mul__(self, other):
        """ notion of blending colors, only works between two colors """
        if isinstance(other, Color):
            new_r = self.x * other.x
            new_g = self.y * other.y
            new_b = self.z * other.z
        elif isinstance(other, (float, int)):
            return super().__mul__(other)
        else:
            raise TypeError

        return Color(new_r, new_g, new_b)

    def scale_255(self):
        if self.x >= 1.0:
            scaled_r = 255
        elif self.x <= 0.0:
            scaled_r = 0
        else:
            scaled_r = floor(self.x * 256)

        if self.y >= 1.0:
            scaled_g = 255
        elif self.y <= 0.0:
            scaled_g = 0
        else:
            scaled_g = floor(self.y * 256)

        if self.z >= 1.0:
            scaled_b = 255
        elif self.z <= 0.0:
            scaled_b = 0
        else:
            scaled_b = floor(self.z * 256)

        return (scaled_r, scaled_g, scaled_b)
