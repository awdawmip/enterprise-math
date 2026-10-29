#!/usr/bin/env python3
"""Author-side exact Jacobi p^2 correction and CM Hensel-port witness; not native H0/B0."""
from math import comb, isqrt


def primes(n):
    return [p for p in range(5, n) if all(p % d for d in range(2, isqrt(p) + 1))]


def algebra(p, precision):
    m = p ** precision
    inv36 = pow(36, -1, m)
    def add(x, y):
        return ((x[0]+y[0]) % m, (x[1]+y[1]) % m)
    def scalar(c, x):
        return ((c*x[0]) % m, (c*x[1]) % m)
    def mul(x, y):
        a, b = x; c, d = y
        return ((a*c - b*d*inv36) % m, (a*d+b*c+b*d) % m)
    def inv(x):
        a, b = x
        norm = (a*(a+b)+b*b*inv36) % m
        return scalar(pow(norm, -1, m), (a+b, -b))
    return m, add, scalar, mul, inv


def hasse(p):
    m, add, scalar, mul, _ = algebra(p, 2)
    k, e = (p-1)//2, (p-1)//4
    s = (pow(4,-1,m), -pow(4,-1,m) % m)
    power = (1,0); previous = power
    H = (0,0); derivative = (0,0)
    for j in range(e+1):
        c = comb(k, 2*j)*comb(2*j,j)
        H = add(H, scalar(c, power))
        if j:
            derivative = add(derivative, scalar(-j*c*pow(4,-1,m), previous))
        previous, power = power, mul(power, s)
    return H, derivative


def companion(p):
    mod = p*p
    hits = [next(j for j in range(p) if (8*j+q) % p == 0) for q in (1,3)]
    a=1; K=D=0
    for j in range(max(hits)+1):
        K=(K+a)%mod; D=(D+j*a)%mod
        if j<max(hits):
            a=a*(8*j+1)*(8*j+3)*pow(576*(j+1)**2,-1,mod)%mod
    return K,D


def verify_jacobi(p):
    """Coefficientwise: H_p=P_e(2t-1)-p/2*M_e(1-t) mod p^2."""
    m=p*p; k=(p-1)//2; e=(p-1)//4
    base=1; harmonic=0; inv4=pow(4,-1,m)
    for j in range(e+1):
        lhs=comb(k,2*j)*comb(2*j,j)*pow(inv4,j,m)%m
        rhs=base*(1 - p*pow(2,-1,m)*harmonic)%m
        assert lhs==rhs, (p,j,lhs,rhs)
        if j<e:
            base=base*(-e+j)*(e+1+j)*pow((j+1)**2,-1,m)%m
            harmonic=(harmonic+pow(e+1+j,-1,m))%m


def legendre_and_derivative(p):
    """Legendre P_e(x), P_e'(x) in F_p[t]/(36t^2-36t+1)."""
    _,add,sc,mul,_=algebra(p,1)
    x=(-1%p,2%p); P0=(1,0); P1=x; D0=(0,0); D1=(1,0)
    e=(p-1)//4
    if e==0: return P0, D0
    for n in range(1,e):
        P2=sc(pow(n+1,-1,p),add(sc(2*n+1,mul(x,P1)),sc(-n,P0)))
        D2=sc(pow(n+1,-1,p),add(sc(2*n+1,add(P1,mul(x,D1))),sc(-n,D0)))
        P0,P1,D0,D1=P1,P2,D1,D2
    return P1,D1


def verify_parity(p):
    H,dH=hasse(p)
    P,dP=legendre_and_derivative(p)
    _,add,sc,_,_=algebra(p,1)
    assert (H[0]%p,H[1]%p)==P
    assert (dH[0]%p,dH[1]%p)==sc(2,dP)
    e=(p-1)//4
    if e%2:
        assert dH[1]%p==0, (p,dH)
    else:
        assert (2*dH[0]+dH[1])%p==0, (p,dH)


def verify_hensel(p):
    """Hasse-only lift alters the originally fixed z=1/9 when K is a simple root."""
    m,add,sc,mul,inv=algebra(p,1)
    H,dH=hasse(p); K,D=companion(p)
    assert H[0]%p==H[1]%p==0 and K==0 and D%p!=0
    h=(H[0]//p,H[1]//p)
    d=(dH[0]%p,dH[1]%p)
    delta=sc(-1,mul(h,inv(d)))
    dz=sc(4,mul(add((1,0),sc(-2,(0,1))),delta))
    shift_port=sc(9*D,dz)
    assert delta!=(0,0) and dz!=(0,0) and shift_port!=(0,0)
    # Independent direct polynomial evaluation at the corrected Hasse root.
    mm,add2,sc2,mul2,_=algebra(p,2)
    t_shift=add2((0,1),sc2(p,delta))
    s_shift=sc2(pow(4,-1,mm),add2((1,0),sc2(-1,t_shift)))
    H_shift=(0,0); power=(1,0); k=(p-1)//2
    for j in range((p-1)//4+1):
        H_shift=add2(H_shift,sc2(comb(k,2*j)*comb(2*j,j),power))
        power=mul2(power,s_shift)
    assert H_shift==(0,0)
    assert (H[0]//p,H[1]//p)==h
    # Companion Taylor port: K(z+p dz)=K(z)+p dz*K'(z), K'(1/9)=9*theta K.
    assert K==0
    return (h,d,delta,dz,shift_port)


def main():
    checked=primes(400)
    for p in checked:
        verify_jacobi(p)
        verify_parity(p)
    for p in [13,23,37,47,61,71,109,157,181,229,373]:
        verify_hensel(p)
    assert verify_hensel(13)==((2,4),(6,0),(4,8),(12,1),(5,8))
    assert verify_hensel(23)==((21,9),(11,0),(19,18),(11,6),(10,18))
    assert verify_hensel(373)==((14,28),(180,0),(203,33),(322,109),(316,56))
    print(f'PASS_JACOBI_FIRST_ORDER_AND_DERIVATIVE_EIGENLINE {len(checked)} primes <400')
    print('PASS_SOURCE_PRESERVING_HENSEL_PORT_OBSTRUCTION p=13,23,373')

if __name__=='__main__':
    main()
