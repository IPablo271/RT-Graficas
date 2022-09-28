from Utilities import *
from Sphere import *
from vector import *

modelo1 = [
    Sphere(V3(-0.3, -3.3, -16), 0.05, color(255, 255, 255)),
    Sphere(V3(0.3, -3.3, -16), 0.05, color(255, 255, 255)),
    Sphere(V3(-0.3, -3.3, -16), 0.2, color(0, 0, 0)),
    Sphere(V3(0.3, -3.3, -16), 0.2, color(0, 0, 0)),
    Sphere(V3(0, -2.8, -16), 0.12, color(255, 128, 0)),
    Sphere(V3(0, -0.6, -16), 0.2, color(0, 143, 57)),
    Sphere(V3(0, 2, -16), 0.2, color(255, 0, 0)),
    Sphere(V3(0, -3, -16), 1, color(255, 255, 255)),
    Sphere(V3(0, -0.6, -16), 1.5, color(255, 255, 255)),
    Sphere(V3(0, 2, -16), 2, color(255, 255, 255)),
    Sphere(V3(0, -4, -16), 0.5, color(255, 0, 0)),
]

def returnmodelo():
    return modelo1