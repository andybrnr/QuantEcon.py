# -*- coding: utf-8 -*-
"""
Filename: QuantEcon_Exercises_Ch1Sec5
Created on Tue Jun 23 13:16:26 2015
@author: ABerner
"""

#Ex 1:

class ECDF:
    
    def __init__(self, observations):
        """
        Set up instance
        """
        self.observations = observations
        
    def __call__(self,x):
        return 1/len(self.observations)*sum([xi <= x for xi in self.observations])

#Ex 2:

class Polynomial:
    
    def __init__(self, coeff):
        """
        Set up instance. Expect coeff
        """
        self.coeff = coeff
        
    def __call__(self, x):
        res = 0
        for n,a in enumerate(self.coeff):
            res = res+a*x**n
        return res
        
    def d(self, x, D):
        """
        Calculate the arbitrary derivative of 
        """
        if not ((type(D) is int) and (D>=0)):
            print "derivative not defined"
            return False
        else:
            tmpD = D
            tmpCoeff = self.coeff
            while tmpD > 0:
                tmpD-=1
                tmpCoeff = [tmpCoeff[i]*range(0,len(tmpCoeff))[i] for i in range(1,len(tmpCoeff))]
                pp = Polynomial(tmpCoeff)
            return pp(x)