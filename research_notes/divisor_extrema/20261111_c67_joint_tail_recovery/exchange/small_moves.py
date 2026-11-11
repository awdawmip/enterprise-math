"""Compare all two-gap templates that use one or two fives.
Run from any directory with --c66 pointing to C66/exchange.
"""
import argparse
import json
import sys
from pathlib import Path
from math import isqrt
import sympy as sp
from complete_exchange import dual,multiply,PRIMES,BOUND

R,C=sp.symbols('r c')
PAIRS=[((0,1),(1,0),0),((1,1),(2,0),2),((0,2),(1,1),0)]

def polys(r,c,s,t):
    def two(p):
        return multiply(dual(r,c,p[0]),dual(r-1,c-p[0],p[1]))
    a,b,h,d=two(s)
    e,f,g,i=two(t)
    return a*g-e*h,a*i+b*g-e*d-f*h,b*i-f*d,a*i+d*e-b*g-h*f

def core(expr,minimum):
    factors=[]
    coefficient, fs=sp.factor_list(expr)
    for f,n in fs:
        q=sp.Poly(f,R,C)
        if q.total_degree()>1:
            assert n==1
            factors.append(f)
        else:
            assert f.subs({R:2,C:minimum})>0 and min(q.coeff_monomial(R),q.coeff_monomial(C))>=0
    assert len(factors)==1
    return int(sp.sign(coefficient))*factors[0]

def nonscalar(s,t):
    a,_,c,_=polys(R,C,s,t)
    f,g=[core(v,2+sum(s)) for v in (a,c)]
    p=sp.Poly(sp.resultant(f,g,C),R).primitive()[1].shift(BOUND)
    assert min(p.all_coeffs())>0 or max(p.all_coeffs())<0
    return dict(core_degrees=[sp.Poly(x,R,C).total_degree() for x in (f,g)],resultant_degree=p.degree())

def high(s,t,off):
    from verify_exchange import newton
    vals=[[polys(2+x,4*(2+x)+off+y,s,t)[:3] for y in range(21)] for x in range(21)]
    counts=[]
    for idx in range(3):
        rows=[newton([-v[idx] for v in row]) for row in vals]
        arr=[a for j in range(21) for a in newton([row[j] for row in rows])]
        assert vals[0][0][idx]<0 and min(arr)>=0
        counts.append(sum(x>0 for x in arr))
    return counts

def finite(s,t,off):
    bits=4*BOUND+2
    tables=[]
    for p in PRIMES:
        sq={i*i%p for i in range(p)}
        rep=((1<<(p*((bits+p-1)//p)))-1)//((1<<p)-1)
        rows=[]
        for r in range(p):
            row=0
            for c in range(p):
                a,b,d,_=polys(r,c,s,t)
                if (b*b-4*a*d)%p in sq:row|=1<<c
            rows.append(rep*row)
        tables.append((p,rows))
    count=residual=0
    for r in range(2,BOUND):
        lo=max(r+2,2+sum(s))
        hi=4*r+off-1
        count+=hi-lo+1
        mask=(1<<(hi+1))-(1<<lo)
        for p,row in tables:mask &= row[r%p]
        while mask:
            bit=mask & -mask
            mask-=bit
            c=bit.bit_length()-1
            residual+=1
            a,b,d,_=polys(r,c,s,t)
            assert (a,b,d)!=(0,0,0),(s,t,r,c)
            if a*d>0 and a*b<0:
                disc=b*b-4*a*d
                assert disc<=0 or isqrt(disc)**2!=disc,(s,t,r,c)
    return dict(checked_stocks=count,residual=residual)

def run(c66):
    sys.path.insert(0,str(c66.resolve()))
    return [dict(pair=[s,t],high_offset=off,high_Newton_coefficients=high(s,t,off),
                 nonscalar=nonscalar(s,t),finite=finite(s,t,off)) for s,t,off in PAIRS]

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--c66',type=Path,required=True)
    print(json.dumps(run(ap.parse_args().c66),indent=2))
