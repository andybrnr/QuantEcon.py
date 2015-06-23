# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:31:51 2015

@author: ABerner
"""

from market import Market

def deadw(m):
    "Computes deadweight loss for market m."
    # == Create analogous market with no tax == #
    m_no_tax = Market(m.ad, m.bd, m.az, m.bz, 0)
    # == Compare surplus, return difference == #
    surp1 = m_no_tax.consumer_surp() + m_no_tax.producer_surp()
    surp2 = m.consumer_surp() + m.producer_surp() + m.taxrev()
    return surp1 - surp2
    
def __main__():
    baseline_params = 15, .5, -2, .5, 3
    m = Market(*baseline_params)
    print deadw(m)
    
__main__()