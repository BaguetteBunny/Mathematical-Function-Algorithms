class Vec3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (x, y, z)

        self.NULL = self.__isNullVector()
        self.NUMERICAL = self.__isNumericalVector()

    def check_validity(self):
        try:
            a = Vec3(5, 10, 15)
            b = Vec3(-2, -5, -10)

            # Basic
            assert a == Vec3(5, 10, 15)

            # Sum
            assert 1+a == a+1 == Vec3(6, 11, 16)
            assert a+b == b+a == Vec3(3, 5, 5)

            # Difference
            assert 1-a == Vec3(-4, -9, -14)
            assert a-1 == Vec3(4, 9, 14)
            assert a-b == Vec3(7, 15, 25)
            assert b-a == Vec3(-7, -15, -25)

            # Scalar Multiplication
            assert a*2 == 2*a == Vec3(10, 20, 30)

            # Scalar Division
            assert a/2 == Vec3(2.5, 5, 7.5)
            assert 2/a == Vec3(0.4, 0.2, 2/15)

            # Dot Product
            assert a*b == b*a == -210

            # Norm
            assert a.norm() == abs(a) == 350 ** 0.5

            # Normalize
            assert a.normalize() == Vec3(5/abs(a), 10/abs(a), 15/abs(a))

        except: raise ValueError("Error with Vec3 class. Please report this ASAP!")
        else: print("All vector modules are functioning properly.")

    def __isNullVector(self):
        return self.x == self.y == self.z == 0
        
    def __isNumericalVector(self):
        for n in self.vector:
            if not isinstance(n, (float, int)):
                return False
        return self.x == self.y == self.z == 0

    def __pos__(self):
        return self

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        if isinstance(other, Vec3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return NotImplemented

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
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        return NotImplemented

    def __float__(self):
        return Vec3(float(self.x), float(self.y), float(self.z))
    
    def __int__(self):
        return Vec3(int(self.x), int(self.y), int(self.z))

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
    
    def cross(self, other: 'Vec3'):
        if isinstance(other, Vec3):
            return Vec3(
                self.y*other.z - self.z*other.y,
                self.z*other.x - self.x*other.z,
                self.x*other.y - self.y*other.x
            )
        return NotImplemented

    def triple(self, v: 'Vec3', w: 'Vec3'):
        if isinstance(v, Vec3) and isinstance(w, Vec3):
            return self * v.cross(w)

a = Vec3(5, 10, 15)
b = Vec3(-2, -5, -10)
c = Vec3(-1.5, 60, 0)

# Basic
assert 0+a == +a == a == Vec3(5, 10, 15)
assert 0-a == -a

# Sum
assert 1+a == a+1 == Vec3(6, 11, 16)
assert a+b == b+a == Vec3(3, 5, 5)

# Difference
assert 1-a == Vec3(-4, -9, -14)
assert a-1 == Vec3(4, 9, 14)
assert a-b == Vec3(7, 15, 25)
assert b-a == Vec3(-7, -15, -25)

# Scalar Product
assert a*2 == 2*a == Vec3(10, 20, 30)

# Scalar Quotient
assert a/2 == Vec3(2.5, 5, 7.5)
assert 2/a == Vec3(0.4, 0.2, 2/15)

# Entrywise Product
assert a @ b == b @ a == Vec3(-10, -50, -150)

# Dot Product
assert a*b == b*a == -210

# Cross Product
assert a.cross(b) == -b.cross(a) == Vec3(-25, 20, -5)

# Scalar Triple
assert a.triple(b, c) == b.triple(c, a) == c.triple(a, b) == -a.triple(c, b) == 1237.5

# Norm
assert a.norm() == abs(a) == 350 ** 0.5

# Normalize
assert a.normalize() == Vec3(5/abs(a), 10/abs(a), 15/abs(a))

print("✅ All vector modules are functioning properly. ✅")