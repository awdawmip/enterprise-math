"""Sharp seven-sample cutoffs for common integer numerator/denominator errors."""
from fractions import Fraction
from itertools import product
from math import lcm
import json

SIGNATURE = (20, 20, 20, -100, 140, -100)
CODES = [tuple(SIGNATURE[(a+j) % 6] for j in range(3)) for a in range(6)]
W = (1, -4, 6, -4, 1)


def counts(end):
    exact = [1] + [0] * end
    for weight in (1, 1, 1, 2, 3, 6):  # Five named sources plus the slack variable.
        for n in range(weight, end+1):
            exact[n] += exact[n-weight]
    c = [0] + exact
    t = [0]
    for count in c[:-1]:
        t.append(t[-1] + count)
    return c, t


def multiply_linear(poly, low, high):
    out = [0] * (len(poly)+1)
    for i, value in enumerate(poly):
        out[i] += low*value
        out[i+1] += high*value
    return out


def tail_polynomial(q, c, t, e, k, sign):
    # Substitute d=k(x-1)/(1+x), x>=0. Read x=infinity for d=+k.
    factors = [(c[n]-k, c[n]+k) for n in range(q,q+5)]
    constant = 60 - sign*(4+SIGNATURE[q % 6])
    out = [constant]
    for low, high in factors:
        out = multiply_linear(out,low,high)
    for j, weight in enumerate(W):
        n = q+j
        p = [sign*weight*n**3*(t[n]+e)]*2  # factor (1+x)
        for i, (low, high) in enumerate(factors):
            if i != j:
                p = multiply_linear(p,low,high)
        out = [a+b for a,b in zip(out,p)]
    return out


def certify_tail(c,t,m,k,start):
    # On q=q0+6n each coefficient in x is polynomial in n, degree <=29.
    for q0,e,sign in product(range(start,start+6),sorted({-m,m}),(-1,1)):
        if c[q0] <= k:
            return False
        values = [tail_polynomial(q0+6*n,c,t,e,k,sign) for n in range(31)]
        for seq in zip(*values):
            row = list(seq)
            if row[0] <= 0:
                return False
            for _ in range(30):
                row = [b-a for a,b in zip(row,row[1:])]
                if row[0] < 0:
                    return False
            assert row == [0]  # additionally cross-check the degree bound
    return True


def first_failure(c,t,r,m,k):
    phase = r % 6
    true = CODES[phase]
    # Try strongest denominator errors first. Remaining integer values are exhaustive.
    for d in dict.fromkeys([-k,k,*range(-k+1,k)]):
        den = [c[n]+d for n in range(r,r+7)]
        if min(den) <= 0:
            continue
        scale = lcm(*den)
        slopes = [n**3*(scale//den[n-r]) for n in range(r,r+7)]
        bases = [slopes[i]*t[r+i] for i in range(7)]
        z0 = [sum(w*x for w,x in zip(W,bases[j:]))-4*scale for j in range(3)]
        z1 = [sum(w*x for w,x in zip(W,slopes[j:])) for j in range(3)]
        if all(abs(z-p*scale)+m*abs(slope)<60*scale for z,slope,p in zip(z0,z1,true)):
            continue
        for rival,code in enumerate(CODES):
            if rival == phase:
                continue
            for h,sgn in product(range(3),(-1,1)):
                # Require every signed rival residual <= this signed true residual.
                lo, hi = -m,m
                for i,side in product(range(3),(-1,1)):
                    coef = side*z1[i]-sgn*z1[h]
                    rhs = sgn*(z0[h]-true[h]*scale)-side*(z0[i]-code[i]*scale)
                    if coef > 0:
                        hi = min(hi,rhs//coef)
                    elif coef < 0:
                        lo = max(lo,-((-rhs)//coef))
                    elif rhs < 0:
                        hi = lo-1
                    if lo > hi:
                        break
                if lo <= hi:
                    z = [a+lo*b for a,b in zip(z0,z1)]
                    ds = [Fraction(max(abs(x-scale*y) for x,y in zip(z,w)),scale) for w in (true,code)]
                    assert ds[1] <= ds[0]
                    return dict(r=r,phase=phase,rival=rival,e=lo,d=d,
                                true_distance=str(ds[0]),rival_distance=str(ds[1]))
    return None


def solve(m,k):
    start=32
    while True:
        c,t=counts(start+200)
        if certify_tail(c,t,m,k,start):
            break
        start*=2
    for r in range(start-1,0,-1):
        bad=first_failure(c,t,r,m,k)
        if bad:
            return dict(M=m,K=k,N=r+1,certified_tail=start,witness=bad)
    return dict(M=m,K=k,N=1,certified_tail=start,witness=None)


if __name__=='__main__':
    cases = [(0,0),(0,2),(2,2),(0,10),(0,100),(0,1000),
             (10,10),(100,100),(1000,100),(1000000,0),(1000000,100)]
    print(json.dumps([solve(m,k) for m,k in cases], indent=2))
