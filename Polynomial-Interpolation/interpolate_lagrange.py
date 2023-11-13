#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:30:34 2018

@author: evan
"""

def interpolate_lagrange( f, nodes, a=-1, b=1 ):
    ''' Interpolates a given function (f) by Lagrange's formula for n given nodes (nodes):
        P(x) = y_0*L_0 + ... + y_(n-1)*L_(n-1)
    
    f (func): the function being interpolated
    nodes (list[int,flt]): the nodes at which to interpolate
    a (flt): the left endpoint of the interpolation interval, def. set to -1
    b (flt): the right endpoint of the interpolation interval, def. set to 1
    
    Returns a list of polynomial coefficients for a polynomial in the form
     a_0 + a_1*x + a_2*x**2 + ... + a_n*x**n , ordered [a_0, ..., a_n].
    '''
    # foil_nodes is used to handle L numerators
    def foil_nodes( nodes ):
        ''' Foils a polynomial factorization to find the expanded form.
        
        nodes (list[ints,flts]): a list of values in form [a_0, a_1, ..., a_n] 
         representing polynomial factors in the form (x + a_i)
         
        Returns a list of polynomial coefficients for a polynomial in the form
         a_0 + a_1*x + a_2*x**2 + ... + a_n*x**n, ordered [a_0, ..., a_n].
        '''
        n = len(nodes)
        if n == 1:
            return [nodes[0], 1]
        # fill output with a_0, a_n, a_(n-1)
        coefs = [nodes[0]*nodes[1],nodes[0]+nodes[1],1]
        if n == 2:
            return coefs
        steps = {i:[] for i in range(n-1)}
        steps[0] = coefs[:]
        count = 1
        while count <= len(steps)-1:
            now_node = nodes[count+1]
            steps[count].append(steps[count-1][0]*now_node)
            for i in range(len(steps[count-1])-1):
                steps[count].append(now_node*steps[count-1][i+1]+
                     steps[count-1][i])
            steps[count].append(1)
            count += 1
        
        return steps[ len(steps)-1 ]
    #
    
    n=len(nodes)
    # find y-values
    ys=[f(node) for node in nodes]
    # find L denominators
    denoms={i:1 for i in range(n)}
    for key,value in denoms.items():
        temp = 1
        for k in range(n):
            if k == key: pass
            else: temp *= (nodes[key]-nodes[k])
        denoms[key] = temp
    # foil nodes to find L numerators
    numers={i:1 for i in range(n)}
    for key,value in numers.items():
        temp_nodes = []
        for k in range(n):
            if k == key: pass
            else: temp_nodes.append(-1*nodes[k])
        numers[key] = foil_nodes(temp_nodes)
    # calculate coefs from y/denom
    coefs=[0 for i in range(n)]
    for k in range(n):
        coefs[k]=ys[k]/denoms[k]
    # multiply coefs by terms in each L numer and sum
    output=[0 for i in range(n)]
    for j in range(n):
        for k in range(n):
            output[j] += numers[k][j]*coefs[k]
    #
    return output
#
