import unittest
from pytrace.material import Material
from pytrace.objects import Sphere

class MaterialTestCase(unittest.TestCase):
    def test_objects_have_default_material(self):
        s = Sphere()
        self.assertEqual(s.material, Material())
    
    def test_assign_material_to_object(self):
        s = Sphere()
        m = Material()
        m.ambient = 1
        s.material = m
        self.assertEqual(s.material, m)
