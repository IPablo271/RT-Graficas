from Sphere import *
from math import *
from vector import *
from Utilities import *
import random 
import writebmp
class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.clear()
        self.scene = []
        self.density = 1

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c or self.current_color

    def write(self, filename):
        writefile(filename, self.width, self.height, self.framebuffer)