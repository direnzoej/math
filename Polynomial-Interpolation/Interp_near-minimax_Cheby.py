#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:09:06 2018

@author: evan
"""
def near_minimax(n,a=-1,b=1):
    '''Finds a near-minimax approximation of a given function (defined below)
    by Chebyshev nodes and Newton's divided differences interpolation method.
        
     n (int > 0): the degree of the desired approx. polynomial
     a (flt): left endpoint of the approximation interval, def. set to -1
     b (flt): right endpoint of the approximation interval, def. set to 1
        
    Returns a list of polynomial coefficients for a polynomial in the form
     a_0 + a_1*x + a_2*x**2 + ... + a_n*x**n , ordered [a_0, ..., a_n].
    '''
    import math
    def f(x):
        '''The function being interpolated.'''
        return math.e**x
    # find n+1 Chebyshev nodes
    nodes = [math.cos(math.pi*(2*j+1)/(2*n+2)) for j in range(0,n+1)]
    # transform nodes to new interval if necessary
    if a != -1 or b != 1:
        old_nodes = nodes.copy()
        for node in old_nodes:
            node = (1/2)*(b+a+node*(b-a))
    # calculate Newton's divided differences for given nodes
    def div_diffs(nodes):
        '''Calculates the divided differences for Newton's interpolation
        formula using recursion.
         
         nodes (list): x values of interpolation points
        
        Returns a list of the divided differences, in order.
        '''
        ys=[f(node) for node in nodes]
        def get_dd(nodes,ys):
            if len(nodes) == 1:
                return ys[0]
            elif len(nodes) == 2:
                return (ys[1]-ys[0])/(nodes[1]-nodes[0])
            elif len(nodes) > 2:
                return (get_dd(nodes[1:],ys[1:])-
                        get_dd(nodes[0:-1],ys[0:-1]))/(nodes[-1]-nodes[0])
                
        return [get_dd(nodes[0:n+1],ys[0:n+1]) for n in range(len(nodes))]
    # expand the factorizations of given nodes
    def foil_nodes(nodes):
        '''Foils a polynomial factorization to find the expanded form.
        
        nodes (list)(ints,flts): a list of values in form [a_0, a_1, ..., a_n] 
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
        
        return steps[len(steps)-1]
    # find the divided differences for the Chebyshev nodes
    dds = div_diffs(nodes)
    # pad the coefficients list with zeros
    coefs = [0 for i in range(n+1)]
    # loop over terms, summing into coefficients list
    for i in range(n+1):
        if i == 0:
            coefs[0] = dds[0]
        else:
            chi = foil_nodes([-1*node for node in nodes[0:i]])
            for k in range(len(chi)):
                coefs[k] += dds[i] * chi[k]

    return coefs