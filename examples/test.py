import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

#hack to get relative imports working in script
#pylint: disable=wrong-import-position
#pylint: disable=import-error
from tuple import Color
from canvas import Canvas


# c = Canvas(5, 3)
# c1 = Color(1.5, 0 , 0)
# c2 = Color(0, 0.5, 0)
# c3 = Color(-0.5, 0, 1)
# c.write_pixel(0, 0, c1)
# c.write_pixel(2, 1, c2)
# c.write_pixel(4, 2, c3)
# print(c.to_ppm())
# expected_ppm = """P3
# 5 3
# 255
# 255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
# """
# print("---")

expected_ppm = """P3
5 3
255
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
153 255 204 153 255 204 153 255 204 153 255 204 153
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204
153 255 204 153 255 204 153 255 204 153 255 204 153
"""
print(expected_ppm)

c = Canvas(10, 2)
for y, row in enumerate(c.pixels):
    for x, _ in enumerate(row):
        c.pixels[y][x] = Color(1, 0.8, 0.6)
output_ppm = c.to_ppm()
print(output_ppm)