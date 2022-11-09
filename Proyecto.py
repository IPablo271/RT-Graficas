from Raytracer import *
from material import *
from color import *
from light import *
from plane import *
from plane2 import *
from cube import *
from triangle import *
White = color(255, 255, 255)

#Colores
rubber = Material(diffuse=color(100, 0, 0), albedo=[0.9, 0.1, 0,0], spec=10)
ivory = Material(diffuse=color(255, 255, 255), albedo=[0.6, 0.3, 0.1,0], spec=50)
mirror = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8,0], spec=1425)
glass = Material(diffuse=color(150, 180, 200), albedo=[0, 0.5, 0.1,0.8], spec=125, reflactive_index=1.5)
redback = Material(diffuse=color(161,59,73),albedo=[0.9,0.1,0,0],spec=10)
redfront = Material(diffuse=color(102, 47, 65),albedo=[0.9,0.1,0,0],spec=10)
redmidle = Material(diffuse=color(178, 87, 84), albedo=[0.9,0.1,0,0],spec=10)
suncolor = Material(diffuse=color(230, 133, 61), albedo=[0.9,0.1,0,0],spec=10)
suncolor2 = Material(diffuse=color(242, 227, 207), albedo=[0,1,0.8,0],spec=300)
purple = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8,0], spec=1425)
ray = Raytracer(400, 400)
ray.light = Light(
    position=V3(-20,20,20),
    intensity=2,
    color=White
)
ray.scene = [
    # Sphere(V3(0, -1.5, -10), 1.5, ivory),
    # Sphere(V3(0, 0, -5), 0.5, glass),
    # Sphere(V3(1, 1, -8), 1.7, rubber),
    # Sphere(V3(-2, 1, -10), 2, mirror)
    

    Triangle([V3(-1.5, 1, -10), V3(-3.5, -1, -10), V3(-5.5, 1, -10), V3(-1.5, 1, -10)], redback),
    Triangle([V3(-0.5, 1, -10), V3(-2.5, -1, -10), V3(-4.5, 1, -10), V3(-0.5, 1, -10)], redmidle),
    Triangle([V3(-2.5, 1, -10), V3(-4.5, -1, -10), V3(-6.5, 1, -10), V3(-2.5, 1, -10)], redmidle),



    Triangle([V3(1.5, 1, -10), V3(3.5, -1, -10), V3(5.5, 1, -10), V3(1.5, 1, -10)], redback),
    Triangle([V3(0.5, 1, -10), V3(2.5, -1, -10), V3(4.5, 1, -10), V3(0.5, 1, -10)], redmidle),
    Triangle([V3(2.5, 1, -10), V3(4.5, -1, -10), V3(6.5, 1, -10), V3(2.5, 1, -10)], redmidle),

    Triangle([V3(-1.8, 1, -10), V3(0.2, -2.5, -10), V3(1.8, 1, -10), V3(-1.8, 1, -10)], redfront),


    Sphere(V3(-1,-1.5,-8), 0.5, suncolor),
    Plane(V3(0,-0.3,-2), 3,3.6, purple)

    
   


    #Cube(V3(0.75, -0.75, -2.5), 0.5, rubber),
]
ray.envmap = Envmap('atar.bmp')
ray.render()
ray.write('proyecto2.bmp')