#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:24:52 2018

@author: evan
"""
def div_diffs(nodes,ys=None):
    '''Calculates the divided differences for Newton's interpolation formula.
    Uses recursion.
    
    nodes (list): the list of x values to be used for interpolation, in order
    ys (list): the list of y values corresponding to each node, in order, def
        set to None (if ys == None, function will calculate ys based on a
        a given function defined below)
    
    Returns a list of the divided differences, in order.
    '''
    if ys == None:
        import math
        def f(x):
            '''The function to evaluate at each node'''
            return math.e**x
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