#!/usr/bin/env python3
"""Exact finite Clausen p^2 factorization and p^3 high-low truncation defect.

Author-side computation in Z/p^3 Z; does not execute EM native Source experiments.
No external dependencies or float arithmetic.
"""
from math import comb, isqrt


def primes_1_mod_6(bound: int):
    sieve = bytearray(b'\x01') * (bound + 1)
    sieve[0:2] = b'\x00\x00'
    for d in range(2, isqrt(bound)+1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((bound-d*d)//d + 1)
    return [p for p in range(7, bound+1) if sieve[p] and p%6==1]


def case(p: int):
    assert p%6 == 1 and p >= 7
    r=(p-1)//6
    m2=p*p; m3=p**3
    inv18=pow(18,-1,m3); inv2=pow(2,-1,m3)
    h=[1]*p; a=[1]*p; powers=[1]*p
    for k in range(1,p):
        powers[k]=powers[k-1]*inv2 % m3
        ik=pow(k,-1,m3)
        h[k]=h[k-1]*(6*k-5)*(3*k-2)*inv18*ik*ik%m3
        a[k]=a[k-1]*(2*k-1)*(3*k-2)*(3*k-1)*inv18*ik*ik*ik%m3
    # The exact Clausen formal identity determines coefficients of degrees < p.
    H=sum(h[k]*powers[k] for k in range(p))%m3
    H1=sum(k*h[k]*powers[k] for k in range(p))%m3
    F=sum(a[k]*powers[k] for k in range(p))%m3
    F1=sum(k*a[k]*powers[k] for k in range(p))%m3
    assert (H*H-F)%m2==0
    assert (2*H*H1-F1)%m2==0

    # Low-index reduction of (1/6,1/3) to (-r,-2r), then Clausen.
    pr=sum(comb(r,j)*comb(2*r,j)*powers[j] for j in range(r+1))%p
    assert H%p==pr
    assert F%p==pr*pr%p

    # Fast O(p) high-low defect, no need to build high-index coefficients.
    inv2_p=pow(2,-1,p)
    X=[0]*(r+2);Y=[0]*(r+2)
    for j in range(r,0,-1):
        w=h[j]*pow(inv2_p,j,p)%p
        X[j]=(X[j+1]+w)%p
        Y[j]=(Y[j+1]+j*w)%p
    c=pow(18*(r+1)*(2*r+1),-1,p)
    D0=D1=0
    for s in range(1,r+1):
        scaled=c*pow(2,s,p)%p
        D0=(D0+scaled*X[s])%p
        D1=(D1+scaled*(Y[s]-s*X[s]))%p
        if s<r:
            c=c*s*s*pow((r+s+1)*(2*r+s+1),-1,p)%p
    theta=(D0+6*D1)%p
    assert (H*H-F)//m2 %p==D0
    assert (2*H*H1-F1)//m2 %p==D1
    S=(F+6*F1)%m3
    assert S==(H*(H+12*H1)-m2*theta)%m3

    if pr==0:
        assert H%p==0
        u=H//p %(p*p)
        v=H1%(p*p)
        # Condition equivalent to S = p (mod p^3), not assumed universally.
        assert (S//p)%m2==(12*u*v+p*(u*u-theta))%m2
    else:
        u=None;v=None
    return {'p':p,'r':r,'class':p%24,'pr':pr,'D0':D0,'D1':D1,
            'theta':theta,'Hdivp':u,'H1':v,'S':S,
            'S_equals_p':S==p}


def independent_high_low(p:int):
    """Independent exact convolution and reflected factorial/kernel cross-check."""
    from math import factorial
    r=(p-1)//6; m3=p**3
    inv18=pow(18,-1,m3)
    h=[1]*p; a=[1]*p
    for k in range(1,p):
        ik=pow(k,-1,m3)
        h[k]=h[k-1]*(6*k-5)*(3*k-2)*inv18*ik*ik %m3
        a[k]=a[k-1]*(2*k-1)*(3*k-2)*(3*k-1)*inv18*ik*ik*ik%m3
    # True coefficientwise Clausen comparison and p^2 whole-polynomial factorization.
    for n in range(2*p-1):
        conv=sum(h[k]*h[n-k] for k in range(max(0,n-p+1), min(n,p-1)+1))%m3
        if n<p:
            assert conv==a[n],(p,n,'formal-coefficient')
        else:
            assert conv%(p*p)==0,(p,n,'p2-tail')
    def high_coeff(s):
        numerator=factorial(r)*factorial(2*r)*factorial(s-1)**2
        denom=18*factorial(r+s)*factorial(2*r+s)
        return numerator*pow(denom,-1,p)%p
    inv2=pow(2,-1,p)
    D0=D1=0
    for s in range(1,r+1):
        k=p-s
        assert h[k]%(p*p)==0
        c=high_coeff(s)
        assert h[k]//(p*p)%p==c,(p,s,'factorial-reflection')
        for j in range(s,r+1):
            # 2 identical cross-pairs of index (p-s,j).
            contribution=2*c*h[j]*pow(inv2,k+j,p)%p
            D0=(D0+contribution)%p
            D1=(D1+(k+j)*contribution)%p
    got=case(p)
    assert (got['D0'],got['D1'])==(D0,D1), (p,'independent-double-sum')
    # Independently reconstruct original binomial A at z=1/2.
    for k in range(p):
        a_direct=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m3)%m3
        assert a_direct==a[k]*pow(2,-k,m3)%m3,(p,k,'binomial-A')
    return got


def main():
    ps=primes_1_mod_6(3000)
    target=[];total=0
    for p in ps:
        d=case(p);total+=1
        if p%24 in (13,19):
            target.append(d)
            assert d['pr']==0,(p,'CM-Hasse-finite-check')
    print('ALL 1(mod6) primes <= 3000:', total)
    print('PASS: exact finite Clausen square p^2 evaluation and p^3 weighted defect; integer arithmetic')
    print('TARGET 13/19 finite Hasse root check:',len(target))
    print('FINITE S=p mod p^3 in checked range (not universal proof):',sum(case(p)['S_equals_p'] for p in ps),'/',total)
    sample=(7,13,19,31,37,43,61,373,1171)
    for p in sample:
        d=independent_high_low(p)
        print('certificate',d)
    print('INDEPENDENT: polynomial convolution, high-index factorial reflection, double-sum, direct binomial A for 9 sample primes PASS')
    print('STATUS: AUTHOR_DERIVED; EXACT_PROOF_DRAFT; EXACT_CHECKED; UNREVIEWED; NOT_ADMITTED; NATIVE_NOT_EXECUTED')
if __name__=='__main__':main()
