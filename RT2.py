from Raytracer import *
from material import *
from color import *
from light import *
White = color(255, 255, 255)

#Colores
lighBrown = Material(diffuse=color(200, 158, 130),albedo=[1,0], spec=0)
darkerBrown = Material(diffuse=color(178, 95, 3), albedo=[0.9,0.1],spec=0)
black = Material(diffuse=color(0,0,0), albedo=[0.9,0.1], spec=40)
red = Material(diffuse=color(255,50,52), albedo=[0.7,0.3], spec=60)
metal = Material(diffuse=color(240,240,240),albedo=[0.9,0.1],spec=60)

ray = Raytracer(1200, 1000)
ray.light = Light(
    position=V3(0,0,0),
    intensity=2,
    color=White
)
ray.scene = [
    #Cuerpo
    Sphere(V3(-3.0, 0, -10), 1.7, red),
    Sphere(V3(3.0, 0, -10), 1.7, metal),

    #Cabeza
    Sphere(V3(-3.0, -1.5, -10), 1.4, lighBrown),

    #Ojos
    Sphere(V3(-3.1, -1.8, -8.8), 0.22, black),
    Sphere(V3(-2.3, -1.8, -9.0), 0.22, black),

    #Nariz
    Sphere(V3(-2.73, -1.4, -9.0), 0.48, darkerBrown),


    #Orejas
    Sphere(V3(-3.6, -2.5, -9), 0.6, darkerBrown),
    Sphere(V3(-1.6, -2.5, -10), 0.65, darkerBrown),

    #Brazos
    Sphere(V3(-4.4, -0.4, -9), 0.7, darkerBrown),
    Sphere(V3(-1.1, -0.4, -10), 0.7, darkerBrown),

    #Piernas
    Sphere(V3(-3.8, 1.4, -9), 0.7, darkerBrown),
    Sphere(V3(-1.4, 1.4, -10), 0.75, darkerBrown),
   


    
]

ray.render()
ray.write('prueba.bmp')