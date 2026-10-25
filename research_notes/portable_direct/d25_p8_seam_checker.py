#!/usr/bin/env python3
"""Portable, source-exposed author check for the D25 original WZ p^8 Frobenius seam.
No native Researcher experiment or independent review is implied.
"""
from math import comb, isqrt


def check_prime(p):
    assert p >= 13 and p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1))
    m, n, M, deg = (p - 1) // 6, (p - 1) // 3, p**8, 5

    def P(x): return [x % M] + [0] * deg
    def mul(*factors):
        ans = P(1)
        for b in factors:
            nxt = [0] * (deg + 1)
            for i in range(deg + 1):
                if ans[i]:
                    for j in range(deg + 1 - i):
                        nxt[i+j] = (nxt[i+j] + ans[i]*b[j]) % M
            ans = nxt
        return ans
    def add(*factors): return [sum(a[i] for a in factors) % M for i in range(deg + 1)]
    def inv(b):
        out = [0] * (deg + 1)
        out[0] = pow(b[0], -1, M)
        for k in range(1, deg + 1):
            out[k] = (-out[0] * sum(b[j] * out[k-j] for j in range(1, k+1))) % M
        return out
    def div(a, b): return mul(a, inv(b))
    def power(a, k):
        if k < 0: return power(inv(a), -k)
        out = P(1)
        while k:
            if k & 1: out = mul(out, a)
            a = mul(a, a)
            k >>= 1
        return out
    def lin(c=1, v=0):
        out = P(c)
        out[1] = v % M
        return out
    def f(a, b=1): return a * pow(b % M, -1, M) % M
    def q(c): return (pow(c, p - 1, p**9) - 1) // p

    z = lin(0, 1)
    C = div(mul(lin(1, 1), power(lin(-1, 2), 2), add(P(40), mul(P(77), z), mul(P(30), power(z, 2)))),
            mul(P(2), lin(2, 1), lin(1, 2), lin(-1, 4), lin(5, 4)))
    B, carry = P(0), P(1)
    for j in range(1, 5):
        B = add(B, mul(lin(6*j+7, 6), carry))
        if j < 4:
            num = mul(lin(2*j+3, 2), lin(3*j-1, 2), lin(3*j, 2))
            den = mul(P(4), lin(3*j+1, 2), lin(j+2, 1), lin(3*j+11, 4))
            carry = mul(carry, div(num, den))

    K = mul(power(lin(1, q(108)), -1), power(lin(1, -1), -2))
    for k in range(2, n + 1):
        K = mul(K, power(lin(1, -pow(k, -1, M)), 2))
    for j in range(1, n):
        K = mul(K, power(lin(1, pow(j, -1, M)), -1))
    A = mul(P(2*m), C, K)

    tail = P(1)
    for c, exponent in [(-1, 2), (2, 2), (5, 2), (8, 1), (11, 1)]:
        tail = mul(tail, power(lin(1, pow(c, -1, M)), -exponent))
    tail = mul(tail, power(lin(1, q(2)), -2), power(lin(1, q(3)), -3))
    for j in range(1, n):
        tail = mul(tail, power(lin(1, -pow(j, -1, M)), 2))
    for j in range(1, 6): tail = mul(tail, lin(1, pow(j, -1, M)))
    for j in range(1, 5): tail = mul(tail, lin(1, 2*pow(j, -1, M)))
    tail = mul(tail, lin(1, 2))
    for j in range(1, 3):
        tail = mul(tail, power(lin(1, pow(j, -1, M)), -2))
    for j in range(1, n+5):
        tail = mul(tail, power(lin(1, pow(j, -1, M)), -1))
    L = mul(P(3*pow(220, -1, M)), z, B, tail)

    # Exact original factorial rational products, independently evaluated at z=p.
    Cp = f((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
           2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))
    Bp, carryp = 0, 1
    for j in range(1, 5):
        Bp = (Bp+(6*p+6*j+7)*carryp) % M
        if j < 4:
            carryp = carryp*f((2*p+2*j+3)*(2*p+3*j-1)*(2*p+3*j),
                            4*(2*p+3*j+1)*(p+j+2)*(4*p+3*j+11)) % M
    Ku = pow(1+p*q(108), -1, M)*pow(1-p, -2, M) % M
    for k in range(2, n+1): Ku = Ku*f((k-p)**2, k*k) % M
    for j in range(1, n): Ku = Ku*f(j, j+p) % M
    Ap = 2*m*Cp*Ku % M
    Pp = 1
    for c, exponent in [(-1,2),(2,2),(5,2),(8,1),(11,1)]:
        Pp = Pp*pow(1+p*f(1,c), -exponent, M) % M
    Pp = Pp*pow(1+p*q(2), -2, M)*pow(1+p*q(3), -3, M) % M
    for j in range(1, n): Pp = Pp*f((j-p)**2,j*j) % M
    for j in range(1, 6): Pp = Pp*f(j+p,j) % M
    for j in range(1, 5): Pp = Pp*f(j+2*p,j) % M
    Pp = Pp*(1+2*p) % M
    for j in range(1,3): Pp = Pp*pow(f(j+p,j),-2,M) % M
    for j in range(1,n+5): Pp = Pp*pow(f(j+p,j),-1,M) % M
    Lp = p*f(3,220)*Bp*Pp % M
    Fu = pow(1+p*q(108), -1, M)
    for k in range(2,n+1): Fu = Fu*f((k-p)**2,k*k) % M
    for j in range(1,p-1): Fu = Fu*f((j+p)**2,j*j) % M
    for j in range(1,n): Fu = Fu*f(j,j+p) % M
    T = comb(2*p-1,p-1) % M
    R = f((1-p)**2, 1-2*p)
    source_diff = (2*m*Cp*Fu + T*T*Lp - Ap - Lp) % M
    assert (Fu-T*T*R*R*Ku) % M == 0, ('original old edge',p)
    assert (Ap-sum(a*p**i for i,a in enumerate(A))) % p**6 == 0, ('old edge jet',p)
    assert (Lp-sum(a*p**i for i,a in enumerate(L))) % p**6 == 0, ('tail jet',p)

    # The binomial observer has the *exact* even-harmonic product identity.
    even_product = 1
    for j in range(1,p):
        even_product = even_product * (1-p*p*pow(j*j,-1,M)) % M
    assert T == even_product, ('exact even-factor product',p)
    def harm(k): return sum(pow(pow(j,k,M), -1, M) for j in range(1,p)) % M
    h2,h4,h6 = harm(2),harm(4),harm(6)
    assert h2%p == h4%p == h6%p == 0
    theta, omega, chi = h2//p, h4//p, h6//p
    Tp2 = (1-2*theta*p**3-omega*p**5+2*theta**2*p**6
           -2*pow(3,-1,M)*chi*p**7) % M
    assert T*T%M == Tp2, ('binomial p8 observer',p)
    assert R*R%M == sum(v*p**i for i,v in enumerate([1,0,2,4,9,20,44,96]))%M, ('R2 p8 jet',p)
    a0,a1,a2,a3,a4,a5 = A
    l1,l2,l3,l4 = L[1:5]
    pred = (
        2*a0*p**2
        +(2*a1+(4-2*theta)*a0)*p**3
        +(2*a2+(4-2*theta)*a1+9*a0-2*theta*l1)*p**4
        +(2*a3+(4-2*theta)*a2+9*a1+(20-4*theta-omega)*a0-2*theta*l2)*p**5
        +(2*a4+(4-2*theta)*a3+9*a2+(20-4*theta-omega)*a1
          +(44-8*theta+2*theta**2)*a0-2*theta*l3-omega*l1)*p**6
        +(2*a5+(4-2*theta)*a4+9*a3+(20-4*theta-omega)*a2
          +(44-8*theta+2*theta**2)*a1
          +(96-18*theta-2*omega-2*pow(3,-1,M)*chi)*a0
          -2*theta*l4-omega*l2+2*theta**2*l1)*p**7
    ) % M
    assert source_diff == pred, ('p8 seam',p,source_diff,pred)
    return dict(p=p,seam=pred,modulus=M,
                chi=chi%p,theta=theta%p,omega=omega%p,
                new_oldedge=(96-18*theta-2*omega-2*pow(3,-1,M)*chi)%p,
                new_genuine_tail=(-2*theta*l4-omega*l2+2*theta**2*l1)%p)


def main():
    primes=[p for p in range(13,3000) if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]
    assert len(primes)==206
    data=[check_prime(p) for p in primes]
    for p in (13,19,31,37,109):
        x=next(v for v in data if v['p']==p)
        print(f"p={p}: seam={x['seam']} (mod {x['modulus']}); chi={x['chi']}; "
              f"new old-edge coeff={x['new_oldedge']}; new tail coeff={x['new_genuine_tail']}")
    print(f'PASS {len(data)}/{len(primes)} original-source / jet / even-harmonic / seam p^8 checks')

if __name__ == '__main__': main()