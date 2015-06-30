# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:45:53 2015

@author: ABerner
"""

# Code snippet from pg 200

import numpy as np
from quantecon import mc_sample_path
P = np.array([[.4,.6],[.2,.8]])
s = mc_sample_path(P, init=(0.5, 0.5), sample_size=100000)
print((s ==0).mean())

# Example: Powers of a Markov Matrix on page 201

P = np.array([[.971,.029,0],[.145,.778,0.077],[0,0.508,0.492]])
psi = np.arry([0.80,0.19,0.01]) #hypothetical state probability estimate vector
np.inner(np.dot(psi,np.linalg.matrix_power(P,6)),np.array([0,1,1])) #6m forward forecast of recession probability given the current state estimates