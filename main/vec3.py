class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (x, y, z)

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
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented
            
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x + other, self.y + other, self.z + other)
        return NotImplemented
        
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
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x * other, self.y * other, self.z * other)
        return self.dot(other)
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x * other, self.y * other, self.z * other)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x / other, self.y / other, self.z / other)
        return NotImplemented
    
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(other / self.x, other / self.y, other / self.z)
        return NotImplemented
    
    def __matmul__(self, other):
        if isinstance(other, 'Vec3'):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        return NotImplemented
    
    def __rmatmul__(self, other):
        return NotImplemented

    def __str__(self):
        return f"({self.x} ; {self.y} ; {self.z})"
    
    def dot(self, other: 'Vec3'):
        if isinstance(other, Vec3):
            return self.x*other.x + self.y*other.y + self.z*other.z

        return NotImplemented

    def norm(self):
        return (self.x*self.x + self.y*self.y + self.z*self.z) ** 0.5
    
    def normalize(self):
        norm = self.norm()
        return Vec3(self.x / norm, self.y / norm, self.z / norm)

a = Vec3(5, 10, 15)
b = Vec3(-2, -5, -10)
assert a

# Addition
assert 1+a
assert a+1
assert a+b
assert b+a

# Substraction
assert 1-a
assert a-1
assert a-b
assert b-a