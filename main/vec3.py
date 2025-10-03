class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (x, y, z)
        self.__inv_vector = (1/x, 1/y, 1/z)

    def __isNullVector(self):
        return self.x == self.y == self.z == 0
        
    def __isNumericalVector(self):
        if self.__isNullVector():
            return False
            
        for n in self.vector:
            if not isinstance(n, (float, int)):
                return False
        return True
        
    def __abs__(self):
        return self.norm()
    
    def _add__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x + other, self.y + other, self.z + other)
            
        elif isinstance(other, 'Vec3'):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
            
        return NotImplemented
            
    def __radd__(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x - other, self.y - other, self.z - other)
            
        elif isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        
        return NotImplemented
        
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(other - self.x, other - self.y, other - self.z)
            
        return NotImplemented
    
    def __str__(self):
        return f"({self.x} ; {self.y} ; {self.z})"


a = Vec3(5, 10, 15)
print(a)