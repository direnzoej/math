# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:58:54 2018

@author: Evan
"""

# build a function to compute addition by recursion

def add(x, y):
    if y == 1:
        x += 1
        return x
    elif y > 1: return 1 + add(x, y - 1)
    elif y < 1: return -1 + add(x, y + 1)