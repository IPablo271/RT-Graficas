class Material:
    def __init__(self, diffuse,albedo,spec,reflactive_index = 0):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.reflactive_index = reflactive_index
