#!/usr/bin/env python3
"""GH-111 exact low-degree Frobenius factors at R_3347(z)=0.

Depends only on the sibling GH-110 independently reconstructed source program.
Arithmetic is entirely over F_3347. No native EM execution or formal admission.
"""
from d25_gh110_p3347_zero_fiber_s1673 import (
    P, D, reflected_R, trim, gcd, derivative, modulus
)

r = reflected_R()[D+1:]

def divide_linear(a, root):
    b = [0] * (len(a)-1)
    b[-1] = a[-1]
    for i in range(len(b)-2, -1, -1):
        b[i] = (a[i+1] + root*b[i+1]) % P
    assert (a[0] + root*b[0]) % P == 0
    return b

# Remove the exactly known double root z=9 and large zero z=0.
Q = divide_linear(divide_linear(r, 9), 9)
assert len(Q)-1 == 834 and gcd(Q, derivative(Q)) == [1]
Q = [(a*pow(Q[-1], -1, P)) % P for a in Q]


def mulmod(a, b):
    out = [0] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                out[i+j] += x*y
    out = [z % P for z in out]
    for k in range(len(out)-1, len(Q)-2, -1):
        c = out[k]
        if c:
            offset = k-(len(Q)-1)
            for j in range(len(Q)-1):
                out[offset+j] = (out[offset+j]-c*Q[j]) % P
    return trim(out[:len(Q)-1])


def power_mod(a, n):
    out = [1]
    while n:
        if n & 1:
            out = mulmod(out,a)
        n >>= 1
        if n:
            a = mulmod(a,a)
    return out


def divide_monic(a, b):
    a, b = trim(a), trim(b)
    v = a[:]
    inv = pow(b[-1],-1,P)
    quotient = [0]*(len(a)-len(b)+1)
    for k in range(len(quotient)-1, -1, -1):
        c = v[k+len(b)-1]*inv % P
        quotient[k] = c
        if c:
            for j,x in enumerate(b):
                v[k+j] = (v[k+j]-c*x) % P
    assert all(x==0 for x in v[:len(b)-1])
    return trim(quotient)


def main():
    expected = {1:0,2:0,3:0,4:0,5:5,6:0,7:0,8:0,9:0,10:15,11:11,12:0}
    frob = [0,1]
    factors = {}
    for k in range(1,13):
        frob = power_mod(frob,P)
        x = frob[:]
        if len(x)<2:
            x += [0] * (2-len(x))
        x[1] = (x[1]-1) % P
        factors[k] = gcd(Q,x)
        assert len(factors[k])-1 == expected[k], (k,len(factors[k])-1)
    f5 = factors[5]
    f10 = divide_monic(factors[10],f5)
    f11 = factors[11]
    assert (len(f5),len(f10),len(f11)) == (6,11,12)
    for f in (f5,f10,f11):
        assert modulus(Q,f) == [0]
    assert f5 == [2592,980,2615,2622,1784,1]
    assert f10 == [3295,1706,2801,2889,2143,3308,2998,2805,557,3178,1]
    assert f11 == [1639,1293,1437,1494,324,2374,1556,3110,1714,1336,448,1]
    print('PASS_GH111_FROBENIUS_DEGREES',expected)
    print('EXACT_IRREDUCIBLE_FACTOR_DEGREE_5',f5)
    print('EXACT_IRREDUCIBLE_FACTOR_DEGREE_10',f10)
    print('EXACT_IRREDUCIBLE_FACTOR_DEGREE_11',f11)
    print('ALL PASS')

if __name__ == '__main__':
    main()
