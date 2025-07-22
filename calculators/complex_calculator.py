import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from complex.complex_generator import complex # Overwrite complex module

from functions.functions import *

class Complex_Calculator():
    def __init__(self):
        pass
    
    def sum(self, a: complex, b: complex):
        '''
        Returns the sum of two complex numbers
        '''
        re_sum = a.Re() + b.Re()
        im_sum = a.Im() + b.Im()
        return complex(real = re_sum, imaginary = im_sum)
    
    def difference(self, a: complex, b: complex):
        '''
        Returns the difference of two complex numbers
        '''
        re_diff = a.Re() - b.Re()
        im_diff = a.Im() - b.Im()
        return complex(real = re_diff, imaginary = im_diff)
    
    def product(self, a: complex, b: complex):
        '''
        Returns the product of two complex numbers
        '''
        re_prod = a.Re()*b.Re() - a.Im()*b.Im()
        im_prod = a.Re()*b.Im() + a.Im()*b.Re()
        return complex(real = re_prod, imaginary= im_prod)
    
    def quotient(self, a: complex, b: complex):
        '''
        Returns the quotient of two complex numbers
        '''
        if not (b.Re() or b.Im()):
            raise ZeroDivisionError(f"{a} cannot be divided by {b}")

        re_quot = (a.Re()*b.Re() + a.Im()*b.Im()) / (b.Re()**2 + b.Im()**2)
        im_quot = (a.Im()*b.Re() - a.Re()*b.Im()) / (b.Re()**2 + b.Im()**2)
        return complex(real = re_quot, imaginary= im_quot)
    
    def e(self, z: complex):
        '''
        Returns the e^z
        '''
        re_exp = exp(z.Re())
        im_exp = z.Im()

        # Converts e^ix to cis(x)
        cisx = complex(real = cos(im_exp), imaginary = sin(im_exp))

        return self.product(cisx, complex(real = re_exp, imaginary = 0))

    
calc = Complex_Calculator()
a = complex(real = 4, imaginary = 3)
b = complex(real = -0.5, imaginary = -6.5)

print(calc.sum(a,b))
print(calc.difference(a,b))
print(calc.product(a,b))
print(calc.quotient(a,b))
print(calc.e(a))