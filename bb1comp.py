import math
# import the bb1add and bb1mult function
from bb1add import bb1add 
from bb1mult import bb1mult
from sympy import symbols, binomial, expand, simplify


# -- xyz = outer curve of degree xyz_dg
# --  u = inner curve of degree  u_dg

def bb11comp(xyz, xyz_dg, u, u_dg, umx=None, xmx=None):
    
    if umx is None or xmx is None:
        umx = u_dg
        xmx = xyz_dg
    
    dg = u_dg * xyz_dg # the degree of the new curve
    # pat is used to store the coefficients of the resulting polynomial
    # while hh is used to store the control points of the resulting Bézier curve.
    pat = [0] * (dg + 1) # The i-th element of pat represents the coefficient of the term of degree i in the polynomial.
    hh = [0] * (dg + 1) # The i-th element of hh represents the control point of the Bézier curve that corresponds to the i-th term of the polynomial.
    U = [0] * (dg + 1)
    ww = [0] * (u_dg + 1)
    
    xyz_local = []
    for i in range(xyz_dg+1):
        xyz_local.append(xyz[i])
        
    mult = 0
    idg = 0
    
    U[0] = 1
    
    for i in range(u_dg + 1):
        ww[i] = 1 - u[i]
    
    for i in range(xmx + 1):
        idg = i * u_dg
        hh = list(U)
        pat_cof = []
        hh_cof = []

        
        for d in range(idg, dg, u_dg):
            hh = bb1mult(hh, d, ww, u_dg)
            
        mult = math.comb(xyz_dg, i)
        
        pat_cof.append(1)
        hh_cof.append(mult*xyz[i])
        
        # since I changed the bb1add function, I modified here as well.
        pat = bb1add(dg, pat, hh, pat_cof, hh_cof)
        if i < xyz_dg:
            U = bb1mult(U, idg, u, u_dg)
        
    return pat


test = 3
if test == 1:
    u_dg = 2
    u = [0, 1/2, 1]
    xyz_dg = 1
    xy = [symbols('xy_%d' % i) for i in range(xyz_dg + 1)]
    p = bb11comp(xy, xyz_dg, u, u_dg)
    print(p)
elif test == 2:
    u_dg = 1
    u = [0, 1/2]
    xyz_dg = 2
    xy = [symbols('xy_%d' % i) for i in range(xyz_dg + 1)]
    p = bb11comp(xy, xyz_dg, u, u_dg)
    print(p)
elif test == 3:
    u_dg = 2
    u = [0, 0, 1]
    xyz_dg = 2
    xy = [symbols('xy_%d' % i) for i in range(xyz_dg + 1)]
    p = bb11comp(xy, xyz_dg, u, u_dg, 1, 1)
    print("p", p)
    
    t = symbols('t')
    # Calculate p1
    mdg = u_dg * xyz_dg
    p1 = sum(p[l] * binomial(mdg, l) * (1 - t) ** (mdg - l) * t ** l for l in range(mdg + 1))
    print("p1", simplify(p1)) 

    # Calculate p2
    v = t ** 2
    p2 = sum(xy[k] * binomial(xyz_dg, k) * (1 - v) ** (xyz_dg - k) * v ** k for k in range(xyz_dg + 1))
    print("p2", simplify(expand(p2)))
