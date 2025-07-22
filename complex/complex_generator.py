import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from functions.functions import *

class complex():
    def __init__(self, real, imaginary):
        '''
        Initiate complex number by attributing a Real part and Imaginary part seperately.
        '''
        self.real = real
        self.imaginary = imaginary

    def Re(self):
        '''
        Returns the real (Re) part of the complex number
        '''
        return self.real
    
    def Im(self):
        '''
        Returns the Imaginary part of the complex number
        '''
        return self.imaginary
    
    def __abs__(self):
        '''
        Returns the modulus of the complex number
        '''
        return (self.Re()**2 + self.Im()**2) ** 0.5
    
    def __add__(self, z: 'complex'):
        '''
        Returns the sum of two complex numbers
        '''
        re_sum = self.Re() + z.Re()
        im_sum = self.Im() + z.Im()
        return complex(real = re_sum, imaginary = im_sum)
    
    def __sub__(self, z: 'complex'):
        '''
        Returns the difference of two complex numbers
        '''
        re_diff = self.Re() - z.Re()
        im_diff = self.Im() - z.Im()
        return complex(real = re_diff, imaginary = im_diff)
    
    def __mul__(self, z: 'complex'):
        '''
        Returns the product of two complex numbers
        '''
        re_prod = self.Re()*z.Re() - self.Im()*z.Im()
        im_prod = self.Re()*z.Im() + self.Im()*z.Re()
        return complex(real = re_prod, imaginary= im_prod)
    
    def __matmul__(self): ...

    def __truediv__(self, z: 'complex'):
        '''
        Returns the quotient of two complex numbers
        '''
        if not (z.Re() or z.Im()):
            raise ZeroDivisionError(f"{self} cannot be divided by {z}.")

        re_quot = (self.Re()*z.Re() + self.Im()*z.Im()) / (z.Re()**2 + z.Im()**2)
        im_quot = (self.Im()*z.Re() - self.Re()*z.Im()) / (z.Re()**2 + z.Im()**2)
        return complex(real = re_quot, imaginary= im_quot)
    
    def __floordiv__(self): ...

    def __mod__(self): ...

    def __pow__(self): ...

    def e(self):
        '''
        Returns the e^z
        '''
        re = self.Re()
        im = self.Im()

        # Converts e^ix to cis(x)
        cisx = complex(real = cos(im), imaginary = sin(im))

        return cisx * complex(real = exp(re), imaginary = 0)
    
    def sin(self):
        '''
        Returns sin(z)
        '''
        re = self.Re()
        im = self.Im()

        real_part = complex(sin(re)*cosh(im), 0)
        imaginary_part = complex(0, cos(re)*sinh(im))

        return real_part + imaginary_part

    def __str__(self):
        if self.imaginary >=0 :
            new_imaginary = f" + {self.imaginary}i"
        else:
            new_imaginary = f" - {str(self.imaginary)[1:]}i"
        
        return f"{self.real}{new_imaginary}" 

a = complex(real = 4, imaginary = 3)
b = complex(real = -0.5, imaginary = -6.5)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(abs(b))
print(b.e())
print(b.sin())