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

"""
    Constants
        π       pi()         Pi
        τ       tau()        Tau
        e       e()          Euler's number
        φ       phi()        Golden Ratio
        y       euler()      Euler's constant
"""

# https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
def phi():
    return (1+5**0.5)/2

# https://en.wikipedia.org/wiki/Chudnovsky_algorithm
def pi(n=5):
    inverse_pi = 0
    for k in range(n+1):
        numerator = ((-1)**k) * factorial(6*k) * (545140134*k + 13591409)
        denominator = factorial(3*k) * factorial(k)**3 * (640320)**(3*k+1.5)
        inverse_pi += numerator/denominator
    return (1/(inverse_pi))/12

#https://en.wikipedia.org/wiki/Tau_(mathematics)
def tau(n=5):
    return 2*pi(n)

# https://en.wikipedia.org/wiki/E_(mathematical_constant)
def e(n=100):
    return exp(1, n)

# https://en.wikipedia.org/wiki/Monte_Carlo_integration
def fun_e(n=100):
    """This is terrible. Don't use this. It's just a demonstration of how to use the Monte Carlo method to approximate e."""
    values = 0
    for _ in range(n):
        x=0
        while x < 1:
            x+= random.random()
            values += 1
    return values/n

# https://en.wikipedia.org/wiki/Euler%27s_constant#Integrals
def euler(n=100_000):
    return sum(1/k - ln(1 + 1/k) for k in range(1, n+1))


"""
    Functions
        Ƒ(n)        fibonnaci(n)        Fibonnaci Sequence
        n!          factorial(n)        Factorial Function
        eⁿ          exp(n)              Exponential Function
        ln(n)       ln(n)               Natural Logarithm Function
        sin(n)      sin(n)              Sine Function
        Γ(n)        gamma(n)            Gamma Function
"""

#https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
def fibonnaci(n, phi=phi()):
    return int((phi**n - (-phi)**(-n))/(2*phi-1))

# Factorial function using incremented multiplications
def factorial(x):
    assert isinstance(x,int) and x>=0
    if x<2:
        return 1
    for i in range(2,x):
        x*=i
    return x

# https://en.wikipedia.org/wiki/Taylor_series
def exp(x,n=100):
    final = 0
    for k in range(0,n+1):
        final+=(x**k)/factorial(k)
    return final

# https://en.wikipedia.org/wiki/Newton%27s_method
def ln(x, n=1e-10):
    y = 1
    while abs(exp(y,20) - x) > n:
        y = y-1 + x/exp(y,20)
    return y

# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
def sin(x, pi=pi()):
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

# https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
def cos(x, pi=pi()):
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

# https://en.wikipedia.org/wiki/Gamma_function
def gamma(x, pi=pi()):
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

# plot(gamma, math.gamma, x=5, step=1)
print(fun_e(10000000))
