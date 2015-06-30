# -*- coding: utf-8 -*-
"""
Filename: QuantEcon_Exercises_Ch1Sec6.py
Created on Wed Jun 24 08:23:13 2015

@author: ABerner
"""


# Ex1

def FibCalc(t):
    """
    Calculate the t-th Fibonacci number recursively
    """    
    def FibRecur(t0,tm1,l,t):    
        if l<t-1:
            return FibRecur(t0+tm1,t0,l+1,t)
        else: 
            return t0
    
    t0=1
    tm1=0
    l=0
    if t==0:
        return tm1
    elif t==1:
        return t0
    else:
        return FibRecur(t0,tm1,l,t)

 
# Ex2    
    
readpath = "C:\\Users\\andrewb\\Documents\\GitHub\\QuantEcon.py\\solutions\\"
filename = "test_table.csv"
filepath = readpath+filename
from csv import reader

def column_iterator(target_file, column_number):
    """A generator function for CSV files.
    When called with a file name target_file (string) and column number
    column_number (integer), the generator function returns a generator
    that steps through the elements of column column_number in file
    target_file.
    """
    # put your code here
    f = open(filepath)
    nikkei_data = reader(f)
    while nikkei_data:
        yield nikkei_data.next()[column_number]
    
dates = column_iterator('test_table.csv', 0)

for date in dates:
    print date


# Ex3   
