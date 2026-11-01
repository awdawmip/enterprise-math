#!/usr/bin/env python3
"""Author-side exact CM/curvature cross-check for D25 GH-113/GH-114.

All finite-field arithmetic uses integer modular inverses; no native
Enterprise Math run or independent theorem acceptance is implied.
"""
from fractions import Fraction
from math import comb, isqrt


def primes_under(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(bound-1)+1):
        if sieve[q]:
            sieve[q*q:bound:q] = b'\x00' * (((bound-1-q*q)//q)+1)
    return [p for p in range(11,bound) if sieve[p] and p % 8 == 3]


def qadd(x,y): return (x[0]+y[0], x[1]+y[1])
def qneg(x): return (-x[0],-x[1])
def qmul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qinv(x):
    n=x[0]*x[0]-2*x[1]*x[1]
    return (x[0]/n, -x[1]/n)
def qdiv(x,y): return qmul(x,qinv(y))


def cm_invariant_exact():
    one=(Fraction(1),Fraction(0))
    T=(Fraction(0),Fraction(2,3))  # T = 2 sqrt(2) / 3
    def scaler(k,x):return (k*x[0],k*x[1])
    b=scaler(Fraction(1,8),qadd(one,T))
    c4=scaler(16,qadd(one,scaler(-3,b)))
    delta=scaler(16,qmul(qmul(b,b),qadd(one,scaler(-4,b))))
    j=qdiv(qmul(qmul(c4,c4),c4),delta)
    assert j == (Fraction(2417472), Fraction(-1707264)),j
    trace=2*j[0]
    norm=j[0]*j[0]-2*j[1]*j[1]
    assert (trace,norm)==(4834944,14670139392)
    print('CM exact j(T)=',j,'H_{-24}=X^2-',trace,'X+',norm)


def legendre_even_value(p,m):
    # P_(2m)(t) with t^2=8/9, computed in Fp[t]/(t^2-y)
    y=8*pow(9,-1,p)%p
    pnm1=(1,0)
    pn=(0,1)
    for n in range(1,2*m):
        tpn=(pn[1]*y%p, pn[0])
        pn1=tuple(((2*n+1)*tpn[i]-n*pnm1[i])*pow(n+1,-1,p)%p for i in (0,1))
        pnm1,pn=pn,pn1
    assert pn[1]==0
    return pn[0]


def f_value_derivative(p,m):
    f=1; val=1; deriv=0
    for r in range(m):
        f=f*(r-m)**2*pow((r+2*m+2)*(r+1),-1,p)%p
        val=(val+f*pow(9,r+1,p))%p
        deriv=(deriv+(r+1)*f*pow(9,r,p))%p
    return val,deriv


def reflected_h_and_derivative(p,m):
    d=2*m
    h=1; H=0; Hp=0; r2=0
    zpower=1; zprev=0
    for j in range(d+1):
        H=(H+(8*j+5)*h*zpower)%p
        if j:
            Hp=(Hp+j*(8*j+5)*h*zprev)%p
        if j<d:
            h=h*(4*j+3)**3*pow((4*j+4)*(4*j+5)*(4*j+6),-1,p)%p
            zprev,zpower=zpower,zpower*9%p
    r2=(d*pow(9,d-1,p)*H+pow(9,d,p)*Hp)%p
    return H,Hp,r2


def r_value_mod_p2_at_3347():
    p=3347; mod=p*p;d=(p-3)//4
    h=1; acc=0; zpow=pow(9,d+1,mod)
    for j in range(d+1):
        n=d+1+j
        acc=(acc+(8*j+5)*h*pow(n,-1,mod)*zpow)%mod
        if j<d:
            h=h*(4*j+3)**3*pow((4*j+4)*(4*j+5)*(4*j+6),-1,mod)%mod
            zpow=zpow*9%mod
    assert acc==3969542 and acc//p==1186
    return acc


def check_prime(p):
    assert p>=11 and p%8==3
    m=(p-3)//8
    D=comb(3*m+1,m)%p
    assert D
    F,Fp=f_value_derivative(p,m)
    G=D*F%p
    Gp=D*Fp%p
    A=(144*Gp+5*G)%p
    E=legendre_even_value(p,m)
    assert G==pow(9,m,p)*E%p,('Hasse bridge',p,G,E)
    assert (G==0)==(p%24==19),('CM split/inert classification',p,G)
    H,Hp,R2=reflected_h_and_derivative(p,m)
    assert H==0,('GH83 author-side H_ref(9) input',p,H)
    assert H==(G*A*pow(D,-2,p))%p,('GH100',p)
    assert R2==pow(9,2*m,p)*Hp%p,('reflected R second derivative',p)
    assert R2!=0,('not simple stationary point',p)
    assert pow(R2,(p-1)//2,p)==1,('curvature squareclass',p,R2)
    if p%24==19:  # CM-inert zero: G(9)=0 and G'(9) !=0.
        assert G==0 and Gp!=0 and A!=0
        predicted=(12*pow(9,m,p)*Gp*pow(D,-1,p))**2%p
        tag='CM_INERT_G_ZERO'
    else:  # CM-split unit: A(9)=0; exact A'(9)=-G(9)/288.
        assert G!=0 and A==0
        # G'' evaluated from its hypergeometric ODE at z=9.
        Gpp=-(9*pow(64,-1,p)*G+29*pow(2,-1,p)*Gp)*pow(72,-1,p)%p
        Ap=(21*Gp+144*Gpp)%p
        assert Ap==(-G*pow(288,-1,p))%p,('A derivative',p,Ap)
        predicted=(-pow(9,2*m,p)*F*F*pow(288,-1,p))%p
        tag='CM_SPLIT_A_ZERO'
    assert R2==predicted,('curvature formula',p,R2,predicted)
    return p,tag,E,R2


def main():
    cm_invariant_exact()
    test_primes=primes_under(3000)
    test_primes.append(3347)
    split=inert=0
    for p in test_primes:
        p,tag,E,R2=check_prime(p)
        split+=tag=='CM_SPLIT_A_ZERO'; inert+=tag=='CM_INERT_G_ZERO'
        if p in (11,19,43,59,3347): print('p',p,'type',tag,'E',E,'Rsecond(9)',R2)
    assert 3347 in test_primes
    v=2331;u=1186;c=1465;p=3347
    assert r_value_mod_p2_at_3347()==p*u
    assert (-2*u*pow(v,-1,p))%p==c
    assert pow(u,(p-1)//2,p)==p-1
    assert pow(v,(p-1)//2,p)==1
    assert (c*pow(u,-1,p))%p==1052**2%p
    assert 2*40**2+3*7**2==p
    print('3347 valuation-one residue',u,'curvature',v,'old ramification c',c,
          'square-class c/u',1052,'prime form 2*40^2+3*7^2')
    print('PASS_GH113_GH114_CM_REFLECTED_CURVATURE',
          'p_count',len(test_primes),'split',split,'inert',inert)


if __name__=='__main__': main()
