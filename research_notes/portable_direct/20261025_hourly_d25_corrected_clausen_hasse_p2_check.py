"""Exact author-side integer checks for corrected Clausen Hasse cutoff.

Uses only Python standard library. Finite checks are not universal proof,
independent review or native CM/Frobenius experiments.
"""
from math import factorial

def primes_upto(n):
    s=[True]*(n+1)
    s[0:2]=[False,False]
    for j in range(2,int(n**0.5)+1):
        if s[j]:
            for k in range(j*j,n+1,j): s[k]=False
    return [p for p in range(7,n+1) if s[p] and p%6==1]

def product_factors(factors, degree, modulus):
    v=[1]+[0]*degree
    for a,b in factors:
        for k in range(degree,0,-1):
            v[k]=(a*v[k]+b*v[k-1])%modulus
        v[0]=a*v[0]%modulus
    return v

def corrected_forcing(p,degree):
    m,N,M=(p-1)//6,p-1,p*p
    numerator=product_factors(
        [(j-m,-1) for j in range(p)]+[(j-2*m,-2) for j in range(p)],
        degree,M)
    denominator=product_factors([(2*j-p,-6) for j in range(1,p)],degree,M)
    scale=pow(2,N,M)*pow(factorial(N),-1,M)%M
    scaled=[scale*x%M for x in numerator]
    answer=[0]*(degree+1); inv=pow(denominator[0],-1,M)
    for k in range(degree+1):
        sub=sum(denominator[j]*answer[k-j] for j in range(1,k+1))
        answer[k]=(scaled[k]-sub)*inv%M
    return answer

def harmonic(p,length,order):
    M=p*p
    return sum(pow(pow(j,-1,M),order,M) for j in range(1,length+1))%M

def formula(p,n):
    M=p*p; m,N=(p-1)//6,p-1
    raw=(1+pow(2,n,M)-pow(3,n,M))*harmonic(p,N,n)
    corr=(-1)**n*(harmonic(p,m,n+1)+pow(2,n,M)*harmonic(p,2*m,n+1))
    corr+=pow(3,n,M)*pow(2,-1,M)*harmonic(p,N,n+1)
    return 2*pow(n,-1,M)*(raw-n*p*corr)%M

def check(p,full):
    M=p*p; degree=(2*p+4 if full else p+2)
    co=corrected_forcing(p,degree)
    assert [k for k,v in enumerate(co) if v%p]==[2,p+1],p
    assert -co[2]%p==p-2
    assert -co[p+1]%p==2
    for n in range(1,p-1):
        assert -co[n+2]%M==formula(p,n),(p,n)
    M3=p**3; u=1
    for j in range(1,p):
        u=u*(2*j)*pow(2*j-p,-1,M3)%M3
    assert u==1,(p,u)
    return p-2

def main():
    ps=primes_upto(373)
    assert len(ps)==35
    pairs=sum(check(p,p<=103) for p in ps)
    assert pairs==6091,pairs
    print(f"PASS primes={len(ps)} corrected_middle_p2_pairs={pairs} "+
          f"full_high_support_primes={sum(p<=103 for p in ps)} "+
          "endpoint_unit_p3=PASS; AUTHOR_CHECKED_NOT_ADMITTED")

if __name__=="__main__":
    main()
