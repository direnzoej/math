#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:10:29 2018

@author: evan
"""
def bisection(a,b,eps,tar=0):
    """Applies the bisection method of root-finding by recursion.
    
    a (flt, int): interval left endpoint
    b (flt, int): interval right endpoint
    eps (flt, int): epsilon, the greatest desired interval length, < 0 
    tar (flt, int): the function value sought by the interval - def. set to 0
    
        Returns a list of the interval endpoints (list of flts, len=2) 
    when the interval is less than the given epsilon.
    """
    def f(x):
        """Defines the function to be used by bisection"""
        return x**3-x**2-x-1
    
    c = (a+b)/2
    f_c = f(c)
    print('Interval =', [a,b])
    print('    c =', c, 'f(c) =',f_c)
    
    if f_c > tar: b = c
    if f_c < tar: a = c
    if f_c == tar:
        print('Possible underflow error...Return [a,b]')
        print('c =', c,', f(c) =', f_c,', and b - a =', b-a)
        return [a,b]
    if b - a < eps: return [a,b]
    else: return bisection(a,b,eps,tar)