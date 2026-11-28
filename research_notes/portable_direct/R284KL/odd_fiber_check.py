from fractions import Fraction as F
from math import prod
from sympy import primerange

def poly(m,cs):
    r=0
    for c in cs:r=r*m+c
    return r
F7=[96,496,644,4,1015,1751,2356,5316]
J1=[1152,15024,84448,266908,553616,992988,1927441,3272963,3776696,2614884,860400]
J2=[16128,265152,2067436,9650156,29629115,62871098,94168943,99087776,70696900,31297632,6675264]
def coeff(m):
    D=(2*m-1)**2*(2*m+1)**2
    return ((m+2)**2*(4*m+7)*poly(m,F7)/(8*D), -(m+2)*poly(m,J1)/(4*m*(m-1)*D), (m+3)*poly(m,J2)/(8*m*m*(m-1)**2*D))
def boundary(a):
    # d=2a+1. Odd factorial products including both endpoints.
    return F((-1)**a*(2*a+3)*prod(range(1,2*a,2))*prod(range(1,2*a+2,2)),2*prod(range(2*a+5,6*a+6,2)))
def vp(n,p):
    assert n
    e=0
    while n%p==0:n//=p;e+=1
    return e
def val(x,p):return vp(x.numerator,p)-vp(x.denominator,p)
def mod(x,p):
    return x.numerator*pow(x.denominator,-1,p)%p

def direct(d):
    m=F(d-2,2);q=-m-2
    U=[F(1)]
    for k in range(d):U.append(U[-1]*(m-k)/(m+k+3))
    V=Q=A=F(0)
    for k in range(d+1):
        l=d-k;x=(k+1)*(l+1)**2*U[k]*(-1)**l
        y=(k+1)*l*l*U[k]*(-1)**(l-1) if l else 0
        V+=x;Q+=y;A+=(m-k)*(m+k+2)*(x+y)/(2*m*(2*m+1))
    Z=q*A+Q+V
    return (d-m)*(-1)**d*U[d],3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z*Z
count=near=far=near_unit=far_unit=0
for d in range(5,302,2):
    a=(d-1)//2;m=F(d-2,2);B=boundary(a);c0,c1,c2=coeff(m);b,C=direct(d)
    assert B==b and C==c0+c1*B+c2*B*B and 0<C and -c1<128*c0
    assert abs(boundary(a+1))*8<abs(B)
    assert abs(B)<F(1,2048)
    count+=1
    # D0 is JR cleared denominator, n=-2. Verify residue of cleared P0 at both prime regimes.
    D0=2*m*(2*m+1)*(-6)*prod(m+i+3 for i in range(d))*prod(i+1 for i in range(d))
    P0=D0*D0*C
    for p in primerange(2*d+4,5*d+1):
        p=int(p)
        if p<=3*d+2:
            near+=1
            assert val(B,p)==-1 and val(D0,p)==1
            r=mod(c2,p)*mod(p*B,p)**2%p
            assert mod(P0,p)==mod(D0/p,p)**2*r%p
            near_unit+=bool(r)
        else:
            far+=1
            assert val(B,p)==0 and val(D0,p)==0
            r=(mod(c0,p)+mod(c1,p)*mod(B,p)+mod(c2,p)*mod(B,p)**2)%p
            assert mod(P0,p)==mod(D0,p)**2*r%p
            far_unit+=bool(r)
print('odd direct identities',count,'near primes',near,'near nonzero',near_unit,'far primes',far,'far nonzero',far_unit)
