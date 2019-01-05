#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:16:59 2018

@author: evan
"""

def f(x):
    '''The function being interpolated.'''
    return (1+4*x**2)**(-1)

def least_sqrs_aprx(n,f,a=-1,b=1):
    '''Finds a least-squares approximation of a given function using
    Legendre polynomials and Simpsons composite method of numerical 
    integration.
     
     n (int > 0): the degree of the desired approx. polynomial
     f (func): the function being approximated
     a (flt): left endpoint of the approximation interval, def. set to -1
     b (flt): right endpoint of the approximation interval, def. set to 1
        
    Returns a list of polynomial coefficients for a polynomial in the form
     a_0 + a_1*x + a_2*x**2 + ... + a_n*x**n , ordered [a_0, ..., a_n].
    '''
    def legendre_Ps(n):
        '''Returns a dictionary of lists representing coefficients of 
        the Legendre polynomials to degree n (int >= 0)'''
        P={0:[1],1:[0,1]}
        if n > 1:
            for j in range(1,n):
                p = [0] + P[j][:]
                for k in range(len(p)):
                    p[k] *= (2*j+1)/(j+1)
                p_1 = P[j-1][:]
                for k in range(len(p_1)):
                    p_1[k] *= j/(j+1)
                for i in range(len(p_1)):
                    p[i] -= p_1[i]
                P[j+1] = p[:]
                
        return P
        #
    #
    def S_n_f(n,f,g,a,b):
        '''Numerically approximates the definite integral of a function
        between given bounds by Simpson's composite method.
        
        n (int > 0): the number of composite integrals to use
        f (func): the function to be integrated (approx.)
        g (list): a polynomial represented by a list of coefficients
        a (flt): the interval left endpoint
        b (flt): the interval right endpoint
        
        Returns a float of the approximate value of the definite integral.
        '''
        if n%2 != 0:
            n += 1
        
        def eval_coef_poly(g,x):
            g_num=0
            for i in range(len(g)):
                g_num += g[i]*x**i
            return g_num
                
        h = (b-a)/n
        nodes = [a+k*h for k in range(n+1)]
        S_sum=0
        for k in range(n+1):
            g_k = eval_coef_poly(g,nodes[k])
            if k==0 or k==n:
                S_sum += f(nodes[k])*g_k
            elif k%2 == 1:
                S_sum += 4*f(nodes[k])*g_k
            elif k%2 == 0:
                S_sum += 2*f(nodes[k])*g_k
        
        return (h/3)*S_sum
        #
    # get a dictionary of legendre polynomials
    # represented as lists of coefficients
    Ps = legendre_Ps(n)
    # get a list of values from inner products (f,P_j)
    numers = [S_n_f((b-a)*10**3,f,Ps[j],a,b) for j in range(n+1)]
    # get a list of values from inner products (P_j,P_j)
    denoms = [2/(2*j+1) for j in range(n+1)]
    # set a temporary dictionary to hold polynomials
    temps={j:[] for j in range(n+1)}
    for j in range(n+1):
        coef = (numers[j]/denoms[j])
        for i in range(len(Ps[j])):
            temps[j].append(coef*Ps[j][i])
    # sum the coefs of each degree term to the ouput polynomial        
    output=[0 for j in range(n+1)]
    for key,value in temps.items():
        for j in range(len(value)):
            output[j] += value[j]
            
    return output            