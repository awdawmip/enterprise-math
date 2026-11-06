#!/usr/bin/env python3
"""D25 provenance-preserving top-jet identities, exact finite fields.

Checks high-degree coefficients using original polynomial products and an
independent rational closed sequence from Bernoulli power sums. No native run.
"""
from fractions import Fraction
from math import comb, factorial, isqrt

C = [Fraction(1),Fraction(-1,4),Fraction(301,288),Fraction(-865,384),
     Fraction(524161,55296),Fraction(-9262421,221184),
     Fraction(11448840713,47775744),Fraction(-295941110075,191102976),
     Fraction(638943911769443,55037657088)]

def bernoulli_numbers(n):
    vals=[Fraction(1)]
    for j in range(1,n+1):
        vals.append(-sum(comb(j+1,k)*vals[k] for k in range(j))/Fraction(j+1))
    return vals

B=bernoulli_numbers(9)
def bernoulli_poly(r,z):
    return sum(comb(r,j)*B[j]*z**(r-j) for j in range(r+1))

def sum_powers(n,q):
    return (bernoulli_poly(q+1,n)-bernoulli_poly(q+1,Fraction(0)))/Fraction(q+1)

def source_e(j,r):
    a=Fraction(-1,3); c=Fraction(-2,3)
    S=[Fraction(0)]*(r+1)
    for d in range(1,r+1):
        S[d]=sum(sum(comb(d,q)*z**(d-q)*(-1)**q*sum_powers(j,q)
                     for q in range(d+1)) for z in (a,c))
    E=[Fraction(1)]
    for d in range(1,r+1):
        E.append(sum((-1)**(q-1)*E[d-q]*S[q] for q in range(1,d+1))/d)
    return E[r]

def rational_top_coeff(k):
    result=Fraction(0)
    for ell in range(k//2+1):
        rising=Fraction(1)
        for h in range(ell):rising*=Fraction(1,2)+h
        rho=Fraction(1+3*ell)*2**ell*rising**3/factorial(ell)
        result+=rho*source_e(Fraction(-1,2)-ell,k-2*ell)
    return result

assert [rational_top_coeff(k) for k in range(len(C))]==C

def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))

def pcheck(p):
    assert p%6==1 and prime(p)
    m=(p-1)//6; a=2*m; b=3*m;c=4*m
    K=min(len(C)-1,p-3)
    inv2=pow(2,-1,p)
    fac=[1]*(b+1)
    for j in range(1,b+1):fac[j]=fac[j-1]*j%p
    invfac=[pow(x,-1,p) for x in fac]
    predicted=[0]*(K+1)
    for ell in range(0,K//2+1):
        j=b-ell
        e=[1]+[0]*K
        count=0
        for h in range(j):
            for x in (a-h,c-h):
                count+=1
                for d in range(min(K,count),0,-1):
                    e[d]=(e[d]+x*e[d-1])%p
        base=(6*j+1)*pow(-inv2,j,p)*fac[b]*invfac[j]*invfac[b-j]*invfac[j]**2%p
        for k in range(2*ell,K+1):
            predicted[k]=(predicted[k]+base*e[k-2*ell])%p
    leg=pow(2,(p-1)//2,p)
    assert leg in (1,p-1)
    expected=[(2*leg*int(v.numerator)*pow(v.denominator,-1,p))%p for v in C[:K+1]]
    assert predicted==expected,(p,predicted,expected)
    top,second=predicted[:2]
    assert top==2*leg%p
    assert second==(-leg*pow(2,-1,p))%p
    return (p,K,top,second,predicted[2] if K>=2 else None)

def moment_check(p):
    m=(p-1)//6; a=2*m;b=3*m;c=4*m
    inv2=pow(2,-1,p)
    M0=M1=Inv1=0
    for z in range(p):
        aa=cc=bb=w=1
        Pz=0
        for j in range(b+1):
            Pz=(Pz+(6*j+1)*aa*bb*cc*w)%p
            if j==b: break
            jj=pow(j+1,-1,p)
            aa=aa*(a+z-j)*jj%p
            cc=cc*(c+z-j)*jj%p
            bb=bb*(b-j)*jj%p
            w=w*(-inv2)%p
        M0=(M0+Pz)%p; M1=(M1+z*Pz)%p
        if z:Inv1=(Inv1+Pz*pow(z,-1,p))%p
    chi=pow(2,(p-1)//2,p)
    assert M0==(-2*chi)%p,(p,M0)
    assert M1==(chi*pow(2,-1,p))%p,(p,M1)
    aa=cc=bb=w=1; da=dc=0; jet=0
    for j in range(b+1):
        jet=(jet+(6*j+1)*w*bb*(da*cc+aa*dc))%p
        if j==b: break
        u=pow(j+1,-1,p)
        da,aa=((da*(a-j)+aa)*u)%p,aa*(a-j)*u%p
        dc,cc=((dc*(c-j)+cc)*u)%p,cc*(c-j)*u%p
        bb=bb*(b-j)*u%p
        w=w*(-inv2)%p
    assert jet==(-Inv1)%p,(p,jet,Inv1)
    return (p,M0,M1,Inv1,jet)

if __name__=='__main__':
    results=[]
    for p in range(7,10001):
        if p%6==1 and prime(p):results.append(pcheck(p))
    print('primes checked',len(results))
    print('sample',[x for x in results if x[0] in [7,13,19,109,211,229,373,1093,3511,5113]])
    print('coefficient profile',list(map(str,C)))
    print('independent value-moment checks',[moment_check(p) for p in (7,13,19,31,37,43,109,211)])
    print('all exact Fp coefficient checks PASS')
