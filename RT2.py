from Raytracer import * 
from models import *
r = Raytracer(800, 600)

r.scene = returnmodelo()

r.render()
r.write('r.bmp')