"""Author-level exact original-source D25 terminal/WZ/Cauchy p-adic checker."""
from fractions import Fraction as Q
from math import factorial as fact

def H(n,k=1):
    return sum((Q(1,j**k) for j in range(1,n+1)),Q(0))

def rawU(p):
    m=(p-1)//6; n=4*m
    return Q(fact(6*m)*fact(4*m+2*n)*fact(3*n),p*3**(6*m)*216**n*fact(2*m)*fact(n)**2*fact(2*m+n)**2*fact(4*m+n))

def red(x,p,k):
    M=p**k
    assert x.denominator%p,(p,x.denominator)
    return x.numerator*pow(x.denominator,-1,M)%M

def term(r,n):
    return Q(fact(6*r)*fact(4*r+2*n)*fact(3*n)*(6*n+12*r+1), 3**(6*r)*216**n*fact(2*r)*fact(n)**2*fact(2*r+n)**2*fact(4*r+n))

def W(r):
    return sum((term(r,n) for n in range(4*r+1)),Q(0))

def kA(s):return Q(4*(1-2*s)*(3*s+1),(2*s+1)*(6*s+1))
def kB(s):return Q((2-3*s)*(6*s+1),3*s*(3*s+1))
def a(r,s):return Q(2**(r-s)*fact(2*r)*fact(s-1),fact(r+s)*fact(r-1))
def c(r,s):return Q(fact(2*r+1)*fact(r+s-1),2**(s-1)*fact(r)*fact(2*r+s))
def Z(r):return sum((a(r,s)*kA(s) for s in range(1,r)),Q(0))-Q(1,24)*sum((c(r,s)*kB(s) for s in range(1,2*r)),Q(0))
def D(r):return Q(2**r*fact(2*r),fact(r)*fact(r-1))
def h(r,t):return Q(fact(r)*fact(t-1),2**t*fact(t+r))
def KK(r,s):return Q(1,27*s)/(r+s+Q(1,6))+Q(1,18)/(s+Q(1,3))/(r+s+Q(1,2))-kB(s)/(12*r)
def E(r):return D(r)*sum((h(r,r+s)*KK(r,s) for s in range(1,2*r)),Q(0))
def B(r):return Q(fact(2*r-1)*fact(2*r),fact(4*r))

def RR(m,p):
    C=Q(18*p**4-59*p**3+132*p**2+633*p+248,36*(p-3)*(p-1)*(p+2)*(2*p+1))
    ans=Q(1,2**(p-1))
    for j in range(2*m):ans*=Q(2*j+1-p,2*j+1)
    return C*ans

def G(m):
    r=m+1;z=Q(0)
    for s in range(1,2*m+2):
        t=Q(1,27*s)/(r+s+Q(1,6))
        if s not in (2*m-1,2*m):t+=Q(1,18)/(s+Q(1,3))/(r+s+Q(1,2))
        if s!=2*m:t-=kB(s)/(12*r)
        z+=h(r,r+s)*t
    return D(r)*z

def test(p):
    m=(p-1)//6;M=m+1
    uu=rawU(p)
    q=(108**(p-1)-1)//p;h1=H(2*m); b=H(2*m-1);h2=H(2*m,2);b2=H(2*m-1,2)
    L=4-2*h1-b-q
    U2=4+Q(q*q+L*L,2)-h2+Q(b2,2)
    U_pred=2*m*(1+p*L+p*p*U2)
    assert red(uu-U_pred,p,3)==0
    C=Q((2*p-1)**2*(3*m+1)*(360*m*m+274*m+49),9*(4*m+1)*(4*p-1)*(2*m+1)*(8*m+3))
    C_pred=-2+Q(3,4)*p-Q(393,40)*p*p
    assert red(C-C_pred,p,3)==0
    J=Q(7,4)-Q(4,3)*h1-Q(2,3)*b-Q(2,3)*q
    J2=Q(141,40)-Q(11,12)*L+Q(2,3)*U2
    edgeold=uu*C
    edgepred=Q(2,3)+p*J+p*p*J2
    assert red(edgeold-edgepred,p,3)==0,(p,'edge digit3',red(edgeold-edgepred,p,3))
    e=[term(M,4*m+j) for j in range(1,5)]
    assert all(red(x/p**2,p,2)>=0 for x in e)
    edge=W(M)-W(m)
    assert edge==p*edgeold+sum(e)
    DH=Z(M)-Z(m)
    lam=DH+Q(82,p)
    assert red(p*DH+82,p,1)==0
    omega=(edge+Q(p*p,123)*DH)/p**2
    omega_pred=J+p*J2+sum((x/p**2 for x in e),Q(0))+lam/123
    assert red(omega-omega_pred,p,2)==0
    rr=RR(m,p); gg=G(m); em=E(m)
    assert gg==E(M)-rr/p
    T=(rr-Q(31,27))/p
    c0=Q(31,27);c1=Q(1031,648);c2=Q(4087,3888)
    q2=(2**(p-1)-1)//p
    w=q2+h1/2
    t0=c1-c0*w
    t1=c2-c1*w+c0*(q2**2+q2*h1/2+(h1*h1-3*h2)/8)
    assert red(T-t0-p*t1,p,2)==0
    xi=6*T+rr+(p+6)*gg-p*em
    xi_pred=c0+6*t0+6*gg+p*(t0+6*t1+gg-em)
    assert red(xi-xi_pred,p,2)==0
    d=(B(M)-B(m))*p*em+B(M)*xi
    gap=omega-d
    gap_pred=(J+p*J2+sum((x/p**2 for x in e),Q(0))+lam/123-
              B(M)*(c0+6*t0+6*gg+p*(t0+6*t1+gg))+p*B(m)*em)
    assert red(gap-gap_pred,p,2)==0,(p,'gap',red(gap-gap_pred,p,2))
    return p,red(uu,p,3),red(J2,p,1),red(omega,p,2),red(gap,p,2)

if __name__=='__main__':
    for p in (13,19,31,37,43,61,67,73,79,97,103,127,211):
        print(*test(p))
