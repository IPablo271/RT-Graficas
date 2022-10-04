from intersect import *
class Sphere(object): #Clase para esferas.
    def __init__(self, center, radius,material): #Recibe el centro y el radio.
        self.center = center
        self.radius = radius
        self.material = material
    
    def ray_intersect(self, orig, direction): 
        L = self.center - orig 
        tca = L @ direction 
        l = L.length() 

        d2 = l**2 - tca**2 
        

        if d2 > self.radius**2: 
            return False

        thc = (self.radius**2 - d2)**0.5 

        t0 = tca - thc 
        t1 = tca + thc 
        
        if t0 < 0: 
            t0 = t1
        
        if t0 < 0: 
            return False
        
        impact = orig + direction * t0
        normal = (impact - self.center).normalize()
        return Intersect(
            distance=t0, 
            point=impact, 
            normal=normal
            )