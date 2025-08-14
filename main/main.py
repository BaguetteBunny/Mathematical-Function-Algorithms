from complex import complex
from registry import functions as FUNCTIONS
from registry import constants as CONSTANTS
from plot import graph

import math # Optional, used to graph and compare.

print("Hello World!")

"""
for name, methods in CONSTANTS.registry.items():
    for method in methods:
        print(CONSTANTS.get(name=name, method_name=method, print_description=True)())

for name, methods in FUNCTIONS.registry.items():
    for method in methods:
        print(FUNCTIONS.get(name=name, method_name=method, print_description=True)(x=5))

graph(FUNCTIONS.get(name="gamma", method_name="lanczos"), math.gamma, step=0.001, exclude=set(-i for i in range(0,51)))
graph(FUNCTIONS.get(name="sin"), math.sin, step=0.001)
graph(FUNCTIONS.get(name="exp"), math.exp, step=0.001)
"""

"""
print([func for func in dir(complex) if callable(getattr(complex, func)) and not func.startswith("__")])

a = complex(real = 4, imaginary = 3)
b = complex(real = -0.5, imaginary = -6.5)
i = complex(real = 0, imaginary = 1)
c = complex(real = 1, imaginary = 0)
empty = complex()
"""
