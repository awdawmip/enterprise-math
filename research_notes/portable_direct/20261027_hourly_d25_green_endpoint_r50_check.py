"""R50: exact finite Green dual and p-adic boundary pole checks.

Pure stdlib; exact Fraction, labeled W/S transfer and two endpoints.
Checks support a universal symbolic summation-by-parts argument.
"""
from fractions import Fraction


def ab(k):
    a=Fraction((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),36*(6*k+1)*(k+1)**3)
    b=Fraction((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),288*(8*k+1)*(k+1)**3)
    return a,b


def abc(k):
    a,b=ab(k)
    a1,b1=ab(k+1)
    return a-b, a*a1-b*b1, a*b*(a1-b1)


def valuation_integer(a,p):
    if a==0:
        return float('inf')
    a=abs(a)
    n=0
    while a%p==0:
        a//=p
        n+=1
    return n


def valuation_fraction(q,p):
    return valuation_integer(q.numerator,p)-valuation_integer(q.denominator,p)


def check(p):
    H=(3*p-1)//4
    N=H+1
    assert p>=13 and N+1<p
    coeff=[abc(i) for i in range(N)]
    v=[]
    for k in range(N):
        alpha,beta,gamma=coeff[k]
        rhs=Fraction(1) if k==1 else Fraction(0)
        if k>=1:
            rhs+=coeff[k-1][1]*v[k-1]
        if k>=2:
            rhs-=coeff[k-2][0]*v[k-2]
        assert gamma!=0
        v.append(rhs/gamma)
    c1=coeff[N-1][0]*v[N-1]
    c0=coeff[N-2][0]*v[N-2]-coeff[N-1][1]*v[N-1]
    w=s=Fraction(1)
    last={0:(w,s)}
    for k in range(N+1):
        a,b=ab(k)
        w*=a
        s*=b
        if k+1 in (N,N+1):
            last[k+1]=(w,s)
    dN=last[N][0]-last[N][1]
    dN1=last[N+1][0]-last[N+1][1]
    d1=Fraction(85,288)
    assert -(c0*dN+c1*dN1)==d1
    assert valuation_fraction(dN,p)>=3 and valuation_fraction(dN1,p)>=3
    assert min(valuation_fraction(c0,p),valuation_fraction(c1,p))<=-3
    return p,N,valuation_fraction(dN,p),valuation_fraction(dN1,p),valuation_fraction(c0,p),valuation_fraction(c1,p)


def main():
    for p in (13,19,37,181,373):
        print('PASS R50 p,N,v(dN),v(dN+1),v(C0),v(C1)=',check(p))


if __name__=='__main__':
    main()
