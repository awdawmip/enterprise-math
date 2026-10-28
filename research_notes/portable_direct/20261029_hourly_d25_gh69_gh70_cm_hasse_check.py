#!/usr/bin/env python3
"""Author-side exact finite-field checks for the GH-69 CM/Hasse bridge.
No native Task execution or independent mathematical admission is implied.
"""
from math import comb, factorial


def primes_below(limit):
    table = bytearray(b'\x01') * limit
    table[:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if table[d]:
            table[d*d:limit:d] = b'\x00' * len(table[d*d:limit:d])
    return [p for p in range(11, limit) if table[p] and p % 8 == 3]


def test_prime(p):
    m = (p - 3) // 8
    n = 2 * m
    N = (p - 1) // 2
    inv = lambda v: pow(v % p, -1, p)
    def plus(x, y): return ((x[0]+y[0]) % p, (x[1]+y[1]) % p)
    def neg(x): return ((-x[0]) % p, (-x[1]) % p)
    def mul(x, y): return ((x[0]*y[0]+2*x[1]*y[1]) % p,
                           (x[0]*y[1]+x[1]*y[0]) % p)
    def scale(x, n): return ((n*x[0]) % p, (n*x[1]) % p)
    def sub(x, y): return plus(x, neg(y))
    def power(x, n):
        t = (1, 0)
        while n:
            if n & 1: t = mul(t, x)
            x = mul(x, x)
            n //= 2
        return t
    Z, O = (0, 0), (1, 0)
    t = (0, 2 * inv(3) % p) # 2 sqrt(2) / 3
    assert mul(t, t) == (8 * inv(9) % p, 0)
    assert power(t, p) == neg(t)
    A = sub(scale(t, -9*inv(2)), (15*inv(2) % p, 0))
    B = sub(scale(t, -9), (7, 0))

    # Hasse invariant = coefficient x^(p-1) in (x^3+A*x+B)^N.
    fac = [1]
    for k in range(1, N + 1): fac.append(fac[-1] * k % p)
    invfac = [inv(x) for x in fac]
    H, Hd = Z, Z
    for i in range((N+1)//2, (2*N)//3 + 1):
        j = 2*N-3*i
        k = 2*i-N
        if min(j,k) < 0: continue
        factor = fac[N] * invfac[i] * invfac[j] * invfac[k] % p
        Hj = mul(power(A,j), power(B,k))
        H = plus(H, scale(Hj, factor))
        # Differentiate the parameter t, not the x coefficient.
        if j:
            Hd = plus(Hd, scale(mul(power(A,j-1), power(B,k)), factor*j*(-9)*inv(2)))
        if k:
            Hd = plus(Hd, scale(mul(power(A,j), power(B,k-1)), factor*k*(-9)))

    # Ordinary Legendre recurrence and its derivative in F_p[sqrt(2)].
    P0, P1 = O, t
    dP0, dP1 = Z, O
    if n == 0: P, dP = P0, dP0
    elif n == 1: P, dP = P1, dP1
    else:
        for r in range(1, n):
            Pinv = inv(r+1)
            Pnext = scale(sub(scale(mul(t,P1),2*r+1),scale(P0,r)), Pinv)
            dPnext = scale(sub(scale(plus(P1,mul(t,dP1)),2*r+1),scale(dP0,r)), Pinv)
            P0, P1 = P1, Pnext
            dP0, dP1 = dP1, dPnext
        P, dP = P1, dP1
    chi = pow(-6 % p, (p-1)//2, p)
    assert chi in (1,p-1)
    assert H == scale(P,chi), (p, 'hasse-polynomial-special',H,P)
    assert Hd == scale(dP,chi), (p, 'hasse-derivative-special', Hd,dP)

    coeff = 1
    F, G = 0, 0
    for r in range(m+1):
        value = coeff * pow(9,r,p) % p
        F = (F+value) % p
        G = (G+(16*r+5)*value) % p
        if r < m:
            coeff = coeff * (m-r)**2 * inv((2*m+2+r)*(r+1)) % p
    D = comb(3*m+1,m) % p
    assert D
    factor = D * inv(pow(9,m,p)) % p
    assert scale(P,1) == (factor * F % p,0), (p,'F-Legendre')
    euler = sub(mul(t,dP),P)
    assert euler == (factor * G % p,0), (p,'G-Legendre')
    H_euler = sub(mul(t,Hd),H)
    assert H_euler == scale(euler,chi)

    # Exact rational family j(t), 2-isogeny modular parametrization.
    # j_1=(u+256)^3/u^2 and j_2=(u+16)^3/u where
    # u=64(1-t)/(1+t), Fricke partner j(-t)=j_2.
    def div(x,y):
        norm = (y[0]*y[0]-2*y[1]*y[1])%p
        assert norm
        return scale(mul(x,(y[0],(-y[1])%p)),inv(norm))
    u = scale(div(sub(O,t),plus(O,t)),64)
    j1 = div(power(plus(u,(256%p,0)),3),power(u,2))
    j2 = div(power(plus(u,(16%p,0)),3),u)
    j1_formula = div(scale(power(plus(scale(t,3),(5,0)),3),64),mul(power(sub(t,O),2),plus(t,O)))
    jminus_formula = div(scale(power(sub((5,0),scale(t,3)),3),64),mul(power(plus(t,O),2),sub(O,t)))
    assert j1 == j1_formula and j2 == jminus_formula
    # j(t0) = 2417472 + 1707264 sqrt(2), Hilbert polynomial D=-24.
    assert j1 == (2417472%p,1707264%p), (p, 'CM j', j1)
    assert sub(sub(power(j1,2),scale(j1,4834944)),(-14670139392%p,0)) == Z
    assert power(j1,p) == j2
    assert (chi == 1) == (p%24==11)
    assert (chi == p-1) == (p%24==19)
    return p, F, G, H, Hd


def main():
    tests = [test_prime(p) for p in primes_below(2000)]
    split = [p for p,F,G,*_ in tests if p%24==11]
    inert = [p for p,F,G,*_ in tests if p%24==19]
    assert all(G==0 for p,F,G,*_ in tests if p%24==11)
    assert all(F==0 for p,F,G,*_ in tests if p%24==19)
    assert len(split)+len(inert)==len(tests)
    print(f'PASS_GH69_HASSE_CM_2ISOGENY {len(tests)} primes p<2000')
    print(f'PASS_GH69_SPLIT_EULER_OBSERVATION {len(split)} p=11 mod24; INERT_F_OBSERVATION {len(inert)} p=19 mod24')
    for p,F,G,H,Hd in tests[:6]:
        print(f'p={p} F(9)={F} G(9)={G} H(t0)={H} Hprime(t0)={Hd}')


if __name__=='__main__': main()
