from Sphere import *
from math import *
from vector import *
from Utilities import *
import random 
from writebmp import *
from color import *
from material import *
from light import *
MAX_RECURSION_DEPTH = 3
LIGHTBLUE = color(173, 216, 230)
WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)

class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = LIGHTBLUE
        self.current_color = LIGHTBLUE
        self.clear()
        self.scene = []
        self.light = Light(V3(0,0,0),1,color(255,255,255))
        self.density = 1

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c.toBytes() or self.current_color.toBytes()

    def write(self, filename):
        writefile(filename, self.width, self.height, self.framebuffer)
        
    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)

        for y in range(self.height):
            for x in range(self.width):
                if random.random() < self.density:
                    i = ((2 * (x + 0.5) / self.width ) - 1) * ar * tana
                    j = (1 - (2 * (y + 0.5) / self.height )) * tana

                    direction = V3(i, j, -1).normalize()
                    origin = V3(0, 0, 0)
                    c = self.cast_ray(origin, direction)

                    self.point(x, y, c)

        
    def cast_ray(self, origin, direction,recursion = 0):
        if recursion == MAX_RECURSION_DEPTH:
            return self.background_color

        material, intersect = self.scene_intersect(origin, direction)
        if material is None:
            return self.background_color

        light_dir = (self.light.position - intersect.point).normalize()

        


        #Shadow
        shadow_bisas = 1.1
        shadow_origin = intersect.point + (intersect.normal * shadow_bisas) 
        shadow_material, shadow_intersect = self.scene_intersect(shadow_origin, light_dir)
        shadow_intensity = 0

        if shadow_material:
            shadow_intensity = 0.7

        difusse_intensity = light_dir @ intersect.normal

        diffuse = material.diffuse * difusse_intensity * material.albedo[0] * (1 - shadow_intensity)



        light_dir = self.reflect(light_dir, intersect.normal)
        intensity = max(0,light_dir @ direction)

        specular_intensity = self.light.intensity * intensity ** material.spec
        specular = self.light.color * specular_intensity * material.albedo[1]

        #Relection
        if material.albedo[2] > 0:
            reverse_direction = direction * - 1
            reflect_direction = self.reflect(reverse_direction, intersect.normal)
            reflection_bias = -0.5 if reflect_direction @ intersect.normal else 0.5
            reflect_origin = intersect.point + (intersect.normal * reflection_bias)
            reflect_color = self.cast_ray(reflect_origin, reflect_direction,recursion + 1)
        else:
            reflect_color = color(0, 0, 0)
        
        #Refraction
        if material.albedo[3] > 0:
            refract_direction = self.refract(direction, intersect.normal,material.reflactive_index)
            refract_bias = -0.5 if refract_direction @ intersect.normal else 0.5
            refract_origin = intersect.point + (intersect.normal * refract_bias)
            refract_color = self.cast_ray(refract_origin, refract_direction,recursion + 1)
        else:
            refract_color = color(0, 0, 0)
        
        reflection = reflect_color * material.albedo[2]
        refraction = reflect_color * material.albedo[3]

        return diffuse + specular + reflection + refraction


    def reflect( self,direction,normal):
        return (direction - normal * 2 * (direction @ normal)).normalize()

    def refract( self,I,N,roi):
        etai = 1
        etat = roi
        cosi = (I @ N) * - 1
        
        if (cosi < 0 ):
            cosi *= -1
            etai *= -1
            etat *= -1
            N *= -1

        eta = etai/ etat 
        k = 1 - eta **2 * (1 - cosi ** 2)

        if k < 0:
            return V3(0,0,0)
        
        cost = k ** 0.5

        return ((I * eta) +  (N * (eta * cosi - cost))).normalize()

    def scene_intersect(self, origin, direction):
        zbuffer = 99999
        material = None
        intersect = None

        for o in self.scene:
            object_intersect = o.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = o.material
                    intersect = object_intersect
        return material, intersect

