"""Exact certificates for D25 Heun candidate and p-adic scalar non-transfer.
Standard library only; does not prove the analytic candidate or run native benchmark.
"""
from fractions import Fraction as F
from math import comb, isqrt

def bounds(parameters, zden, n):
    term = s = F(1)
    for k in range(n):
        num = den = 1
        for a,b in parameters:
            num *= b*k+a; den *= b
        term *= F(num, den*(k+1)**3*zden)
        s += term
    num = den = 1
    for a,b in parameters:
        num *= b*n+a; den *= b
    nxt = term*F(num, den*(n+1)**3*zden)
    return s, s+nxt*F(zden,zden-1)

def binomial_path(p):
    M=p**3; ia=pow(216,-1,M); ib=pow(2304,-1,M)
    a=b=0; ta=tb=1
    for k in range(p):
        a=(a+comb(2*k,k)**2*comb(3*k,k)*ta)%M
        b=(b+comb(2*k,k)**2*comb(4*k,2*k)*tb)%M
        ta=ta*ia%M; tb=tb*ib%M
    return a,b

def recurrence_path(p):
    M=p**3; inva=pow(216,-1,M); invb=pow(2304,-1,M)
    a=b=sa=sb=1
    for k in range(1,p):
        invk=pow(k,-1,M)
        a=a*(2*k)*(2*k-1)*(3*k)*(3*k-1)*(3*k-2)*inva*pow(invk,5,M)%M
        b=b*(4*k)*(4*k-1)*(4*k-2)*(4*k-3)*invb*pow(invk,4,M)%M
        sa=(sa+a)%M; sb=(sb+b)%M
    return sa,sb

def main():
    n=110; scale=10**n
    alo,ahi=bounds(((1,2),(1,3),(2,3)),2,350)
    blo,bhi=bounds(((1,4),(1,2),(3,4)),9,120)
    sq=isqrt(2*scale**2)
    dl=alo-F(3,4)*F(sq+1,scale)*bhi
    dh=ahi-F(3,4)*F(sq,scale)*blo
    assert -F(2,10**110)<dl<dh<F(2,10**110)
    expected={19:(2888,2527),373:(9878159,28243187)}
    for p,values in expected.items():
        assert binomial_path(p)==recurrence_path(p)==values
        assert all(v%p**2==0 and v//p**2%p!=0 for v in values)
        print(p,values,tuple(v//p**2 for v in values))
    assert pow(2,9,19)==18
    print("PASS: rational 110-digit interval, independent exact p19/p373 residues")
if __name__=="__main__":
    main()
