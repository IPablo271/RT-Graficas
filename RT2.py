from Raytracer import *
from material import *

rubber = Material(diffuse=color(255, 0, 0))
ivory = Material(diffuse=color(255, 255, 255))

ray = Raytracer(800, 800)
ray.light = Light(V3(-3, -2, 0), 1)
ray.scene = [
    Sphere(V3(-3, 0, -16), 2, rubber),
    Sphere(V3(2.8, 0, -10), 2., ivory)
]

ray.render()
ray.write('prueba.bmp')