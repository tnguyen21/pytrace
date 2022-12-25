import unittest
import src.pytrace.tuple # example relative import

class TemplateTestCase(unittest.TestCase):
    def test_simple_assertion(self):
        a = True
        self.assertTrue(a)

    def test_equality(self):
        a = 1
        b = 1
        self.assertEqual(a, b)
