# -*- coding: utf-8 -*-
"""
Filename: bifurcation_diagram.py
Reference: http://quant-econ.net/py/python_oop.html
"""
from chaos_class import Chaos
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ch = Chaos(0.1, 4)
r = 2.5
while r < 4:
    ch.r = r
    t = ch.generate_sequence(1000)[900:]
    ax.plot([r] * len(t), t, 'b.', ms=0.6, alpha=0.5)
    r = r + 0.00025
    
ax.set_xlabel(r'$r$', fontsize=16)
plt.show()
