import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

#hack to get relative imports working in script
#pylint: disable=wrong-import-position
#pylint: disable=import-error
from tuple import Point, Vector

class Projectile:
    def __init__(self, position: Point, velocity: Vector):
        self.position = position
        self.velocity = velocity

class Environment:
    def __init__(self, gravity: Vector, wind: Vector):
        self.gravity = gravity
        self.wind = wind

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)

if __name__ == "__main__":
    p = Projectile(Point(0, 1, 0), Vector(1, 1, 0))
    e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

    while p.position.y >= 0:
        print(p.position)
        p = tick(e, p)
