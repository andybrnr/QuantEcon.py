# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:38:11 2015

@author: ABerner
"""

#Ex 1

from __future__ import print_function
import numpy as np
from numba import jit

#pure python

p_stayhi = 0.8
p_staylo = 0.9
p_lo2hi = 0.1
p_hi2lo = 0.2

probs = (p_stayhi,p_staylo,p_lo2hi,p_hi2lo)

s_init = 1
n = 100000

def fin_markov(probs,s_init,n):
    p_stayhi, p_staylo = probs[0], probs[1]
    m_path = np.ones(n+1, dtype=int)  
    curr_state = s_init    
    draws = np.random.uniform(0,1,n)
    for ind in range(0,n):
        if curr_state==1 and draws[ind]>p_stayhi:
            curr_state=0
        elif curr_state==0 and draws[ind]>p_staylo:
            curr_state=1
        m_path[ind+1]=curr_state
    return m_path
    
m_path = fin_markov(probs,s_init,n)

print(np.sum(m_path)/(n*1.0))
            
# using numba with numpy

@jit    
def fm_inner_loop(m_path,draws,p_stayhi,p_staylo,curr_state):
    tmp = curr_state
    for ind in range(0,n):
        if tmp==1 and draws[ind]>p_stayhi:
            tmp=0
        elif tmp==0 and draws[ind]>p_staylo:
            tmp=1
        m_path[ind+1]=tmp
    return m_path
        
def fin_markov_numba(probs,s_init,n):
    p_stayhi, p_staylo = probs[0], probs[1]
    m_path = np.ones(n+1, dtype=int)  
    curr_state = s_init    
    draws = np.random.uniform(0,1,n)
    return fm_inner_loop(m_path,draws,p_stayhi,p_staylo,curr_state)
    
m_path = fin_markov_numba(probs,s_init,n)

print(np.sum(m_path)/(n*1.0))

# using cython

%load_ext cython

%%cython
from numpy cimport float_t
def fm_cython(double p_stayhi,double p_staylo, int s_init, int n):
    cdef int t
    cdef int curr_state
    curr_state = s_init
    
    m_np_array = np.ones(n+1,dtype=float)
    d_np_array = np.random.uniform(0,1,n)
    
    cdef float_t [:] m = m_np_array
    m[0] = curr_state
    
    cdef float_t [:] d = d_np_array
    for t in range(n):
        if curr_state==1 and d[t]>p_stayhi:
            curr_state = 0
        elif curr_state==0 and d[t]>p_staylo:
            curr_state = 1
        m[t+1] = curr_state
    return np.asarray(m)
        
