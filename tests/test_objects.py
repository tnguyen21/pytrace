import unittest
import numpy as np
import src.pytrace.matrix_transforms as transforms
from src.pytrace.objects import Sphere

class ObjectsTestCase(unittest.TestCase):
    def test_default_obj_transformation(self):
        s = Sphere()
        self.assertTrue((s.transform == np.eye(4)).all())

    def test_set_obj_transformation(self):
        s = Sphere()
        t = transforms.translation(2, 3, 4)
        s.set_transform(t)
        self.assertTrue((s.transform == t).all())
