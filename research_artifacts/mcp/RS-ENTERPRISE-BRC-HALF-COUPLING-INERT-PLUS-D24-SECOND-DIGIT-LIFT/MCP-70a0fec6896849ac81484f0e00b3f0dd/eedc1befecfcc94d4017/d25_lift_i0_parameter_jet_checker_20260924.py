from fractions import Fraction
from math import comb, factorial

def rf(a,k):
    z=Fraction(1)
    for j in range(k): z*=a+j
    return z

def u(n,k):
    return Fraction(6*k+1)*rf(Fraction(1,2),k)*rf(Fraction(-n),k)*rf(Fraction(2,3),k)/(factorial(k)**3*2**k)

def a(k):
    return Fraction(6*k+1)*rf(Fraction(1,2),k)*rf(Fraction(2,3),k)/(factorial(k)**2*2**k)

def AB(n,k):
    A=sum((Fraction(1,j) for j in range(n-k+1,n+1)),Fraction(0))
    B=sum((Fraction(1,j*j) for j in range(n-k+1,n+1)),Fraction(0))
    return A,B

def derivative_coeffs(n,k):
    # Direct polynomial product P(eps)=(-n+eps)_k; return P(0),P'(0),P''(0).
    poly=[Fraction(1)]
    for j in range(k):
        c=Fraction(-n+j)
        nxt=[Fraction(0)]*(len(poly)+1)
        for d,v in enumerate(poly):
            nxt[d]+=v*c
            nxt[d+1]+=v
        poly=nxt
    p0=poly[0]
    p1=poly[1] if len(poly)>1 else Fraction(0)
    p2=2*poly[2] if len(poly)>2 else Fraction(0)
    return p0,p1,p2

def check_derivative_and_binomial(n):
    U0=Fraction(0)
    U0b=Fraction(0)
    for k in range(n+1):
        A,B=AB(n,k)
        p0,p1,p2=derivative_coeffs(n,k)
        assert p0==rf(Fraction(-n),k)
        assert p1==-p0*A
        assert p2==p0*(A*A-B)
        U0+=u(n,k)
        U0b+=(-1)**k*comb(n,k)*a(k)
    assert U0==U0b

def check_reflection(n):
    assert n%2==0
    for k in range(n+1):
        uk=u(n,k); uj=u(n,n-k)
        rho=Fraction(6*(n-k)+1,6*k+1)*Fraction(2**(2*k),2**n)
        rho*=rf(Fraction(1,2),n-k)/rf(Fraction(1,2),k)
        rho*=rf(Fraction(2,3),n-k)/rf(Fraction(2,3),k)
        rho*=Fraction(factorial(k)**2,factorial(n-k)**2)
        assert uj==uk*rho
        assert rho>0
        assert (uj>0)==(uk>0)
    assert u(n,n//2)!=0

def ycoeff(k):
    # coefficient of t^k in y=(1+6 theta) 2F1(1/2,2/3;1;t)
    return Fraction(6*k+1)*rf(Fraction(1,2),k)*rf(Fraction(2,3),k)/(factorial(k)**2)

def check_y_ode(K=60):
    c=[ycoeff(k) for k in range(K+3)]
    # Coefficient of t^r in
    # 6t(t-1)(6t-1)y'' +(78t^2-19t+6)y' +2(6t-7)y.
    for r in range(K):
        z=Fraction(0)
        # 36 t^3 -42 t^2 +6 t multiplying y''
        for d,coef in ((3,36),(2,-42),(1,6)):
            j=r-d+2
            if j>=2: z+=coef*j*(j-1)*c[j]
        # (78t^2-19t+6)y'
        for d,coef in ((2,78),(1,-19),(0,6)):
            j=r-d+1
            if j>=1: z+=coef*j*c[j]
        # (12t-14)y
        if r>=1: z+=12*c[r-1]
        z-=14*c[r]
        assert z==0,(r,z)

for n in range(0,41,2):
    check_derivative_and_binomial(n)
    check_reflection(n)
check_y_ode()
print('PASS: parameter derivatives, binomial transform, reflection no-go, Gauss-derived ODE')
