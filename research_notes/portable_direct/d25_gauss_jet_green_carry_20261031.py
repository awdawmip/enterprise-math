#!/usr/bin/env python3
"""Finite Gauss parameter-jet ODE/Green carry, p^2 exact modular guard.

AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED; not native H0/B0, not a proof of D25 LIFT.
Uses independent coefficient recurrence, factorial endpoint and Green current.
"""
from math import comb


def primes(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(n**0.5)+1):
        if sieve[d]:
            sieve[d*d:n+1:d] = b'\x00' * ((n-d*d)//d+1)
    return [p for p in range(7, n+1) if sieve[p] and p % 6 == 1]


def jets(p):
    m = p*p
    ell = (p-1)//6
    inv6, inv3 = pow(6, -1, m), pow(3, -1, m)
    u,v,w = [1], [0], [0]
    x,y,z = 1,0,0
    for k in range(1,p):
        a,b=k-1-ell,k-1-2*ell
        a0=x*a % m
        a1=(y*a+x*inv6)%m
        a2=(z*a+y*inv6)%m
        den=pow(k*k,-1,m)
        x=a0*b*den % m
        y=(a1*b+a0*inv3)*den %m
        z=(a2*b+a1*inv3)*den %m
        u.append(x);v.append(y);w.append(z)
    return u,v,w


def L0(seq,ell,m):
    p=len(seq)
    return [(k*k*(seq[k] if k<p else 0)
             -(k-1-ell)*(k-1-2*ell)*(seq[k-1] if k>=1 else 0))%m
            for k in range(p+1)]


def signed_green_coefficient(p):
    ell=(p-1)//6; m=p*p
    u,v,w=jets(p)
    inv2=pow(2,-1,m);inv3=pow(3,-1,m); inv18=pow(18,-1,m)
    D=lambda k: (k*inv2-2*ell*inv3)%m
    gamma=20*ell*ell*w[-1]%m
    # independently reproduce cross-wall coefficient from original factorials
    fact=[1]*p
    for i in range(1,p):fact[i]=fact[i-1]*i%m
    wtop=(((-1)**ell)*fact[ell]*fact[2*ell]*fact[5*ell-1]*fact[4*ell-1]
          *pow(18*fact[p-1]**2,-1,m))%m
    assert wtop==w[-1], (p,'factorial terminal')
    assert gamma%p !=0, (p,'terminal unit')
    assert all(x==0 for x in u[ell+1:]), (p,'u support')
    assert all(x==0 for x in v[2*ell+1:]), (p,'v support')

    eq0,eq1,eq2=L0(u,ell,m),L0(v,ell,m),L0(w,ell,m)
    for k in range(p+1):
        un=u[k-1] if 1<=k<=p else 0
        vn=v[k-1] if 1<=k<=p else 0
        assert eq0[k]==0, (p,k,'J0 equation')
        assert eq1[k]==(D(k-1)*un if k>=1 else 0)%m, (p,k,'J1 equation')
        forcing=(D(k-1)*vn+inv18*un if k>=1 else 0)%m
        if k==p:forcing=(forcing-gamma)%m
        assert eq2[k]==forcing, (p,k,'J2 equation')

    # Exact p-carry identity.  RHS coefficient uses u,v, plus *one* old w endpoint.
    lower=0
    for i in range(ell+1):
        for j in range(2*ell+1):
            k=p-1-i-j
            if k>=0:
                lower += comb(3*ell+k,k)*u[i]*(D(j)*v[j]+inv18*u[j])
    lower%=m
    assert (lower-gamma)%p==0, (p,'p divisibility')

    # Independent complete signed Wronskian: both source orders retained.
    W=[0]*p
    for i in range(p):
        for j in range(1,p):
            if i+j-1>=p: break
            W[i+j-1]=(W[i+j-1]+u[i]*j*w[j]-w[i]*j*u[j])%m
    current=sum(comb(3*ell+k-1,k)*W[p-1-k] for k in range(p))%m
    assert (lower-gamma)%m == p*current%m, (p,'Green divided-carry')
    return {'p':p,'ell':ell,'signed_terminal_unit':gamma%p,
            'lower_source_residue':lower%p,'carry':((lower-gamma)%m)//p,
            'green_current':current%p}


def main():
    tested=[signed_green_coefficient(p) for p in primes(500)]
    anchors=[x for x in tested if x['p'] in (7,13,19,37,67,373)]
    print('tested primes 7 <= p <= 500, p = 1 mod 6:',len(tested))
    print('anchors:',anchors)
    print('PASS_D25_GAUSS_JET_GREEN_P_CARRY_EXACT')

if __name__=='__main__':main()
