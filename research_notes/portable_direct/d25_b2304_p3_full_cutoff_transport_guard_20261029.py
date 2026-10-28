#!/usr/bin/env python3
"""D25 B2304 third-digit cutoff/transport exact p-adic integer checker. Pure Python.

Author-side portable finite ring research, not a Source-native benchmark.
"""
from math import comb

def coefficients(parameters, denominator, length, mod):
    vals=[1]
    for n in range(length-1):
        top=1
        for a,step in parameters: top *= a+step*n
        bot=denominator*(n+1)**len(parameters)
        vals.append(vals[-1]*top*pow(bot,-1,mod)%mod)
    return vals

def run(p,check_coeff=True):
    assert p>3 and p%8 in (3,5)
    M=p**3; w=pow(9,-1,M)
    a=((p-3)//8 if p%8==3 else (5*p-1)//8)
    b=((3*p-1)//8 if p%8==3 else (7*p-3)//8)
    beta=coefficients([(1,8),(3,8)],64,p,M)
    gamma=coefficients([(1,4),(2,4),(3,4)],64,p,M)
    assert all(beta[i]%p==0 for i in range(a+1,p))
    assert all(beta[i]%(p*p)==0 for i in range(b+1,p))
    w_pow=[1]
    for i in range(max(2*b,p-1)+1):w_pow.append(w_pow[-1]*w%M)
    # Exact low and high source-tagged pair convolutions of K_b^2.
    high=low=0
    coeff=[0]*(2*b+1)
    for i in range(b+1):
        for j in range(b+1):
            coeff[i+j]=(coeff[i+j]+beta[i]*beta[j])%M
    if p%8==5:
        assert 2*a >= p and a+b >= p
        assert coeff[2*a]%p != 0
        assert all(x%p==0 for x in coeff[2*a+1:])
        assert coeff[a+b]%p==0 and coeff[a+b]%(p*p)!=0
        assert all(x%(p*p)==0 for x in coeff[a+b+1:])
        assert coeff[2*b]%(p*p)==0 and coeff[2*b]%M!=0
    else:
        assert 2*b<p
    for n,s in enumerate(coeff):
        term=(1+8*n)*s*w_pow[n]%M
        if n>=p:high=(high+term)%M
        else:low=(low+term)%M
    K=sum(beta[i]*w_pow[i] for i in range(b+1))%M
    thetaK=sum(i*beta[i]*w_pow[i] for i in range(b+1))%M
    weighted_K=(K*K+16*K*thetaK)%M
    assert (low+high)%M==weighted_K
    # Missing p^2 partner tail, with only i<=a surviving modulo p^3.
    corr_unit=0
    for i in range(a+1):
        for j in range(b+1,p-i):
            corr_unit += (1+8*(i+j))*(beta[i]%p)*((beta[j]//(p*p))%p)*pow(w,i+j,p)
    corr_unit %=p
    correction=2*(p*p)*corr_unit %M
    C=sum((1+8*n)*gamma[n]*w_pow[n] for n in range(p))%M
    Bor=sum((8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,M) for n in range(p))%M
    assert C==Bor
    assert (weighted_K-high+correction)%M==C, (p,weighted_K,high,correction,C)
    if check_coeff:
        for n in range(p):
            defect=(gamma[n] - (coeff[n] if n<len(coeff) else 0))%M
            repair=0
            for j in range(b+1,n+1):
                repair+=2*beta[j]*beta[n-j]
            assert defect == repair%M,(p,n,defect,repair%M)
            assert defect%(p*p)==0,(p,n,defect)
    return dict(p=p,a=a,b=b,K=K,thetaK=thetaK,weighted_K=weighted_K,weighted_high=high,repair_unit=corr_unit,repair=correction,original_B=C,weighted_projected=low,head_unit=(high//p)%p if high%p==0 else None, Bq=C//p if C%p==0 else None)

if __name__=='__main__':
    tests=(11,13,19,29,37,43,53,59,61,67,83,107,109,131,139,157,163,181,187,229,251,277,283,307,331,349,373,379)
    for p in tests:
        # elementary deterministic primality check
        if any(p%i==0 for i in range(2,int(p**.5)+1)):continue
        result=run(p,check_coeff=True)
        if p in (13,19,37,43,373):print('EXACT',result)
    print('PASS_D25_B2304_P3_UNIFORM_TRUNCATION_REPAIR',sum(not any(p%i==0 for i in range(2,int(p**.5)+1)) for p in tests),'primes')

def cross_kernel_p373():
    p=373; M=p**3; m=(p-1)//6
    al=coefficients([(1,3),(1,2),(2,3)],18,p,M)
    ba=coefficients([(1,6),(1,3)],18,p,M)
    wa=pow(2,-1,M)
    h=2*m
    ha=sum(ba[i]*pow(wa,i,M) for i in range(h+1))%M
    dha=sum(i*ba[i]*pow(wa,i,M) for i in range(h+1))%M
    base=(ha*ha+12*ha*dha)%M
    corr_unit=0
    for i in range(m+1):
        for j in range(h+1,p-i):
            assert ba[j]%(p*p)==0
            corr_unit += (1+6*(i+j))*(ba[i]%p)*((ba[j]//(p*p))%p)*pow(wa,i+j,p)
    repair=(2*p*p*(corr_unit%p))%M
    A=sum((1+6*n)*al[n]*pow(wa,n,M) for n in range(p))%M
    Aoriginal=sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,M) for n in range(p))%M
    assert A==Aoriginal==(base+repair)%M==p
    B=run(p,check_coeff=False)
    assert (base - B['weighted_K'] + B['weighted_high'] + repair - B['repair'])%M==0
    return dict(p=p,A_original=A, A_square=base, A_repair=repair, A_repair_unit=(2*corr_unit)%p,
                B_square=B['weighted_K'],B_high=B['weighted_high'],B_repair=B['repair'],B_original=B['original_B'],
                A_minus_B=((base - B['weighted_K'])+B['weighted_high']+(repair-B['repair']))%M)

if __name__=='__main__':
    print('CROSS_373',cross_kernel_p373())
