import matplotlib.pyplot as plt
import math
import random

def plot(func, true_func, x=None, step=2, domain=[-50,50]):
    abscissa = []
    y1 = []
    y2 = []

    abscissa = [x * step for x in range(domain[0], domain[1])]
    if callable(true_func):
        y1 = [func(i*step) for i in range(domain[0], domain[1])]
        y2 = [true_func(i*step) for i in range(domain[0], domain[1])]
    else:
        y1 = [func() for _ in range(domain[0], domain[1])]
        y2 = [true_func for _ in range(domain[0], domain[1])]


    plt.plot(abscissa, y1, label=func.__name__, color="red", linestyle='-')
    plt.plot(abscissa, y2, label="True Function", color="blue", linestyle='-')
    plt.title(f"Accuracy Chart for {func.__name__}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

class ConstantRegistry:
    """
    Constants
        π   Pi
        τ   Tau
        e   Euler's number
        φ   Golden Ratio
        y   Euler's constant
    """
    def __init__(self):
        self.registry = {}

    def register(self, name, func, method_name="default", description="Error: No description provided."):
        if name not in self.registry:
            self.registry[name] = {}
        self.registry[name][method_name] = {
            "func": func,
            "desc": description
        }

    def get(self, name, method_name="default", print_description=False):
        if print_description:
            print(self.registry[name][method_name]["desc"])
        return self.registry[name][method_name]["func"]
    
    def available(self):
        return {
            const: list(methods.keys())
            for const, methods in self.registry.items()
        }
    
def phi(): # https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
    return (1+5**0.5)/2

def chudnovsky_pi(n=5): # https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    inverse_pi = 0
    for k in range(n+1):
        numerator = ((-1)**k) * factorial(6*k) * (545140134*k + 13591409)
        denominator = factorial(3*k) * factorial(k)**3 * (640320)**(3*k+1.5)
        inverse_pi += numerator/denominator
    return (1/(inverse_pi))/12

def tau(pi_function=chudnovsky_pi, n=5): #https://en.wikipedia.org/wiki/Tau_(mathematics)
    return 2*pi_function(n)

def exp_e(n=100): # https://en.wikipedia.org/wiki/E_(mathematical_constant)
    return exp(1, n)

def montecarlo_e(n=100): # https://en.wikipedia.org/wiki/Monte_Carlo_integration
    values = 0
    for _ in range(n):
        x=0
        while x < 1:
            x+= random.random()
            values += 1
    return values/n

def euler_gamma(n=100_000): # https://en.wikipedia.org/wiki/Euler%27s_constant#Integrals
    return sum(1/k - ln(1 + 1/k) for k in range(1, n+1))


class FunctionRegistry:
    """
    Functions
        Ƒ(n)        Fibonnaci Sequence
        n!          Factorial Function
        eⁿ          Exponential Function
        ln(n)       Natural Logarithm Function
        sin(n)      Sine Function
        Γ(n)        Gamma Function
    """
    def __init__(self):
        self.registry = {}

    def register(self, name, method_name, description, func):
        if name not in self.registry:
            self.registry[name] = {}
        self.registry[name][method_name] = {
            "func": func,
            "desc": description
        }

    def get(self, name, method_name="default"):
        return self.registry[name][method_name]["func"]
    
    def available(self):
        return {
            const: list(methods.keys())
            for const, methods in self.registry.items()
        }

def fibonnaci(n, phi=phi()): #https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
    return int((phi**n - (-phi)**(-n))/(2*phi-1))

def factorial(x): # Factorial function using incremented multiplications
    assert isinstance(x,int) and x>=0
    if x<2:
        return 1
    for i in range(2,x):
        x*=i
    return x

def exp(x,n=100): # https://en.wikipedia.org/wiki/Taylor_series
    final = 0
    for k in range(0,n+1):
        final+=(x**k)/factorial(k)
    return final

def ln(x, n=1e-10): # https://en.wikipedia.org/wiki/Newton%27s_method
    y = 1
    while abs(exp(y,20) - x) > n:
        y = y-1 + x/exp(y,20)
    return y

def sin(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    x %= 2*pi
    if x>pi:
        x -= 2*pi
    
    result = 0
    sign = 1
    for n in range(0, 7):
        term = (x**(2*n+1)) / factorial(2*n+1)
        result += sign * term
        sign *= -1
    return result

def cos(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    x %= 2*pi
    if x>pi:
        x -= 2*pi
    
    result = 0
    sign = 1
    for n in range(0, 7):
        term = (x**(2*n)) / factorial(2*n)
        result += sign * term
        sign *= -1
    return result

def gamma(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Gamma_function
    # Recursion limit
    if abs(x-1) < 1e-8:
        return 1
    if abs(x-0.5) < 1e-8:
        return pi**0.5
    
    # 1. Integers
    if isinstance(x, int) or int(x) == x:
        if x <= 0:
            return "undefined"
        return factorial(x-1)
    
    # 2. Float
    if x > 1:
        return (x-1)*gamma(x-1)
    return pi/(sin(pi*x)*gamma(1-x))

"""
    Constants
        π       pi()         Pi
        τ       tau()        Tau
        e       e()          Euler's number
        φ       phi()        Golden Ratio
        y       euler()      Euler's constant
"""

#constants.register(name="", method_name="", description="", func=)
constants = ConstantRegistry()
constants.register(name="phi", method_name="default", description="Generates golden ratio.", func=phi)
constants.register(name="pi", method_name="chudnovsky", description="Generates pi using the Chudnovsky algorithm based on Ramanujan's pi formulae.", func=chudnovsky_pi)
constants.register(name="tau", method_name="default", description="Generates tau, the ratio of a circle's circumferance.", func=tau)
constants.register(name="e", method_name="exp", description="Generates e by using the exponential function, calculated using the Taylor Series.", func=exp_e)
constants.register(name="e", method_name="montecarlo", description="Generates e by using a suboptimal Monte Carlo approach.", func=montecarlo_e)
constants.register(name="gamma", method_name="default", description="Generates gamma by integrating exp(-x)log(x) dx.", func=euler_gamma)
print(f"Loaded constants: {constants.available()}")

#functions.register(name="", method_name="", description="", func=)
functions = FunctionRegistry()
functions.register(name="fibonacci", method_name="default", description="Generates the nth fibonnaci number based off of the golden ratio.", func=fibonnaci)
functions.register(name="factorial", method_name="default", description="Generates 1⋅2...⋅(x-1)⋅x.", func=factorial)
functions.register(name="exp", method_name="default", description="Generates exponential of x using the Taylor series.", func=exp)
functions.register(name="ln", method_name="default", description="Generates natural logarithm of x using Newton's method.", func=ln)
functions.register(name="sin", method_name="default", description="Generates sine of x using the Taylor series.", func=sin)
functions.register(name="cos", method_name="default", description="Generates sine of x using the Taylor series.", func=cos)
functions.register(name="gamma", method_name="default", description="Generates gamma of x, the expansion of factorial using the general method.", func=gamma)
print(f"Loaded functions: {functions.available()}")

# plot(gamma, math.gamma, x=5, step=1)
# print(fun_e(10000000))
