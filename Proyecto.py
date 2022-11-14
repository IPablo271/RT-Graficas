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
metal = Material(diffuse=color(240,240,240),albedo=[0.9,0.1,0,0],spec=60)
black = Material(diffuse=color(0,0,0), albedo=[0.9,0.1,0,0], spec=40)
ivory = Material(diffuse=color(255, 255, 255), albedo=[0.6, 0.3, 0.1,0], spec=50)
mirror = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8,0], spec=1425)
glass = Material(diffuse=color(150, 180, 200), albedo=[0, 0.5, 0.1,0.8], spec=125, reflactive_index=1.5)
redback = Material(diffuse=color(161,59,73),albedo=[0.9,0.1,0,0],spec=10)
redfront = Material(diffuse=color(102, 47, 65),albedo=[0.9,0.1,0,0],spec=10)
redmidle = Material(diffuse=color(178, 87, 84), albedo=[0.9,0.1,0,0],spec=10)
suncolor = Material(diffuse=color(230, 133, 61), albedo=[0.9,0.1,0,0],spec=10)
glass2 = Material(diffuse=color(242, 227, 207), albedo=[0,1,0.8,0],spec=300)
purple = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8,0], spec=1425)
dorado = Material(diffuse=color(235, 190, 95),albedo=[0.9,0.1,0,0],spec=300)
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

    #Sol 
    Sphere(V3(-1,-1.5,-8), 0.5, suncolor),

    #Primera nave
    Triangle([V3(-3.2, 1.9, -10), V3(-1.4, 2.3, -10), V3(-3.2,3.1, -10), V3(-3.2, 1.9, -10)], metal),
    Cube(V3(-3.5,2.4,-10), 1, black),

    #Segunda Nave
    Triangle([V3(3.2, 1.9, -10), V3(1.4, 2.3, -10), V3(3.2,3.1, -10), V3(3.2, 1.9, -10)], metal),
    Cube(V3(3.5,2.4,-10), 1, black),

    # Balas primera nave
    Sphere(V3(-1,2.3,-10), 0.2, dorado),
    Sphere(V3(-0.5,2.3,-10), 0.2, dorado),

    # Balas segunda nave
    Sphere(V3(0.5,2.3,-10), 0.2, rubber),
    Sphere(V3(1,2.3,-10), 0.2, rubber),

    #Planeta 
    Sphere(V3(3.2,-3.3,-8), 0.5, glass2),

    #Estrellas
    Sphere(V3(3.2,-2.3,-8), 0.15, glass2),
    Sphere(V3(2.2,-3.9,-8), 0.15, glass2),
    Sphere(V3(1.2,-1.3,-8), 0.15, glass2),
    Sphere(V3(0.2,-3.3,-8), 0.2, glass2),
    Sphere(V3(4,-1.3,-8), 0.15, glass2),
    Sphere(V3(-4,-2.3,-8), 0.15, glass2),
    Sphere(V3(-1.9,-3.3,-8), 0.15, glass2),
    Sphere(V3(-2.2,-1.3,-8), 0.15, glass2),
    Sphere(V3(-1.2,-3.4,-8), 0.15, glass2),
    Sphere(V3(-3.2,-2.3,-8), 0.15, glass2),

    #Plano de agua
    Cube(V3(-1.5,6.4,-9), 7, purple),
    









    
   


    #Cube(V3(0.75, -0.75, -2.5), 0.5, rubber),
]
ray.envmap = Envmap('atar.bmp')
ray.render()
ray.write('proyecto2.bmp')