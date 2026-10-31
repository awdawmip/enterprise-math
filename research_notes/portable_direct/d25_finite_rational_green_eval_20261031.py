#!/usr/bin/env python3
"""AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED.

Exact finite rational evaluation of D25 Gauss Green current at z=1/2.
Mod p^2 tests are implementation checks, not an infinite-prime proof, native
H0/B0 experiment, source checkpoint or canonical task admission.
"""
from math import comb


def primes(n):
    out = []
    for p in range(7, n + 1):
        if p % 6 == 1 and all(p % d for d in range(2, int(p**0.5) + 1)):
            out.append(p)
    return out


def add_poly(a,b,mod):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]=(out[i]+x)%mod
    for i,x in enumerate(b):out[i]=(out[i]+x)%mod
    return out


def mul_poly(a,b,mod):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[i+j]=(out[i+j]+x*y)%mod
    return out


def evaluation(poly, z, mod):
    out=0
    for x in poly[::-1]:out=(out*z+x)%mod
    return out


def jets(p):
    m=p*p;l=(p-1)//6
    r6=pow(6,-1,m);r3=pow(3,-1,m)
    u,v,w=[1],[0],[0]
    x,y,z=1,0,0
    for k in range(1,p):
        a,b=k-1-l,k-1-2*l
        xa=x*a%m;ya=(y*a+x*r6)%m;za=(z*a+y*r6)%m
        inv=pow(k*k,-1,m)
        x=xa*b*inv%m
        y=(ya*b+xa*r3)*inv%m
        z=(za*b+ya*r3)*inv%m
        u.append(x);v.append(y);w.append(z)
    return u,v,w


def signed_R_independent(p):
    """Previously established four-port boundary, independently as double sum."""
    l=(p-1)//6
    inv2=pow(2,-1,p)
    c=[0]*(l+1)
    c[1]=pow(10,-1,p)
    for i in range(1,l):
        c[i+1]=c[i]*36*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
    R=0
    for i in range(1,l+1):
        g=comb(l,i)*comb(2*l,i)*pow(inv2,i,p)%p
        K=sum((1+6*(i-a))*c[a] for a in range(1,i+1))%p
        R=(R+2*g*K)%p
    return R


def exact_mod_check(p):
    l=(p-1)//6;M=3*l;mod=p*p
    u,v,w=jets(p)
    assert not any(u[l+1:]) and not any(v[2*l+1:])
    inv18=pow(18,-1,mod)
    d=[(j*pow(2,-1,mod)-2*l*pow(3,-1,mod))*v[j] %mod for j in range(p)]
    d=add_poly(d,[x*inv18%mod for x in u],mod)
    low=mul_poly(u,d,mod)
    gamma=20*l*l*w[-1]%mod
    F=add_poly(low, [0]*(p-1)+[(-gamma*x)%mod for x in u],mod)
    F=F[:7*l+1]

    # Finite y=1-z binomial transform of polynomial numerator F(z).
    coeff=[0]*len(F)
    for j, Fj in enumerate(F):
        if Fj:
            for k in range(j+1):
                coeff[k]=(coeff[k]+(-1 if k%2 else 1)*Fj*comb(j,k))%mod

    # Nontrivial residue cancellation at z=1. This also gives a top-jet identity.
    assert coeff[M] == 0, (p,'nonzero forbidden rational residue')
    S=sum(u[i]*comb(6*l+i,3*l) for i in range(l+1))%mod
    top=l*pow(3,-1,mod)*u[l]*v[2*l]%mod
    assert gamma*S%mod == top, (p,'endpoint top-jet residue identity')
    assert S%p == (-1)**l%p, (p,'S not signed unit')

    # The finite primitive evaluation uses only unit denominators k-M (k != M).
    finite=0
    for k,fk in enumerate(coeff):
        if k == M: continue
        r=k-M
        assert -p < r < p
        twopow=pow(2, -r, mod) if r < 0 else pow(pow(2,r,mod),-1,mod)
        finite=(finite+fk*(1-twopow)*pow(r,-1,mod))%mod

    inv2=pow(2,-1,mod)
    j0=evaluation(u,inv2,mod)
    j2=evaluation(w,inv2,mod)
    dj0=evaluation([j*u[j]%mod for j in range(p)], inv2,mod)
    dj2=evaluation([j*w[j]%mod for j in range(p)], inv2,mod)
    # theta-value = z * derivative; Wronskian derivative value=2*(theta W)
    W=(j0*(2*dj2)-j2*(2*dj0))%mod
    direct=pow(2, M-1,mod)*W%mod
    assert finite==direct, (p,finite,direct,'finite adjoint mismatch')
    return (p,gamma%p,S%p,direct%p,direct,signed_R_independent(p))


def main():
    tested=[exact_mod_check(p) for p in primes(500)]
    anchors=[r for r in tested if r[0] in (7,13,19,37,67,373)]
    print('primes p=1 mod6, 7<=p<=500:',len(tested))
    print('anchors (p,gamma modp,S modp,Phi(1/2) modp,Phi(1/2) modp²,signed R modp):',anchors)
    assert exact_mod_check(67)[3] != exact_mod_check(67)[5]
    assert exact_mod_check(373)[3] != exact_mod_check(373)[5]
    print('PASS_D25_FINITE_RATIONAL_GREEN_EVALUATION_PLOCAL')

if __name__=='__main__':main()
