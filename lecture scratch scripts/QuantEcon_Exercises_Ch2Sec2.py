# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:45:53 2015

@author: ABerner
"""

# Ex 1

import numpy as np
import quantecon as qe
import matplotlib.pyplot as plt

alpha = 0.1
beta = 0.1

P = np.array([[1-alpha,alpha],[beta,1-beta]])

p_UnEmp = beta/(alpha+beta)

n = 10000
x0s = [0,1]

fig, ax = plt.subplots()
inds = np.linspace(1,n+1,n,dtype=float)

for x0 in x0s: 
    s = qe.mc_sample_path(P, init=x0, sample_size=n)
    tmp = np.cumsum(s==0)/inds-p_UnEmp
    ax.plot(inds-1,tmp)
    
ax.set_xlim([0,n])
    
