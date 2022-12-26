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
    v = np.array([x, y, z, 1])
    return np.diag(v)

def rotation_x(rad: float) -> np.array:
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad)],
                                [np.sin(rad), np.cos(rad)]])
    transform = np.eye(4)
    transform[1:3, 1:3] = rotation_matrix
    return transform

def rotation_y(rad: float) -> np.array:
    transform = np.eye(4)
    transform[0][0] = np.cos(rad)
    transform[2][0] = -np.sin(rad)
    transform[0][2] = np.sin(rad)
    transform[2][2] = np.cos(rad)
    return transform

def rotation_z(rad: float) -> np.array:
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad)],
                                [np.sin(rad), np.cos(rad)]])
    transform = np.eye(4)
    transform[0:2, 0:2] = rotation_matrix
    return transform

def shearing(
    x_to_y: float,
    x_to_z: float,
    y_to_x: float,
    y_to_z: float,
    z_to_x: float,
    z_to_y: float
) -> np.array:
    return np.eye(4)
