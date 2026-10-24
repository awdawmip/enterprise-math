"""Author-level Fraction reconstruction of distinct D25 original/auxiliary observers."""
from fractions import Fraction as Q
from math import factorial as f

def red(x,p,k=1):
    assert x.denominator % p
    return x.numerator * pow(x.denominator,-1,p**k) % p**k

def term(r,n):
    return Q(f(6*r)*f(4*r+2*n)*f(3*n)*(6*n+12*r+1),
             3**(6*r)*216**n*f(2*r)*f(n)**2*f(2*r+n)**2*f(4*r+n))

def W(r):
    return sum((term(r,n) for n in range(4*r+1)),Q(0))

def kA(s): return Q(4*(1-2*s)*(3*s+1),(2*s+1)*(6*s+1))
def kB(s): return Q((2-3*s)*(6*s+1),3*s*(3*s+1))
def a(r,s): return Q(2**(r-s)*f(2*r)*f(s-1),f(r+s)*f(r-1))
def c(r,s): return Q(f(2*r+1)*f(r+s-1),2**(s-1)*f(r)*f(2*r+s))

def Z(r):
    return sum((a(r,s)*kA(s) for s in range(1,r)),Q(0))-Q(1,24)*sum((c(r,s)*kB(s) for s in range(1,2*r)),Q(0))

def D(r): return Q(2**r*f(2*r),f(r)*f(r-1))
def h(r,t): return Q(f(r)*f(t-1),2**t*f(t+r))
def K(r,s):
    return Q(1,27*s)/(r+s+Q(1,6))+Q(1,18)/(s+Q(1,3))/(r+s+Q(1,2))-kB(s)/(12*r)

def E(r): return D(r)*sum((h(r,r+s)*K(r,s) for s in range(1,2*r)),Q(0))
def B(r): return Q(f(2*r-1)*f(2*r),f(4*r))

def R(m,p):
    C=Q(18*p**4-59*p**3+132*p**2+633*p+248,36*(p-3)*(p-1)*(p+2)*(2*p+1))
    P=Q(1,2**(p-1))
    for j in range(2*m): P*=Q(2*j+1-p,2*j+1)
    return C*P

def Greg(m):
    t=m+1; z=Q(0)
    for s in range(1,2*m+2):
        v=Q(1,27*s)/(t+s+Q(1,6))
        if s not in (2*m-1,2*m): v+=Q(1,18)/(s+Q(1,3))/(t+s+Q(1,2))
        if s!=2*m: v-=kB(s)/(12*t)
        z+=h(t,t+s)*v
    return D(t)*z

def H(n): return sum((Q(1,k) for k in range(1,n+1)),Q(0))
def pf(n,p):
    z=1
    for t in range(1,n+1):
        if t%p: z=z*t%p
    return z

def tau(m,p,j):
    r=m+1;n=4*m+j
    u=lambda k:pf(k,p)
    N=4*(6*n+12*r+1)*u(6*r)*u(4*r+2*n)*u(3*n)
    V=pow(3,6*r,p)*pow(216,n,p)*u(2*r)*u(n)**2*u(2*r+n)**2*u(4*r+n)
    return N*pow(V%p,-1,p)%p

def test(p):
    assert p>=13 and (p-1)%6==0
    m=(p-1)//6; t=m+1
    # Independent factorial vs original n-ratio, not an auxiliary replacement.
    A=Q(f(6*m),3**(6*m)*f(2*m)**3); nratio=Q(1); w2=Q(0)
    for n in range(4*m+1):
        w2+=A*(6*n+12*m+1)*nratio
        nratio*=Q((4*m+2*n+1)*(3*n+1)*(3*n+2),36*(n+1)*(2*m+n+1)*(4*m+n+1))
    assert w2==W(m)
    edge=W(t)-W(m); high=Z(t)-Z(m); lam=high+Q(82,p)
    omega=(edge+Q(p*p,123)*high)/p**2
    rr=R(m,p); g=Greg(m); assert g==E(t)-rr/p
    T=(rr-Q(31,27))/p; xi=6*T+rr+(p+6)*g-p*E(m)
    d=(B(t)-B(m))*p*E(m)+B(t)*xi; gap=omega-d
    assert red(p*high,p)==red(Q(-82),p)
    assert red(edge/p,p)==red(Q(2,3),p)
    q2=(2**(p-1)-1)//p; q108=(108**(p-1)-1)//p
    j=Q(7,4)-Q(4,3)*H(2*m)-Q(2,3)*H(2*m-1)-Q(2,3)*q108
    tails=[tau(m,p,k) for k in range(1,5)]
    for k,x in enumerate(tails,1): assert red(term(t,4*m+k)/p**2,p)==x
    xi_first=Q(385,36)-Q(62,9)*q2-Q(31,9)*H(2*m)+6*g
    prediction=j+sum(tails)+lam/Q(123)-B(t)*xi_first
    assert red(xi,p)==red(xi_first,p)
    assert red(omega,p)==red(j+sum(tails)+lam/Q(123),p)
    assert red(gap,p)==red(prediction,p)
    return p,red(omega,p),red(xi,p),red(d,p),red(gap,p),red(omega,p,2),red(d,p,2),red(gap,p,2)

if __name__=='__main__':
    for p in (13,19,31,37,43,61,67,73,79,97,103,127,211): print(test(p))
