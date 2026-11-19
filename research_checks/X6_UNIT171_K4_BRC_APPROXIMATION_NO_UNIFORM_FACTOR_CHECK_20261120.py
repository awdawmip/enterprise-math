"""Exact integer check of Unit171 paired K4 residual fibers.

This is an independent finite check, not the original R063 benchmark.
The universal theorem is proved separately by factorial algebra.
"""
import json
from math import factorial, comb
from fractions import Fraction


def incidence(v):
    a, b, c, d = v
    return (a+b, a+c, a+d, b+c, b+d, c+d)


def observation(x):
    a, b, c, d, e, f = x
    return (a+f, b+e, (a+b+c) % 2)


def native_brc(x):
    n = sum(abs(u) for u in x)
    result = factorial(n)
    for u in x:
        result //= factorial(abs(u))
    return result


def independent_brc(x):
    length = 0
    result = 1
    for u in x:
        k = abs(u)
        result *= comb(length+k, k)
        length += k
    return result


def check(m):
    va=(-3*m,0,0,3*m)
    vb=(3*m,m,-2*m,-2*m)
    a=incidence(va)
    b=incidence(vb)
    if a != (-3*m,-3*m,0,0,3*m,3*m):
        raise RuntimeError('incidence_A')
    if b != (4*m,m,m,-m,-m,-4*m):
        raise RuntimeError('incidence_B')
    oa,ob=observation(a),observation(b)
    la,lb=sum(map(abs,a)),sum(map(abs,b))
    qa,qb=sum(u*u for u in a),sum(u*u for u in b)
    if not (oa==ob==(0,0,0) and la==lb==12*m and qa==qb==36*m*m):
        raise RuntimeError('observation')
    ba,bb=native_brc(a),native_brc(b)
    if ba!=independent_brc(a) or bb!=independent_brc(b):
        raise RuntimeError('brc independent')
    ratio=Fraction(bb,ba)
    product=Fraction(1)
    for i in range(1,m+1):
        factor=Fraction((m+i)*(2*m+i),i*(3*m+i))
        if factor < Fraction(3,2):
            raise RuntimeError('factor lower bound')
        product *= factor
    if ratio!=product**2 or ratio < Fraction(9,4)**m:
        raise RuntimeError('factorial identity/bound')
    return {'m':m,'L':la,'Q':qa,'B_A':str(ba),'B_B':str(bb),
            'ratio_num':str(ratio.numerator),'ratio_den':str(ratio.denominator),
            'lower_bound_numerator':str(9**m),'lower_bound_denominator':str(4**m)}


def main():
    samples=[check(m) for m in range(1,33)]
    print(json.dumps({'schema':'X6_UNIT171_EXACT_INTEGER_CHECK_V1',
     'scope':'m=1..32; independent factorial and comb interleaving; no native R063 rerun',
     'pairs_checked':len(samples),'violations':0,'samples':[samples[i-1] for i in [1,2,3,8,16,32]]},
     ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
