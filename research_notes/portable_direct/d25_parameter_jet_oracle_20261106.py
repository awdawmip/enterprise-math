#!/usr/bin/env python3
"""Independent original-216 polynomial three-jet exact arithmetic.
Same original 216 coefficient, not native p373 H0/B0 divided-power.
"""
from math import isqrt, comb

def primes(N):
    sieve=bytearray(b'\x01')*(N+1)
    sieve[:2]=b'\x00\x00'
    for d in range(2,isqrt(N)+1):
        if sieve[d]: sieve[d*d::d]=b'\x00'*((N-d*d)//d+1)
    return [p for p in range(7,N+1) if sieve[p] and p%6==1]

def jet(p):
    assert p>=7 and p%6==1
    m=(p-1)//6; M=p**3
    A0,A1,A2=1,0,0
    S0=S1=S2=0
    for n in range(p):
        w=6*n+1
        S0=(S0+w*A0)%M
        S1=(S1+w*A1)%M
        S2=(S2+w*A2)%M
        if n==p-1: break
        x,y,z=n-3*m,n-2*m,n-4*m
        c0=18*x*y*z
        c1=12*x*y+3*z*(2*x+3*y)
        c2=2*(2*x+3*y)+3*z
        iv=pow(36*(n+1)**3,-1,M)
        B0=c0*A0*iv%M
        B1=(c0*A1+c1*A0)*iv%M
        B2=(c0*A2+c1*A1+c2*A0)*iv%M
        A0,A1,A2=B0,B1,B2
        if n+1>2*m: assert A0==0
        if n+1>3*m: assert A1==0
        if n+1>4*m: assert A2==0
    value=(S0+p*S1+p*p*S2)%M
    direct=0
    for n in range(p):
        gamma=comb(2*n,n)**2*comb(3*n,n)
        an=gamma*pow(216,-n,M)%M
        direct=(direct+(6*n+1)*an)%M
    assert value==direct,(p,value,direct)
    assert S0%p==0
    return dict(p=p,m=m,J0=S0,J1=S1%p**2,J2=S2%p,
                W=direct,target=(p%24 in (13,19)),
                jet2_nonzero=(S2%p!=0))

if __name__=='__main__':
    rows=[jet(p) for p in primes(1999)]
    print('PASS primes',len(rows),'target',sum(r['target'] for r in rows),
          'J2_nonzero',sum(r['jet2_nonzero'] for r in rows),
          'target_j2_nonzero',sum(r['target'] and r['jet2_nonzero'] for r in rows))
    print('all_w_equals_p',all(r['W']==r['p'] for r in rows))
    for r in rows:
        if r['p'] in (7,13,19,31,67,373): print(r)
