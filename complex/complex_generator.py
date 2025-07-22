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
    
    def modulus(self):
        '''
        Returns the modulus of the complex number
        '''
        return (self.Re()**2 + self.Im()**2) ** 0.5