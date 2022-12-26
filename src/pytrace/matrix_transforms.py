# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# #hack to get imports working in package
# #pylint: disable=wrong-import-position
# #pylint: disable=import-error
# from tuple import Tuple, Point, Vector

from .tuple import Tuple, Point, Vector
import numpy as np

def translation(x: float, y: float, z: float) -> np.array:
    translation_vector = np.array([x, y, z, 1])
    translation_matrix = np.eye(4)
    translation_matrix[:, -1] = translation_vector
    return translation_matrix

def scaling(x: float, y: float, z: float) -> np.array:
    return np.eye(4)

def rotation_x(rad: float) -> np.array:
    return np.eye(4)

def rotation_y(rad: float) -> np.array:
    return np.eye(4)

def rotation_z(rad: float) -> np.array:
    return np.eye(4)

def shearing(
    x_to_y: float,
    x_to_z: float,
    y_to_x: float,
    y_to_z: float,
    z_to_x: float,
    z_to_y: float
) -> np.array:
    return np.eye(4)
