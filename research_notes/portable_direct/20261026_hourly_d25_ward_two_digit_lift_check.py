#!/usr/bin/env python3
"""All-prime p^2 Green quotient factorisation checker, author-only.

Reuse the immediately preceding author's exact labelled corrected-Hasse input.
"""
import importlib.util
from pathlib import Path
from fractions import Fraction as Q

prior = Path(__file__).with_name('20261026_hourly_d25_ward_factorial_boundary_r11_check.py')
spec = importlib.util.spec_from_file_location('prior_d25_ward', prior)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def correction(m, t):
    N = 2*m-1
    return Q(1,2*N+1)-Q(1,2*t+1)+sum((Q(1,2*r-1)-Q(1,2*r) for r in range(t+1,N+1)),Q(0))


def check(m):
    p = 6*m+1
    assert base.is_prime(p)
    N=2*m-1
    f=base.F(m)
    count=0
    for t in range(N):
        observed = base.coeff(m,-t-1)/p
        predicted = -f*base.C(t)/Q(2*t+1)*(1+p*correction(m,t))
        assert base.residue(observed-predicted,p*p)==0, (m,t,'negative factor')
        count+=1
    assert base.residue(base.all_product(m)/p+f*base.C(N)*(1+Q(p,2*N+1)),p*p)==0
    count+=1
    _,u=base.jets(m)
    G=base.moments(p,m,u)
    rows=[]
    for a,b in base.CHANNELS:
        S={n:base.source(m,p,u,G,n,a,b) for n in range(1-2*m,2*m)}
        edge=G(a,b,1-2*m,1)-Q(p-(1-2*m),2)*G(a,b,1-2*m)
        direct=sum((base.coeff(m,h)*S[h] for h in range(2*m)),Q(0))/(p*f)
        zeroth=sum((base.C(t)*S[-t-1]/Q(2*t+1) for t in range(N)),Q(0))-base.C(N)*edge
        first=sum((base.C(t)*S[-t-1]/Q(2*t+1)*correction(m,t) for t in range(N)),Q(0))-base.C(N)*edge/Q(2*N+1)
        assert base.residue(direct-zeroth-p*first,p*p)==0, (m,a,b,'source quotient')
        count+=1
        rows.append((a,b,base.residue(zeroth,p*p),base.residue(first,p),base.residue(direct,p*p)))
    if p==13:
        assert rows==[(0,2,141,2,167),(1,2,111,0,111),(0,3,97,8,32)]
        count+=1
    return p,count,rows


def main():
    total=0
    for m in range(1,13):
        p=6*m+1
        if not base.is_prime(p):
            continue
        _,n,rows=check(m)
        total+=n
        print('m=',m,'p=',p,'PASS=',n,'rows=',rows if p==13 else '<computed>')
    print('ALL PASS=',total)


if __name__ == '__main__':
    main()
