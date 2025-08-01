import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from functions.functions import *

class complex():
    def __init__(self, real, imaginary):
        '''
        Initiate complex number by attributing a Real part and Imaginary part seperately.
        '''
        self.__real = real
        self.__imaginary = imaginary
        
        self.__pi = chudnovsky_pi()
        self.__current = 0

    def Re(self):
        '''
        Returns the real (Re) part of the complex number
        '''
        return self.__real
    
    def Im(self):
        '''
        Returns the Imaginary part of the complex number
        '''
        return self.__imaginary
    
    def conj(self):
        '''
        Returns complex conjugate of complex number
        '''
        return complex(real = self.Re(), imaginary = (-1)*self.Im())

    def arg(self):
        '''
        Returns complex argument θ
        '''
        x = self.Re()
        y = self.Im()

        match (x, y):
            case (x, y) if x > 0:
                return arctan(y / x)
            case (x, y) if x < 0 and y >= 0:
                return arctan(y / x) + self.__pi
            case (x, y) if x < 0 and y < 0:
                return arctan(y / x) - self.__pi
            case (x, y) if x == 0 and y > 0:
                return self.__pi / 2
            case (x, y) if x == 0 and y < 0:
                return -self.__pi / 2
            case (x, y) if x == 0 and y == 0:
                raise ValueError("undefined atan2(0, 0)")
            case _:
                raise Exception("How the fuck did this happen")
            
    def isGaussian(self): # https://en.wikipedia.org/wiki/Gaussian_integer
        '''
        Returns True if the complex number is a Gaussian Integer
        '''
        return (float(self.Re()).is_integer() and float(self.Im()).is_integer())

    def isEisenstein(self): # https://en.wikipedia.org/wiki/Eisenstein_integer
        '''
        Returns True if the complex number is a Eisenstein Integer
        ''' 
        b: float = round(self.Im() * (2/sqrt(3)), 10)
        a: float = round((self.Re() + b/2), 10)

        print(a, b)

        return a.is_integer() and b.is_integer()

    def __iter__(self):
        yield self.Re()
        yield self.Im()

    def __getitem__(self, ident):
        if ident == 0 or ident == "R":
            return self.Re()
        
        elif ident == 1 or ident == "I":
            return self.Im()
        
        raise KeyError(f"Invalid key: {ident}")

    def __setitem__(self, ident, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        
        if ident == 0 or ident == "R":
            self.__real = value
            return
        
        elif ident == 1 or ident == "I":
            self.__imaginary = value
            return

        raise KeyError(f"Invalid key: {ident}")

    def __delitem__(self, ident):
        if ident == 0 or ident == "R":
            self.__real = 0
            return
        
        elif ident == 1 or ident == "I":
            self.__imaginary = 0
            return

        raise KeyError(f"Invalid key: {ident}")

    def __reversed__(self):
        self.__real, self.__imaginary = self.__imaginary, self.__real

    def __len__(self):
        return 2
    
    def __contains__(self, z):
        if isinstance(z, complex):
            return self.__eq__(z)
        
        elif isinstance(z, (int, float)):
            return self.Re() == z or self.Im() == z
        
        return False

    def __abs__(self):
        '''
        Returns the modulus of the complex number
        '''
        return (self.Re()**2 + self.Im()**2) ** 0.5
    
    def __add__(self, z):
        '''
        Returns the sum of two complex numbers
        '''
        if isinstance(z, complex):
            re_sum = self.Re() + z.Re()
            im_sum = self.Im() + z.Im()

        elif isinstance(z, (int, float)):
            re_sum = self.Re() + z
            im_sum = self.Im()

        else:
            return NotImplemented

        return complex(real = re_sum, imaginary = im_sum)
    
    def __radd__(self, z):
        return self.__add__(z)
    
    def __sub__(self, z):
        '''
        Returns the difference of two complex numbers
        '''
        if isinstance(z, complex):
            re_diff = self.Re() - z.Re()
            im_diff = self.Im() - z.Im()

        elif isinstance(z, (int, float)):
            re_diff = self.Re() - z
            im_diff = self.Im()

        else:
            return NotImplemented
        
        return complex(real = re_diff, imaginary = im_diff)
    
    def __rsub__(self, z):
        if isinstance(z, (int, float)):
            re_diff = z - self.Re()
            im_diff = 0 - self.Im()

            return complex(real = re_diff, imaginary = im_diff)
        
        return NotImplemented
    
    def __mul__(self, z):
        '''
        Returns the product of two complex numbers
        '''
        if isinstance(z, complex):
            re_prod = self.Re()*z.Re() - self.Im()*z.Im()
            im_prod = self.Re()*z.Im() + self.Im()*z.Re()

        elif isinstance(z, (int, float)):
            re_prod = self.Re()*z
            im_prod = self.Im()*z
        
        else:
            return NotImplemented
        
        return complex(real = re_prod, imaginary= im_prod)
    
    def __rmul__(self, z):
        return self.__mul__(z)
    
    def __matmul__(self, z):
        f'{z}'
        return NotImplemented

    def __truediv__(self, z):
        '''
        Returns the quotient of two complex numbers
        '''
        if isinstance(z, complex):
            if not (z.Re() or z.Im()):
                raise ZeroDivisionError(f"{self} cannot be divided by {z}.")

            re_quot = (self.Re()*z.Re() + self.Im()*z.Im()) / (z.Re()**2 + z.Im()**2)
            im_quot = (self.Im()*z.Re() - self.Re()*z.Im()) / (z.Re()**2 + z.Im()**2)

        elif isinstance(z, (int, float)):
            if not z:
                raise ZeroDivisionError(f"{self} cannot be divided by {z}.")
            
            re_quot = self.Re() / z
            im_quot = self.Im() / z

        else:
            return NotImplemented

        return complex(real = re_quot, imaginary= im_quot)

    def __rtruediv__(self, z):
        if isinstance(z, (int, float)):
            if not (self.Re() or self.Im()):
                raise ZeroDivisionError(f"{z} cannot be divided by {self}.")

            new_nominator = self.conj() * z
            new_denominator = self.Re()**2 + self.Im()**2

            return new_nominator.__truediv__(new_denominator)
        
        return NotImplemented

    def __floordiv__(self, z):
        '''
        Returns the floored quotient of two complex numbers
        '''
        divided_z = self.__truediv__(z)

        re = divided_z.Re()
        im = divided_z.Im()

        return complex(real = int(re), imaginary = int(im))
    
    def __rfloordiv__(self, z):
        divided_z = self.__rtruediv__(z)

        re = divided_z.Re()
        im = divided_z.Im()

        return complex(real = int(re), imaginary = int(im))

    def __mod__(self): ...

    def __pow__(self, z):
        # complex**0
        if not z:
            return 1
        
        # complex**real
        elif not isinstance(z, complex):
            modulus = abs(self) ** z
            cos_arg = cos(self.arg() * z)
            sin_arg = sin(self.arg() * z)
            return complex(real = modulus*cos_arg, imaginary=modulus*sin_arg)
        
        # complex**complex
        else:
            new_exponent = z * self.ln()
            return new_exponent.e()
        
    def __rpow__(self, z):
        if z > 0:
            new_ln = ln(z)
        else:
            new_ln = complex(real = ln(abs(z)), imaginary = self.__pi)

        new_exponent = self * new_ln
        return new_exponent.e()

    def __eq__(self, z):
        if isinstance(z, complex):
            return (self.Re() == z.Re()) and (self.Im() == z.Im())
        
        elif isinstance(z, (int,float)):
            return self.Re() == z
    
    def __ne__(self, z):
        return not self.__eq__(z)

    def e(self):
        '''
        Returns the e^z
        '''
        re = self.Re()
        im = self.Im()

        # Converts e^ix to cis(x)
        cisx = complex(real = cos(im), imaginary = sin(im))

        return cisx * complex(real = exp(re), imaginary = 0)
    
    def ln(self):
        '''
        Returns ln(z)
        '''
        return complex(real = ln(abs(self)), imaginary = self.arg())
    
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
        if self.__imaginary >=0 :
            new_imaginary = f" + {self.__imaginary}i"
        else:
            new_imaginary = f" - {str(self.__imaginary)[1:]}i"
        
        return f"{self.__real}{new_imaginary}" 

    def __bool__(self):
        if self.Re() and self.Im():
            return True
        else:
            return False
        
    def __int__(self):
        return int(self.Re() + self.Im())
    
    def __float__(self):
        return float(self.Re() + self.Im())

a = complex(real = 4, imaginary = 3)
b = complex(real = -0.5, imaginary = -6.5)
i = complex(real = 0, imaginary = 1)
c = complex(real = 1, imaginary = 0)
empty = complex(0,0)