#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:10:38 2018

@author: evan
"""
def Newtons_method(x_0,eps,tar=0):
    """Applies Newton's method of root-finding by recursion.
    
    x_0 (flt, int): starting x value
    eps (flt, int): epsilon, the greatest desired interval length, > 0 
    tar (flt, int): the function value sought by the interval - def. set to 0
    
        Returns a list of the interval endpoints (list of flts, len=2) 
    when the interval is less than the given epsilon.
    """
    #import math
    
    def f(x):
        """Defines the function to be used by Newton's method"""
#        return x**3-3*x**2+3*x-1
#        return x**6-x-1
        return (0.5/(1+x**4))-x
    
    def fp(x):
        """Defines the derivate of f to be used by Newton's method"""
#        return 3*x**2-6*x+3
#        return 6*x**5-1
        return ((-2*x**4)/((1+x**4)**(-2)))-1
    
    f_x = f(x_0)
    fp_x = fp(x_0)
    x_1 = x_0 - (f_x/fp_x)
    err = abs(x_1 - x_0)
    f_x_1 = f(x_1)
#    print([x_0,f_x,fp_x,x_1,err])#troubleshooting
    print('Interval:', [x_0,x_1])
    print('    error =', err, ', f(x_1) =', f_x_1)
    
    if err < eps:
        if x_1 > x_0: return [x_0,x_1]
        elif x_1 < x_0: return [x_1,x_0]
    else: return Newtons_method(x_1,eps,tar)
    
#    cont = input('Continue? (y/n):')
#    if cont == 'y':
#        if err < eps:
#            if x_1 > x_0: return [x_0,x_1]
#            elif x_1 < x_0: return [x_1,x_0]
#        else: return Newtons_method(x_1,eps,tar)
#    else: return None