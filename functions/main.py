import math # Optional, used to graph and compare.

from functions.registry import Registry
from functions.plot import graph
from functions.functions import *
    
#constants.register(name="", method_name="", description="", func=)
constants = Registry()
constants.register(name="phi", method_name="default", description="Generates golden ratio.", func=phi)
constants.register(name="pi", method_name="chudnovsky", description="Generates pi using the Chudnovsky algorithm based on Ramanujan's pi formulae.", func=chudnovsky_pi)
constants.register(name="pi", method_name="leibniz", description="Generates pi using the Madhava-Leibniz series", func=leibniz_pi)
constants.register(name="tau", method_name="default", description="Generates tau, the ratio of a circle's circumferance.", func=tau)
constants.register(name="e", method_name="exp", description="Generates e by using the exponential function, calculated using the Taylor Series.", func=exp_e)
constants.register(name="e", method_name="montecarlo", description="Generates e by using a suboptimal Monte Carlo approach.", func=montecarlo_e)
constants.register(name="mascheroni", method_name="default", description="Generates Euler-Mascheroni by integrating exp(-x)log(x) dx.", func=mascheroni_gamma)
print(f"Loaded constants: {constants.available()}\n")

#functions.register(name="", method_name="", description="", func=)
functions = Registry()
functions.register(name="fibonnaci", method_name="default", description="Generates the nth fibonnaci number based off of the golden ratio.", func=fibonnaci)
functions.register(name="factorial", method_name="default", description="Generates 1⋅2...⋅(x-1)⋅x.", func=factorial)
functions.register(name="exp", method_name="default", description="Generates exponential of x using the Taylor series.", func=exp)
functions.register(name="ln", method_name="default", description="Generates natural logarithm of x using Newton's method.", func=ln)
functions.register(name="sin", method_name="default", description="Generates sine of x using the Taylor series.", func=sin)
functions.register(name="cos", method_name="default", description="Generates sine of x using the Taylor series.", func=cos)
functions.register(name="tan", method_name="default", description="Generates tangent of x using basic Trigonometric Ratios", func=tan)
functions.register(name="gamma", method_name="recursive", description="Generates gamma of x at suboptimal pace, the expansion of factorial using the recursive method.", func=recursion_gamma)
functions.register(name="gamma", method_name="lanczos", description="Generates an approximation of gamma of x featuring Lanczos' approximation method.", func=lanczos_gamma)
print(f"Loaded functions: {functions.available()}\n")

graph(lanczos_gamma, math.gamma, step=0.001, exclude=set(-i for i in range(0,51)))

"""
for name, methods in constants.registry.items():
    for method in methods:
        print(constants.get(name=name, method_name=method, print_description=True)())

for name, methods in functions.registry.items():
    for method in methods:
        print(functions.get(name=name, method_name=method, print_description=True)(x=5))

graph(lanczos_gamma, math.gamma, step=0.001, exclude=set(-i for i in range(0,51)))
graph(sin, math.sin, step=0.001)
graph(exp, math.exp, step=0.001)
"""


