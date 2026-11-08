#!/usr/bin/env python3
"""Exact original W216 low-valuation block, terminating Legendre bridge and two jets.

All computations exact in Z/(p^3), for p=6m+1>3.  Source pin unchanged.
"""
from math import comb
from pathlib import Path
import json

P=[7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373]

def legendre_even_weighted(N,q):
    """Evaluate P_N(s)^2 - 3 P_N(s) P_N'(s)/s, with s^2=1/2 and N even."""
    inv2=pow(2,-1,q)
    def s_mul(x):return (x[1]*inv2%q,x[0])
    def add(x,y):return ((x[0]+y[0])%q,(x[1]+y[1])%q)
    def scale(t,x):return (t*x[0]%q,t*x[1]%q)
    if N==0:return 1
    p0,p1=(1,0),(0,1)
    d0,d1=(0,0),(1,0)
    for n in range(1,N):
        inv=pow(n+1,-1,q)
        pn=scale(inv,add(scale(2*n+1,s_mul(p1)),scale(-n,p0)))
        dn=scale(inv,add(scale(2*n+1,add(p1,s_mul(d1))),scale(-n,d0)))
        p0,p1,d0,d1=p1,pn,d1,dn
    assert p1[1]==0 and d1[0]==0,(N,p1,d1)
    a,b=p1[0],d1[1]
    return (a*a-3*a*b)%q

def certify(p):
    assert p>3 and p%6==1
    m=(p-1)//6;N=2*m;q=p**3
    base=first=second=0
    R=1; H1=H2=0
    for n in range(N+1):
        w=(6*n+1)%q
        base=(base+w*R)%q
        first=(first+w*R*H1)%q
        second=(second+w*R*(H1*H1+H2))%q
        if n==N:break
        invA=(9*pow((3*n+1)*(3*n+2),-1,q))%q
        H1=(H1+invA)%q; H2=(H2+invA*invA)%q
        R=(R*(2*n+1)*(n-N)*(n+N+1)*pow(4*(n+1)**3,-1,q))%q
    z=p*(p+1)*pow(9,-1,q)%q
    predicted=(base+z*first+(z*z*pow(2,-1,q)%q)*second)%q
    W0=sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,q) for n in range(N+1))%q
    L=legendre_even_weighted(N,q)
    assert base==L,(p,'Legendre',base,L)
    assert W0==predicted,(p,'W0',W0,predicted)
    return {'p':p,'m':m,'N':N,'p3':q,'original_W_grade0':W0,
            'terminating_base':base,'legendre_closed_base':L,
            'first_moment':first,'second_moment':second,
            'deformation_z':z,'first_correction':z*first%q,
            'second_correction':z*z*pow(2,-1,q)*second%q,'check':True}

def main():
    out={'schema':'EM_D25_TERMINATING_LEGENDRE_TWO_JET_V1',
        'source_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
        'status':'AUTHOR_SIDE_EXACT_FINITE/UNREVIEWED/NOT_ADMITTED/NOT_NATIVE',
        'scope':'The identities are for every p=6m+1>3; finite checks are the 18 listed primes.',
        'checks':[certify(p) for p in P]}
    path=Path(__file__).with_name('d25_original_w216_terminating_legendre_results_20261109.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',len(P))
    print('p373',json.dumps(out['checks'][-1],sort_keys=True))
    print('saved',path)
if __name__=='__main__':main()
