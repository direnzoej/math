#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:01:32 2018

@author: evan
"""

def g(x):
    import math
    return ((1+4*x**2)**(-1) 
            - (0.8270182690 - 0.8203317303*x**2))**2

def S_n_f(n,f,a,b):
    '''Numerically approximates the definite integral of a function
    between given bounds by Simpson's composite method.
    
    n (int > 0): the number of composite integrals to use
    f (func): the function to be integrated (approx.)
    a (flt): the interval left endpoint
    b (flt): the interval right endpoint
    
    Returns a float of the approximate value of the definite integral.
    '''
    if n%2 != 0:
        n += 1
        print(f'n must be even...continuing with n = {n}')
        
    h = (b-a)/n
    nodes = [a+k*h for k in range(n+1)]
    S_sum=0
    for k in range(n+1):
        if k==0 or k==n:
            S_sum += f(nodes[k])
        elif k%2 == 1:
            S_sum += 4*f(nodes[k])
        elif k%2 == 0:
            S_sum += 2*f(nodes[k])
    
    return (h/3)*S_sum
