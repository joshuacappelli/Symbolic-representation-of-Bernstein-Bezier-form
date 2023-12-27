from sympy import symbols
def bb1_sub(b, bl, br, dg, s):

# dg: degree
    b_local = [0]*(dg+1)
    for i in range(dg+1):
        b_local[i] = b[i]
    l=0
    bl[l] = b_local[0]
    br[dg-l] = b_local[dg-l]
    for l in range(1,dg+1):
        for i in range(dg+1-l): # for layer 1 to dg
            b_local[i] = (1-s)*b_local[i] + s*b_local[i+1]
        bl[l] = b_local[0]
        br[dg-l] = b_local[dg-l]  

    return b_local



dg = 2
bb = [symbols('bb_%d' % i) for i in range(dg + 1)]
# initialize b1 and b2
b1 = [0] * (dg+1)
b2 = [0] * (dg+1)
out = bb1_sub(bb,b1,b2,dg,1/2)
print(out)
print()
print(b1)
print(b2)