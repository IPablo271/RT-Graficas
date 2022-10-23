from intersect import *
from vector import *
class Plane(object): #Clase para esferas.
    def __init__(self, center,w,l,material): #Recibe el centro y el radio.
        self.center = center
        self.w = w
        self.l = l
        self.material = material
    def ray_intersect(self, origin, direction): 
        d = -(origin.y + self.center.y) / direction.y
        impact = (direction * d) - origin 
        normal = V3(0,1,0)
        
        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) or \
            impact.z > (self.center.z + self.l/2) or impact.z < (self.center.z - self.l/2):
            return None
        return Intersect(
            distance=d, 
            point=impact, 
            normal=normal
        )