from sympy import symbols, binomial

def bb1mult(b1, d1, b2, d2, lo=None, hi=None):
    """
    Multiply two univariate polynomials in BB-form

    Arguments:
    b1 -- array of coefficients of polynomial 1
    d1 -- degree of polynomial 1
    b2 -- array of coefficients of polynomial 2
    d2 -- degree of polynomial 2
    lo -- (optional) lower index of vectors for component-wise multiplication
    hi -- (optional) upper index of vectors for component-wise multiplication

    Returns:
    out -- array of coefficients of the product polynomial in BB-form
    """

    dgout = d1 + d2
    out = [0] * (dgout + 1)

    if lo is None or hi is None:
        for i1 in range(d1 + 1):
            for i2 in range(d2 + 1):
                mult = binomial(d1, i1) * binomial(d2, i2) / binomial(d1 + d2, i1 + i2)
                out[i1 + i2] += mult * b1[i1] * b2[i2]
    else:
        for i1 in range(d1 + 1):
            for i2 in range(d2 + 1):
                mult = binomial(d1, i1) * binomial(d2, i2) / binomial(d1 + d2, i1 + i2)
                h = sum(b1[m][i1] + b2[m][i2] for m in range(lo, hi + 1))
                out[i1 + i2] += mult * h

    return out

# Test
test = 1
if test == 1:
    dg1 = 2
    dg2 = 1
    b1 = [symbols('b1_%d' % i) for i in range(dg1 + 1)]
    b2 = [1,1]
    bb = bb1mult(b1, dg1, b2, dg2)
    print(bb)
