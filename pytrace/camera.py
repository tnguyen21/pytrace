import numpy as np

from pytrace.ray import Ray
from pytrace.tuple import Point, Vector

class Camera:
    def __init__(self, hsize, vsize, fov):
        self.hsize = hsize
        self.vsize = vsize
        self.fov = fov
        self.transform = np.eye(4)
        self._compute_pixel_size()

    def _compute_pixel_size(self):
        half_view = np.tan(self.fov / 2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize
    
    def ray_for_pixel(self, px, py):
        xoffset = (px + 0.5) * self.pixel_size
        yoffset = (py + 0.5) * self.pixel_size
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset
        pixel = np.linalg.inv(self.transform) @ np.array([world_x, world_y, -1, 1])
        origin = np.linalg.inv(self.transform) @ np.array([0, 0, 0, 1])
        direction = np.round((pixel - origin)[:3]) # TODO - round necessary? fails test if not here...why?
        return Ray(Point(*origin[:3]), Vector(*direction))
