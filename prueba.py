from Raytracer import *
from material import *
from color import *
from light import *
White = color(255, 255, 255)

#Colores
rubber = Material(diffuse=color(100, 0, 0), albedo=[0.9, 0.1, 0,0], spec=10)
ivory = Material(diffuse=color(255, 255, 255), albedo=[0.6, 0.3, 0.1,0], spec=50)
mirror = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8,0], spec=1425)
glass = Material(diffuse=color(150, 180, 200), albedo=[0, 0.5, 0.1,0.8], spec=125, reflactive_index=1.5)


ray = Raytracer(800, 600)
ray.light = Light(
    position=V3(-20,20,20),
    intensity=2,
    color=White
)
ray.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(0, 0, -5), 0.5, glass),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, -1, -10), 2, mirror)
]

ray.render()
ray.write('rp.bmp')