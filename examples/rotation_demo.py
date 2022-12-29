import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

#hack to get relative imports working in script
#pylint: disable=wrong-import-position
#pylint: disable=import-error
from tuple import Point, Vector, Color
from matrix_transforms import rotation_y, translation
from canvas import Canvas
import numpy as np

if __name__ == "__main__":
    c = Canvas(100, 100)
    center = 50
    radius = 40

    p = Point(0, 0, 1)
    for hour in range(12):
        transform = rotation_y(hour * (np.pi / 6))
        p_new = p @ transform
        print(radius * p_new.x + center, radius * p_new.z + center)
        c.write_pixel(int(radius * p_new.x + center), int(radius * p_new.z + center), Color(1, 1, 1))

    with open("clock_face.ppm", "w", encoding="utf-8") as f:
        f.write(c.to_ppm())
