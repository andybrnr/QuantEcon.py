# -*- coding: utf-8 -*-
"""
Filename: chaos_class.py
Reference: http://quant-econ.net/py/python_oop.html
"""
class Chaos:
    """
    Models the dynamical system with :math: `x_{t+1} = r x_t (1 - x_t)`
    """
    def __init__(self, x0, r):
        """
        Initialize with state x0 and parameter r
        """
        self.x, self.r = x0, r
        
    def update(self):
        "Apply the map to update state."
        self.x = self.r * self.x * (1 - self.x)
        
    def generate_sequence(self, n):
        "Generate and return a sequence of length n."
        path = []
        for i in range(n):
            path.append(self.x)
            self.update()
        return path

def __main__():
    from chaos_class import Chaos
    import matplotlib.pyplot as plt    
    
    ch = Chaos(0.1, 4.0) # x0 = 0.1 and r = 0.4
    ts_length = 250    
    
    fig, ax = plt.subplots()
    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$x_t$', fontsize=14)
    x = ch.generate_sequence(ts_length)
    ax.plot(range(ts_length), x, 'bo-', alpha=0.5, lw=2, label=r'$x_t$')
    plt.show()
    return None
    
