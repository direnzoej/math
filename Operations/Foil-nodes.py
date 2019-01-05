#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:04:27 2018

@author: evan
"""
def foil_nodes(nodes):
    '''Foils a polynomial factorization to find the expanded form.
    
    nodes (list)(ints,flts): a list of values in form [a_0, a_1, ..., a_n] 
     representing polynomial factors in the form (x + a_i)
     
    Returns a list of polynomial coefficients for a polynomial in the form
     a_0 + a_1*x + a_2*x**2 + ... + a_n*x**n, ordered [a_0, ..., a_n].
    '''
    if type(nodes) != list:
        print('Input to foil_nodes must be a list...Return None')
        return None
    
    n = len(nodes)
    if n == 0:
        print('Input empty list...Return None')
        return None
    for entry in nodes:
        if type(entry) != int and type(entry) != float:
            print('Factors must be integers or floats...Return None')
            return None
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