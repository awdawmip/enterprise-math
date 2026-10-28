#!/usr/bin/env python3
"""Author-side: explicit binomial/harmonic transport of B2304 high-degree carry.
Not native H0/B0 and not a proof of the all-prime LIFT congruence.
"""
from math import comb

def inverse(a, modulus):
    return pow(a % modulus, -1, modulus)

def run_prime(p):
    assert p >= 13 and p % 8 == 5
    M=p**3
    a=(5*p-1)//8
    b=(7*p-3)//8
    t=(p-1)//4
    assert b-a==t
    # Direct independent hypergeometric recurrence for beta=(1/8)_n(3/8)_n/(n!)^2.
    beta=[1]
    for n in range(b):
        beta.append(beta[-1]*(8*n+1)*(8*n+3)*inverse(64*(n+1)**2,M)%M)
    # Binomial/harmonic low segment through full p^3 precision.
    inv8=inverse(8,M)
    S1=0
    S2=0
    low=[]
    inv2=inverse(2,M)
    for i in range(a+1):
        if i:
            x=5*inv8*inverse(a-i+1,M)%M
            y=7*inv8*inverse(b-i+1,M)%M
            S1=(S1+x+y)%M
            S2=(S2+x*x+y*y)%M
        L=comb(a,i)*comb(b,i)%M
        fac=(1-p*S1+p*p*(S1*S1-S2)*inv2)%M
        low.append(L*fac%M)
        assert low[-1]==beta[i], ('low',p,i,low[-1],beta[i])
    # One-p middle segment, explicit Pochhammer and first p-adic derivative.
    invM=p*p
    S_a=S1%invM
    P=1
    extra=0
    mid=[]
    for r in range(t):
        if r:
            k=r-1
            A=8*k+8; B=8*k+10; C=8*k+15
            assert A%p and B%p and C%p
            P=P*A*B*inverse(C*C,invM)%invM
            extra=(extra+5*(inverse(A,invM)+inverse(B,invM)-2*inverse(C,invM)))%invM
        fac=(1+p*(-S_a+15*inverse(14,invM)+extra))%invM
        E=(comb(b,a)*10*inverse(49,invM)*P*fac)%invM
        j=a+1+r
        assert beta[j]%p==0
        assert E==beta[j]//p%invM, ('mid',p,j,E,beta[j]//p%invM)
        mid.append(p*E%M)
    # Source-preserving, ordered-pair operator, not a single-total surrogate.
    w=inverse(9,M)
    powers=[1]
    for n in range(2*b): powers.append(powers[-1]*w%M)
    parts={'unit_unit':0,'unit_middle':0,'middle_middle':0}
    for i,bi in enumerate(low):
        for j,bj in enumerate(low):
            n=i+j
            if n>=p:
                parts['unit_unit']=(parts['unit_unit']+(1+8*n)*bi*bj*powers[n])%M
    for i,bi in enumerate(low):
        for r,bj in enumerate(mid):
            n=i+a+1+r
            if n>=p:
                parts['unit_middle']=(parts['unit_middle']+2*(1+8*n)*bi*bj*powers[n])%M
    for r,bi in enumerate(mid):
        for s,bj in enumerate(mid):
            n=2*(a+1)+r+s
            if n>=p:
                parts['middle_middle']=(parts['middle_middle']+(1+8*n)*bi*bj*powers[n])%M
    H=sum(parts.values())%M
    # Independently calculate high-degree carry from unsplit beta recurrence.
    direct=0
    for i in range(b+1):
        for j in range(b+1):
            if i+j>=p:
                n=i+j
                direct=(direct+(1+8*n)*beta[i]*beta[j]*powers[n])%M
    assert H==direct,(p,H,direct)
    assert parts['unit_middle']%p==0 and parts['middle_middle']%(p*p)==0
    if p == 373: assert H==14329914
    # Check pointwise valuation layers at distinguished endpoint n=2a,a+b,2b
    # This records exact provenance from the same p-local beta coefficients.
    def coeff_at(n):
        return sum(beta[i]*beta[n-i] for i in range(max(0,n-b),min(b,n)+1))%M
    c2a, cab, c2b=coeff_at(2*a),coeff_at(a+b),coeff_at(2*b)
    assert c2a%p!=0 and cab%p==0 and cab%(p*p)!=0 and c2b%(p*p)==0 and c2b%M!=0
    return {'p':p,'a':a,'b':b,'t':t,'H':H,'H_digit':H//p if H%p==0 else None,'parts':parts,'endpoint':{'c2a':c2a,'cab':cab,'c2b':c2b}}

if __name__ == '__main__':
    primes=[13,29,37,53,61,101,109,149,157,173,181,197,229,269,277,317,349,373]
    for p in primes:
        assert all(p%d for d in range(2,int(p**.5)+1))
    rows=[run_prime(p) for p in primes]
    print(f'PASS_D25_B2304_HARMONIC_THREE_SOURCE_CARRY {len(rows)} primes')
    for row in rows:
        if row['p'] in (13,37,373): print(row)
