class Registry:
    """
    Constants
        π   Pi
        τ   Tau
        e   Euler's number
        φ   Golden Ratio
        y   Euler's constant

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