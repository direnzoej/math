def bisection(f,a,b,eps=1E-5,tar=0):
    '''Applies the bisection method by recursion to find 
    the root of a given function on a given interval.
    
    f (func): the function evaluated, which takes the 
                x-value as its only argument
    a (flt): interval left endpoint
    b (flt): interval right endpoint
    eps (flt): 'epsilon', the greatest tolerated interval 
                length, default set to 1E-5
    tar (flt): the function value sought on the interval,
                default set to 0 (roots mean f(x)=0...)
    
    Returns the interval containing the root when the 
    interval is smaller than the given epsilon.
    '''
    c = (a+b)/2 # find interval midpoint
    f_c = f(c) # evaluate f at midpoint
    
    if f_c == tar: # check for underflow
        print('Possible underflow error. [a,b] returned.')
        print(f'c = {c} and b - a = {b-a}')
        return [a,b]
    if f_c > tar: b = c # set right endpoint to midpoint OR
    if f_c < tar: a = c # set left endpoint to midpoint
    if b - a < eps: return [a,b] # return found solution
    else: return bisection(f,a,b,eps,tar) # recursion to solve
