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
    
    def __str__(self):
        if self.imaginary >=0 :
            new_imaginary = f" + {self.imaginary}i"
        else:
            new_imaginary = f" - {str(self.imaginary)[1:]}i"
        
        return f"{self.real}{new_imaginary}" 