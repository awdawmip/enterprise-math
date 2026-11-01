#!/usr/bin/env python3
"""Independent author exact checks: finite-log moment compression and polynomial contact lift.
Finite-field integer arithmetic only. The script is not a native Enterprise Math experiment.
"""
from math import comb


def is_prime(p):
    return p >= 2 and all(p % q for q in range(2, int(p**0.5) + 1))


def legendre_even_descent(p):
    """Independent P_d(T)=(even polynomial)=E(T**2) coefficient recurrence."""
    d = (p - 3) // 4
    prev, cur = [1], [0, 1]
    for n in range(1, d):
        nex = [0] * (len(cur) + 1)
        for j, c in enumerate(cur):
            nex[j+1] = (nex[j+1] + (2*n+1)*c) % p
        for j, c in enumerate(prev):
            nex[j] = (nex[j] - n*c) % p
        inv = pow(n + 1, -1, p)
        prev, cur = cur, [c * inv % p for c in nex]
    assert len(cur) == d + 1 and not any(cur[1::2])
    assert sum(cur) % p == 1
    return cur[::2]


def poly_eval(coeffs, a, p):
    r = 0
    for c in reversed(coeffs):
        r = (r*a+c) % p
    return r


def poly_product(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % p
    return out


def reflected_coeffs(p):
    d = (p-3)//4
    h = [1]
    for j in range(d):
        h.append(h[-1] * pow(4*j+3, 3, p) *
                 pow((4*j+4)*(4*j+5)*(4*j+6), -1, p) % p)
    return h


def trim(x):
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x


def poly_mod(a, b, p):
    x = trim(a[:]); y = trim(b[:]); iy = pow(y[-1], -1, p)
    while len(x) >= len(y) and any(x):
        t = x[-1]*iy % p
        off = len(x)-len(y)
        for j, z in enumerate(y):
            x[off+j] = (x[off+j]-t*z) % p
        trim(x)
    return x


def test_one(p, direct=False):
    d, m, N = (p-3)//4, (p-3)//8, (p-1)//2
    E = legendre_even_descent(p)
    D = comb(3*m+1, m) % p
    assert D != 0 and E[-1] != 0
    # B(r)=E(1-r)**2; G(z)=z**m*E(1-z**(-1))
    er = [0] * (m+1)
    for k, ek in enumerate(E):
        for j in range(k+1):
            er[j] = (er[j]+ek*comb(k,j)*(-1)**j) % p
    b = poly_product(er, er, p)
    G = [er[m-j] for j in range(m+1)]
    U = poly_product(G,G,p)
    dinv2 = pow(D,-2,p)
    h = reflected_coeffs(p)
    assert [u*dinv2 % p for u in U] == h
    assert G[0] == D and G[-1] == 1 and poly_eval(G,1,p) != 0
    # GH-102 exact character-sum polynomial, expressed without field enumeration.
    M = [0] * (N+1)
    for j, bj in enumerate(b):
        M[N-j] = -bj * pow(N-j,-1,p) % p
    assert M[:d+1] == [0]*(d+1) and M[d+1] != 0
    assert M[N] == 2
    # M'(z) == -z**d G(z)**2, complete polynomial equality.
    mp = [(i*M[i]) % p for i in range(1,len(M))]
    assert mp == [0]*d + [(-u)%p for u in U]
    # GH-103: polynomial contact C(z)=8*z**(d+1)*G(z)**2.
    C = [0]*(N+1)
    for j,u in enumerate(U): C[d+1+j]=8*u%p
    R = [0]*(N+1)
    for j,hj in enumerate(h):
        R[d+1+j]=(8*j+5)*hj*pow(d+1+j,-1,p)%p
    assert all((C[j]-3*M[j]-D*D*R[j])%p==0 for j in range(N+1))
    # G has only simple algebraic roots, not just no roots in F_p.
    Gp=[j*G[j]%p for j in range(1,len(G))]
    if len(Gp)>0:
        x,y=G[:],trim(Gp)
        while any(y):
            x,y=y,poly_mod(x,y,p)
        assert len(trim(x))==1,(p,x)
    if direct:
        checks = list(range(p)) if p<=67 else [0,1,2,9,p-1]
        for a in checks:
            total=0
            for r in range(1,p):
                e=poly_eval(E,(1-r)%p,p)
                x=a*r%p
                numerator=(1-pow(x,p,p*p)-pow((1-x)%p,p,p*p))%(p*p)
                assert numerator % p == 0
                finite_log=numerator//p
                total=(total+pow(r,N,p)*e*e*finite_log)%p
            assert total==poly_eval(M,a,p),(p,a,total,poly_eval(M,a,p))
    if p==3347:
        a=9
        derivative=lambda v:[j*v[j]%p for j in range(1,len(v))]
        S=[sum(v*pow(a,j,p) for j,v in enumerate(q))%p for q in (M,C,R)]
        M1=poly_eval(derivative(M),a,p)
        C1=poly_eval(derivative(C),a,p)
        R1=poly_eval(derivative(R),a,p)
        R2=poly_eval(derivative(derivative(R)),a,p)
        Delta2=(C1-3*M1)%p
        assert S==[1568,1357,0],S
        assert M1==2166 and C1==3151 and R1==0 and R2==2331
        assert Delta2==0
        assert (poly_eval(derivative(derivative(C)),a,p)-3*poly_eval(derivative(derivative(M)),a,p))%p == 914
        print('p3347: d,m,N,D,G(9),M(9),C(9),R(9),Mprime,Cprime,Rprime,Rsecond,Delta_second',d,m,N,D,poly_eval(G,a,p),*S,M1,C1,R1,R2,914)
    return 1


def main():
    primes=[p for p in range(11,1500,8) if is_prime(p)]+[3347]
    for p in primes:
        test_one(p, direct=(p<=67 or p in (83,131,251,3347)))
    print('PASS_GH102_GH103:',len(primes),'primes, complete polynomial coefficient identities, exact G squarefree checks; direct Fermat-quotient finite-log traces selected')

if __name__=='__main__':
    main()
