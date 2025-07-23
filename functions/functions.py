import random # Optional, for Monte Carlo integration of e

def phi(): # https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
    return (1+5**0.5)/2

def chudnovsky_pi(n: int = 5): # https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    inverse_pi = 0
    for k in range(n+1):
        numerator = ((-1)**k) * factorial(6*k) * (545140134*k + 13591409)
        denominator = factorial(3*k) * factorial(k)**3 * (640320)**(3*k+1.5)
        inverse_pi += numerator/denominator
    return (1/(inverse_pi))/12

def leibniz_pi(n: int = 10_000_000): #https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    total = 0
    sign = 1
    for i in range(1,n+1,2):
        total += (1/i)*sign
        sign*=-1
    return total*4

def tau(pi_function=chudnovsky_pi, n: int = 5): #https://en.wikipedia.org/wiki/Tau_(mathematics)
    return 2*pi_function(n)

def exp_e(n: int = 100): # https://en.wikipedia.org/wiki/E_(mathematical_constant)
    return exp(1, n)

def montecarlo_e(n: int = 10_000_000): # https://en.wikipedia.org/wiki/Monte_Carlo_integration
    values = 0
    for _ in range(n):
        x=0
        while x < 1:
            x+= random.random()
            values += 1
    return values/n

def mascheroni_gamma(n: int = 10_000): # https://en.wikipedia.org/wiki/Euler%27s_constant#Integrals
    return sum(1/k - ln(1 + 1/k) for k in range(1, n+1))

def sqrt(x):
    assert x>= 0
    return x**0.5

def fibonnaci(x: int, phi=phi()): #https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
    assert x>=0
    return int((phi**x - (-phi)**(-x))/(2*phi-1))

def factorial(x: int): # Factorial function using incremented multiplications
    assert x>=0
    if x<2:
        return 1
    for i in range(2,x):
        x*=i
    return x

def exp(x, n: int = 100): # https://en.wikipedia.org/wiki/Taylor_series
    final = 0
    for k in range(0,n+1):
        final+=(x**k)/factorial(k)
    return final

def ln(x, epsilon: float = 1e-8): # https://en.wikipedia.org/wiki/Newton%27s_method
    assert x>0
    y = 1
    while abs(exp(y,20) - x) > epsilon:
        y = y-1 + x/exp(y,20)
    return y

def sin(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    x %= 2*pi
    if x>pi:
        x -= 2*pi
    
    result = 0
    sign = 1
    for n in range(0, 50):
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
    for n in range(0, 50):
        term = (x**(2*n)) / factorial(2*n)
        result += sign * term
        sign *= -1
    return result

def tan(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Trigonometry#Trigonometric_ratios
    cosine = cos(x,pi)
    if cosine == 0:
        raise ZeroDivisionError("Undefined for odd multiples of π/2")
    return sin(x,pi)/cosine

def arctan(x, n=75, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Infinite_series
    if abs(x) <= 1:
        return sum(((-1)**i * x**(2*i + 1)) / (2*i + 1) for i in range(n))
    elif x > 0:
        return pi/2 - arctan(1/x, n)
    else:
        return pi/2 - arctan(1/x, n)

def sec(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Trigonometry#Trigonometric_ratios
    cosine = cos(x,pi)
    if cosine == 0:
        raise ZeroDivisionError("Undefined for odd multiples of π/2")
    return 1/cosine

def csc(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Trigonometry#Trigonometric_ratios
    sine = sin(x,pi)
    if sine == 0:
        raise ZeroDivisionError("Undefined for multiples of π")
    return 1/sine

def cot(x, pi=chudnovsky_pi()): # https://en.wikipedia.org/wiki/Trigonometry#Trigonometric_ratios
    sine = sin(x,pi)
    if sine == 0:
        raise ZeroDivisionError("Undefined for multiples of π")
    return cos(x,pi)/sine

def cosh(x): #https://en.wikipedia.org/wiki/Hyperbolic_functions#Exponential_definitions
    return (exp(x)+exp(-x))/2

def sinh(x): #https://en.wikipedia.org/wiki/Hyperbolic_functions#Exponential_definitions
    return (exp(x)-exp(-x))/2

def tanh(x): #https://en.wikipedia.org/wiki/Hyperbolic_functions#Exponential_definitions
    return sinh(x)/cosh(x)

def sech(x): #https://en.wikipedia.org/wiki/Hyperbolic_functions#Exponential_definitions
    return 1/cosh(x)

def csch(x): #https://en.wikipedia.org/wiki/Hyperbolic_functions#Exponential_definitions
    return 1/sinh(x)

def coth(x): #https://en.wikipedia.org/wiki/Hyperbolic_functions#Exponential_definitions
    return cosh(x)/sinh(x)

def recursion_gamma(x, pi=chudnovsky_pi(), sin_func=sin): # https://en.wikipedia.org/wiki/Gamma_function
    # Recursion limit
    if abs(x-1) < 1e-8:
        return 1
    if abs(x-0.5) < 1e-8:
        return pi**0.5
    
    # 1. Integers
    if isinstance(x, int) or int(x) == x:
        if x <= 0:
            return "undefined"
        return factorial(int(x)-1)
    
    # 2. Float
    if x > 1:
        return (x-1)*recursion_gamma(x-1)
    return pi/(sin_func(pi*x)*recursion_gamma(1-x))

def lanczos_gamma(x, n_coef: int = 9, pi: float = chudnovsky_pi(), sin_func=sin, exp_func=exp): # https://en.wikipedia.org/wiki/Lanczos_approximation
    match n_coef:
        case 5:
            g_coefficient = 5
            p_precomputed = [
                1.0000018972739440364,
                76.180082222642137322,
                -86.505092037054859197,
                24.012898581922685900,
                -1.2296028490285820771
            ]
        case 7:
            g_coefficient = 5
            p_precomputed = [
                1.0000000001900148240,
                76.180091729471463483,
                -86.505320329416767652,
                24.014098240830910490,
                -1.2317395724501553875,
                0.0012086509738661785061,
                -5.3952393849531283785e-6
            ]
        case 9:
            g_coefficient = 7
            p_precomputed = [
                0.99999999999980993,
                676.5203681218851,
                -1259.1392167224028,
                771.32342877765313,
                -176.61502916214059,
                12.507343278686905,
                -0.13857109526572012,
                9.9843695780195716e-6,
                1.5056327351493116e-7
            ]
        case 12:
            g_coefficient = 8
            p_precomputed = [
                0.9999999999999999298,
                1975.3739023578852322,
                -4397.3823927922428918,
                3462.6328459862717019,
                -1156.9851431631167820,
                154.53815050252775060,
                -6.2536716123689161798,
                0.034642762454736807441,
                -7.4776171974442977377e-7,
                6.3041253821852264261e-8,
                -2.7405717035683877489e-8,
                4.0486948817567609101e-9
            ]
        case _: 
            return ValueError
    
    if x < 0.5:
        return pi / (sin_func(pi * x) * lanczos_gamma(1 - x))

    x -= 1
    a = p_precomputed[0]
    for i in range(1, len(p_precomputed)):
        a += p_precomputed[i] / (x + i)

    t = x + g_coefficient + 0.5
    return (2 * pi)**(1/2) * t**(x + 0.5)*exp_func(-t)*a