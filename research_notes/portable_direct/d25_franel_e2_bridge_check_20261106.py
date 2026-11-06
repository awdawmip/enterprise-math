#!/usr/bin/env python3
"""Independent exact mod p^3 original 216 / Franel E.2 two-jet checker.
Only finite author checks, not a uniform W=V proof or native H0/B0 run.
"""
from math import comb, isqrt

def primes(n):
    sv=bytearray([1])*(n+1); sv[:2]=b'\0\0'
    for q in range(2,isqrt(n)+1):
        if sv[q]: sv[q*q::q]=bytes((n-q*q)//q+1)
    return [p for p in range(7,n+1) if sv[p] and p%6==1]

def compute(p):
    m=(p-1)//6; M=p**3
    W=sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,M)
          for n in range(p))%M
    v=1; V=0
    for n in range(p):
        V=(V+(6*n+1)*v)%M
        if n<p-1: v=-v*(3*n+1)**3*pow(27*(n+1)**3,-1,M)%M
    f=0; h1=h2=0; L1=L2=0; V0=0
    for n in range(2*m+1):
        b=comb(2*m,n)**3; w=6*n+1
        f=(f+b)%M
        V0=(V0+w*b)%M
        L1=(L1+w*b*h1)%M
        L2=(L2+w*b*(h1*h1-h2*pow(3,-1,M)))%M
        if n<2*m:
            j=2*m-n; iv=pow(j,-1,M)
            h1=(h1+iv)%M; h2=(h2+iv*iv)%M
    assert V0==p*f%M,(p,'exact pair identity')
    Vjet=(p*f-p*L1+p*p*pow(2,-1,M)*L2)%M
    assert V==Vjet,(p,'strict E.2 jet mismatch',V,Vjet)
    assert W==V,(p,'open original/E.2 bridge fails',W,V)
    assert (f-L1+p*pow(2,-1,M)*L2-1)%(p*p)==0
    return {'p':p,'m':m,'F_mod_p2':f%(p*p),'L1_mod_p2':L1%(p*p),
            'L2_mod_p':L2%p,'V':V,'W':W,'bridge_residue':(W-V)%M}

if __name__=='__main__':
    rows=[compute(p) for p in primes(1999)]
    print('PASS',len(rows),'target',sum(r['p']%24 in (13,19) for r in rows),
          'finite original/E2 bridge observations, failures=0')
    for r in rows:
        if r['p'] in (7,13,19,31,67,373): print(r)
