# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:45:53 2015

@author: ABerner
"""

from __future__ import print_function

# Ex 1

import numpy as np
import scipy as sp
import scipy.stats as stats
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


# Ex 2

import re

readpath = "C:\\Users\\andrewb\\Documents\\GitHub\\QuantEcon.py\\data\\"
filename = "web_graph_data.txt"
filepath = readpath+filename

#convert lnklst into graph matrix

def graph_from_file(filepath):
    f = open(filepath, 'r')

    idxdict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6,
               'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 
               'n' : 13}
    graph_mat = np.zeros((14,14),dtype=float)    

    for line in f:
        tmp = (re.findall('\w', line))
        graph_mat[idxdict[tmp[0]],idxdict[tmp[1]]] = 1

    return graph_mat

gmat = graph_from_file(filepath)

#normalize graph by number of links to form Markov matrix
n = gmat.shape[0]
gmat = gmat/np.reshape(np.repeat(gmat.sum(axis=1).T,n,axis=0),(n,n))

#solve for stationary distribution
pstat = qe.mc_compute_stationary(gmat)


# Ex 3

def approx_markov(rho, sigma_u, m=3, n=7):
    sigma_y = np.sqrt((sigma_u**2)/(1.-rho**2))
    x_arr = np.linspace(start=-m*sigma_y,stop=m*sigma_y,num=n)
    F = stats.norm(scale=sigma_u**2).cdf
    s = x_arr[1]-x_arr[0]
    P_arr = np.empty((n,n),dtype=float)
    for i in range(0,n):
        for j in range(0,n):
            if j==0:
                P_arr[i][j] = F(x_arr[0]-rho*x_arr[i]+s/2)
            elif j==n-1:
                P_arr[i][j] = 1-F(x_arr[n-1]-rho*x_arr[i]-s/2)
            else:
                P_arr[i][j] = F(x_arr[j]-rho*x_arr[i]+s/2)-F(x_arr[j]-rho*x_arr[i]-s/2)
    return x_arr, P_arr
    

              
    
    
