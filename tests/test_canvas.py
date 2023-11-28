import unittest
from pytrace.canvas import Canvas
from pytrace.tuple import Color

class CanvasTestCase(unittest.TestCase):
    def test_canvas_construction(self):
        c = Canvas(10, 20)
        expected_pixels = [[Color(0, 0, 0) for _ in range(10)] for _ in range(20)]

        self.assertTrue(c.width == 10)
        self.assertTrue(c.height == 20)
        self.assertListEqual(c.pixels, expected_pixels)

    def test_write_pixel(self):
        c = Canvas(10, 20)
        red = Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertTrue(c.pixels[3][2] == red)

    def test_canvas_to_ppm(self):
        c = Canvas(5, 3)
        c1 = Color(1.5, 0 , 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        output_ppm = c.to_ppm()

        expected_ppm = """P3
5 3
255
255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
"""
        self.assertEqual(output_ppm, expected_ppm)

    def test_long_lines_in_ppm(self):
        c = Canvas(10, 2)
        for y, row in enumerate(c.pixels):
            for x, _ in enumerate(row):
                c.pixels[y][x] = Color(1, 0.8, 0.6)
        output_ppm = c.to_ppm()
        expected_ppm = """P3
10 2
255
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
153 255 204 153 255 204 153 255 204 153 255 204 153
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
153 255 204 153 255 204 153 255 204 153 255 204 153
"""
        self.assertEqual(output_ppm, expected_ppm)


    def test_ppm_ends_with_newline(self):
        c = Canvas(5, 3)
        output_ppm = c.to_ppm()
        self.assertTrue(output_ppm[-1] == "\n")
