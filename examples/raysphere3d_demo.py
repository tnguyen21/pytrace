import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

#hack to get relative imports working in script
#pylint: disable=wrong-import-position
#pylint: disable=import-error
from tuple import Color, Point
from canvas import Canvas
from ray import Ray, Intersections
from objects import Sphere
from lighting import PointLight, lighting

if __name__ == "__main__":
    wall_size = 7.0
    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    c = Canvas(canvas_pixels, canvas_pixels)
    shape = Sphere()
    shape.material.color = Color(1, 0.2, 1) 
    ray_origin = Point(0, 0, -5)
    wall_z = 10

    light_position = Point(-10, 10, -10)
    light_color = Color(1, 1, 1)
    light = PointLight(light_position, light_color)

    for y in range(canvas_pixels):
        world_y = half - pixel_size * y
        for x in range(canvas_pixels):
            world_x = -half + pixel_size * x
            position = Point(world_x, world_y, wall_z)
            r = Ray(ray_origin, (position - ray_origin).normalize())
            xs = r.intersect(shape)
            hit = Intersections(*xs).hit()

            if hit is not None:
                point = r.position(hit.t)
                normal = hit.obj.normal_at(point)
                eye = -r.direction
                color = lighting(hit.obj.material, light, point, eye, normal)
                c.write_pixel(x, y, color)

    with open("raysphere3d.ppm", "w", encoding="utf-8") as f:
        f.write(c.to_ppm())
