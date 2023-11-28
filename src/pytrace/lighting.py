# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# #hack to get imports working in package
# #pylint: disable=wrong-import-position
# #pylint: disable=import-error
# from tuple import Tuple, Point, Vector

from .tuple import Color, Point, Vector
from .material import Material


class PointLight:
    def __init__(self, position: Point, intensity: Color):
        self.position = position
        self.intensity = intensity

def lighting(
    m: Material,
    light: PointLight,
    position: Point,
    eye_vector: Vector,
    normal_vector: Vector
) -> Color:
    """ rough impl of phong shading model """
    # combine surface color w light color + intensity
    effective_color = m.color * light.intensity

    # find direction to light source
    light_vector = (light.position - position).normalize()

    # compute ambient contribution
    ambient = effective_color * m.ambient

    # compute angle between light vector and normal vector
    # neg number means light behind surface
    light_dot_normal = light_vector.dot(normal_vector)
    if light_dot_normal < 0:
        diffuse = Color(0, 0, 0)
        specular = Color(0, 0, 0)
    else:
        # compute diffuse contribution
        diffuse = effective_color * m.diffuse * light_dot_normal

        # reflect light vector, neg number means light reflects away from eye
        reflect_vector = (-light_vector).reflect(normal_vector)

        # compute specular contribution
        reflect_dot_eye = reflect_vector.dot(eye_vector)
        if reflect_dot_eye <= 0:
            specular = Color(0, 0, 0)
        else:
            factor = reflect_dot_eye ** m.shininess
            specular = light.intensity * m.specular * factor

    # final shading is sum of all light contributions
    final_color = ambient + diffuse + specular
    return Color(final_color.x, final_color.y, final_color.z)
