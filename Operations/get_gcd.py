# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# greatest common divisor

def get_gcd(a,b):
    """a, b: integers
    
    Returns the greatest positive integer 
    which is a common divisor of a and b."""
    if type(a) != int or type(b) != int:
        print('Input must be at least two integers...Return None')
        return None
    if abs(a) < abs(b):
        temp = b; b = a; a = temp

    def div_algo(a,b):
    	# a = bq + r
        q = a//b; r = a%b
        if q < 0: q += 1
        if r < 0: r *= 1
        return a,b,q,r
    
    a,b,q,r = div_algo(a,b)
    
    if r == 0:
        return b
    if r != 0:
        return get_gcd(b,r)       
