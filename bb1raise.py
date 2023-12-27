import sympy
# This routine raises the degree of a Bezier curve by 1. 
#
# Basic idea: 
# (d+1 choose i)  P[i,d+1-i] =
#   (d choose i-1) P[i-1,d+1-i]+ (d choose i) P[i,d-i]
#
# divide by (d+1 choose i) yields
# P[i,_] = (i*P[i-1,_]+(d+1-i)*P[i,_])/(d+1) 

# d -- input degree in the u,v directions respectively

def bb1raise(bb,d):
    
    d1 = d+1 # coefficients = degree + 1
    
    bb1 = [0] * (d1) # bb raise degree to get bb1 
    
    for i in range(d1): # range(d1+1) = 0...d1
        if 0 < i:
            bb1[i] += i * bb[i-1] /d1
        if i <= d:
            bb1[i] += (d1 - i) * bb[i] /d1
            
    return bb1




test = 0
if test == 1:
    d = 2 # degree
    bb = [sympy.symbols('b1_%d' % i) for i in range(d+1)]
    bb1 = bb1raise(bb,d)
    print(bb1)
