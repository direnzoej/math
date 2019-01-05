# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:10:37 2018

@author: Evan
"""

# write a function to perform recursive multiplication

def mult(x,y):
    if y == 1:
        return x
    elif y > 1:
        return x + mult(x, y - 1)
    elif y < 1:
        return -x + mult(x, y + 1) 