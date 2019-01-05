#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:24:39 2018

@author: evan
"""
def fixed_point(x_0,eps,M=1000):
    '''Applies fixed point iteration to find x s.t. x = f(x) by looping.
    
    x_0 (int,flt): starting x value
    eps (flt, int): epsilon, the greatest tolerated interval length, > 0 
    M (int): maximum iterations allowed, def. set to 1000

    Prints iteration value, number, and current error.
    Returns an x (flt) s.t. x = f(x).
    '''
    import math
    def f(x):
        '''Returns the value of f(x) at the given x'''
        return 16*math.pi - math.atan(x)

    print(f'x_0 = {x_0}')
    n=0; error=1
    while error > eps and n < M:
        n += 1
        x_1 = f(x_0)
        error = abs(x_1 - x_0)
        print(f'x_n = {x_1} , iteration {n}, error = {error}')
        x_0 = x_1
        
    if error < eps: return x_1
    elif n == M:
        print(f'Max iterations reached: n = {n} = M')
        print('...Return last value...')
        return x_1
    else: 
        print(f'Unknown error ends series at iteration {n}')
        print(f'    error = {error} ...Return last value...')
        return x_1