# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:58:54 2018

@author: Evan
"""
def add(x, y):
    '''Adds two integers by recursion.
    
    x, y (int): the integers to add
    
    Returns an integer.
    '''
    if y == 1: # base case
        x += 1
        return x
    # addition and subtraction recursions
    elif y > 1: return 1 + add(x, y-1)
    elif y < 1: return -1 + add(x, y+1)
