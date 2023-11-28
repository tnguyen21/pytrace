import unittest
import pytrace.tuple
import pytrace.world

class WorldTestCase(unittest.TestCase):
    def test_init_world(self):
        w = pytrace.world.World()
        self.assertListEqual(w.objects, [])
        self.assertIsNone(w.light_source)
