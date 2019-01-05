def bisection(a,b,eps,tar=0):
    def f(x):
        """Defines the function to be used by bisection"""
        return -1+3*x-3*x**2+x**3
            
    c = (a+b)/2
    f_c = f(c)
    print([a,b,c,f_c])#troubleshooting
    if f_c == tar:
        print('Possible underflow error. [a,b] returned.
        print('c =', c,'and b - a =', b-a)
        return [a,b]
    if f_c > tar: b = c
    if f_c < tar: a = c
    if b - a < eps: return [a,b]
    else: return bisection(a,b,eps,tar)
            
