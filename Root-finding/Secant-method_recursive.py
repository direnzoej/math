#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:10:38 2018

@author: evan
"""
def secant_method(x_0,x_1,eps,M=1000,tar=0):
    """Applies the secant method of root-finding by recursion.
    
    x_0,x_1 (flt, int): starting x values
    eps (flt, int): epsilon, the greatest desired interval length, > 0
    M (int): maximum iterations allowed
    tar (flt, int): the function value sought by the interval - def. set to 0
    
        Returns a list of the interval endpoints (list of flts, len=2) 
    when the interval is less than the given epsilon.
    """
    import math
    
    def f(x):
        """Defines the function to be used by the secant method"""
#        return x**3-x**2-x-1
#        return x - math.e**(-x)#uncomment line 19: import math
#        return x**6-x-1
#        return x**3-3*x**2+3*x-1
#        return -1+3*x-3*x**2+x**3
#        return -1+x*(3+x*(-3+x))
#        return math.e**(-x)-x
        return (0.5/(1+x**4))-x
    
    #each secant is performed through and object
    class secant():
        #track method iterations
        iterations = 0
        def __init__(self,x_0,x_1):
            secant.iterations += 1
            self.x_0=x_0;self.x_1=x_1
            self.f_x_0 = f(x_0); self.f_x_1 = f(x_1)
            try:
                self.x_2 = x_1-((x_1-x_0)/(self.f_x_1-self.f_x_0))*(self.f_x_1)
                self.f_x_2 = f(self.x_2); self.err = abs(self.x_2 - self.x_1)
                if self.x_2 >= self.x_1: self.interval = [self.x_1,self.x_2]
                elif self.x_1 > self.x_2: self.interval = [self.x_2,self.x_1]
            except ZeroDivisionError:
                self.interval = [x_0,x_1]; self.err = abs(x_1-x_0)
                self.f_x_2 = None

        def __str__(self):
            #print intervals and iteration
            return f'Interval: {self.interval}, iteration {secant.iterations}'
        
    def get_output(x_0,x_1,eps,M,tar):
        #recursive loop to solve for the intersection using secant objects
        iteration = secant(x_0,x_1); err = iteration.err
        print(iteration)
        print(f'    error = {err}, f(x_2) = {iteration.f_x_2}')
        if err < eps: return iteration.interval
        elif secant.iterations == M:
            print(f'Max iterations reached: n = {M} = M')
            return iteration.interval
        elif iteration.f_x_2 == None:
            print('Division by zero: f(x_1)-f(x_0) ~= 0.0 ...')
            print('...Return last interval...')
            return iteration.interval
        else: return get_output(x_1,iteration.x_2,eps,M,tar)

    return get_output(x_0,x_1,eps,M,tar)