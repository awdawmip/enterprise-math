#!/usr/bin/env python3
"""D25 author-side exact Cauchy/Gauss defect certificates (2026-11-02).

Arithmetic is entirely in Z/p^2 Z and F_p. No native H0/B0 experiment
or project mathematical admission is claimed.
"""
from math import comb, isqrt


def primes_upto(n):
    ok = bytearray(b'\x01') * (n + 1)
    ok[:2] = b'\x00\x00'
    for q in range(2, isqrt(n) + 1):
        if ok[q]:
            ok[q * q::q] = b'\x00' * ((n - q * q) // q + 1)
    return [i for i in range(2, n + 1) if ok[i]]


def coefficientwise_test(p):
    """Check polynomial congruences coefficient by coefficient at selected p."""
    mod = p * p
    f = g = h = b = 1
    Fs, Gs, Hs, Bs = [1], [1], [1], [1]
    for k in range(1, p):
        f = f * (2 * k - 1) * (3 * k - 2) * (3 * k - 1) * pow(18 * k**3, -1, mod) % mod
        g = g * (6 * k - 5) * (3 * k - 2) * pow(18 * k**2, -1, mod) % mod
        h = h * (6 * k - 1) * (3 * k - 1) * pow(18 * k**2, -1, mod) % mod
        b = b * (2 * k - 1) * pow(2 * k, -1, mod) % mod
        Fs.append(f); Gs.append(g); Hs.append(h); Bs.append(b)
    sq = [0] * (2 * p - 1)
    gh = [0] * (2 * p - 1)
    bg = [0] * (2 * p - 1)
    for i in range(p):
        for j in range(p):
            sq[i + j] = (sq[i + j] + Gs[i] * Gs[j]) % mod
            gh[i + j] = (gh[i + j] + Gs[i] * Hs[j]) % mod
            bg[i + j] = (bg[i + j] + Bs[i] * Gs[j]) % mod
    assert sq[:p] == Fs, (p, 'Clausen source coefficients')
    assert all(v == 0 for v in sq[p:]), (p, 'Clausen high tail')
    assert all(v == 0 for v in gh[p:]), (p, 'Euler Cauchy high tail')
    assert all((bg[i] - (Hs[i] if i < p else 0)) % p == 0
               for i in range(2 * p - 1)), (p, 'Euler mod p defect integrality')
    return (p, len(sq), len(gh))


def prime_observers(p):
    assert p >= 7 and p % 6 == 1
    mod = p * p
    r = (p - 1) // 6
    n = 2 * r
    A = [1] * p   # F_p at z=1/2
    B = [1] * p   # (1-z)^-1/2 at z=1/2
    G = [1] * p   # _2F1(1/6,1/3;1;z), z=1/2
    H = [1] * p   # _2F1(5/6,2/3;1;z), z=1/2
    for k in range(1, p):
        A[k] = A[k-1]*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3, -1, mod) % mod
        B[k] = B[k-1]*(2*k-1)*pow(4*k, -1, mod) % mod
        G[k] = G[k-1]*(6*k-5)*(3*k-2)*pow(36*k*k, -1, mod) % mod
        H[k] = H[k-1]*(6*k-1)*(3*k-1)*pow(36*k*k, -1, mod) % mod
    def moments(vals):
        return [sum(pow(k,t)*v for k,v in enumerate(vals)) % mod for t in range(3)]
    f,b,g,h = (moments(x) for x in (A,B,G,H))
    assert f[0] == g[0]*g[0] % mod, (p, 'Clausen at observer')
    assert f[1] == 2*g[0]*g[1] % mod, (p, 'Clausen theta')
    assert f[2] == (2*g[1]*g[1] + 2*g[0]*g[2]) % mod, (p, 'Clausen theta2')
    # Complement of the exact p x p Cauchy square with n=m+j >= p.
    prefix = [[0] * (p+1) for _ in range(3)]
    for j in range(p):
        for t in range(3):
            prefix[t][j+1] = (prefix[t][j] + pow(j,t)*B[j]) % mod
    J = [0,0,0]
    for m,am in enumerate(A):
        q0 = (prefix[0][p] - prefix[0][p-m]) % mod
        q1 = (prefix[1][p] - prefix[1][p-m]) % mod
        q2 = (prefix[2][p] - prefix[2][p-m]) % mod
        J[0] = (J[0] + am*q0) % mod
        J[1] = (J[1] + am*(m*q0+q1)) % mod
        J[2] = (J[2] + am*(m*m*q0+2*m*q1+q2)) % mod
    # Product of Gauss factors preserves all tested theta moments mod p^2.
    C = [(b[0]*f[0]-J[0]) % mod,
         (b[1]*f[0]+b[0]*f[1]-J[1]) % mod,
         (b[2]*f[0]+2*b[1]*f[1]+b[0]*f[2]-J[2]) % mod]
    gh = [(g[0]*h[0]) % mod,
          (g[1]*h[0]+g[0]*h[1]) % mod,
          (g[2]*h[0]+2*g[1]*h[1]+g[0]*h[2]) % mod]
    assert C == gh, (p, 'truncated Cauchy equals Gauss product')
    # B_p G_p - H_p has coefficients divisible by p, by Euler mod p.
    numerator = [(b[0]*g[0]-h[0]) % mod,
                 (b[1]*g[0]+b[0]*g[1]-h[1]) % mod,
                 (b[2]*g[0]+2*b[1]*g[1]+b[0]*g[2]-h[2]) % mod]
    assert all(x % p == 0 for x in numerator), (p, 'defect jet integrality')
    E = [x // p % p for x in numerator]
    # Direct independent one-carry kernel with source labels (m, p-s).
    q0=q1=q2=0
    K=[0,0,0]
    for m in range(1,n+1):
        u = -pow(4*m*(B[m] % p), -1, p) % p
        q0=(q0+u)%p; q1=(q1+m*u)%p; q2=(q2+m*m*u)%p
        K[0] = (K[0] + A[m]*q0) % p
        K[1] = (K[1] + A[m]*(m*q0-q1)) % p
        K[2] = (K[2] + A[m]*(m*m*q0-2*m*q1+q2)) % p
    assert all(J[t] == p*K[t] % mod for t in range(3)), (p, 'source reflected carry')
    jet=[g[0]*E[0] % p,
         (g[1]*E[0]+g[0]*E[1]) % p,
         (g[2]*E[0]+2*g[1]*E[1]+g[0]*E[2]) % p]
    assert K==jet, (p, 'moment defect factorization',K,jet)
    if p % 24 in (13,19):
        assert g[0] % p == 0, (p, 'CM zero only finite tested')
        assert K[0] == 0
        assert K[1] == (-pow(2,-1,p)) % p, (p, 'finite conjecture K1')
        assert K[1] == g[1]*E[0] % p, (p,'local derivative certificate')
    return (p, p%24, g[0]%p, g[1]%p, E[0], K[0], K[1], K[2])


def main():
    samples=[7,13,19,31,37,43,61]
    for p in samples:coefficientwise_test(p)
    cases=[p for p in primes_upto(3000) if p%6==1]
    targets=[p for p in cases if p%24 in (13,19)]
    sample_set={7,13,19,31,37,43,61,373,1171}
    table=[]
    for p in cases:
        v=prime_observers(p)
        if p in sample_set:table.append(v)
    print('2026-11-02 D25 GAUSS_DEFECT_EXACT_CHECK')
    print('coefficientwise polynomial tests primes:',samples,'PASS')
    print('all p=1 mod 6 primes <=3000:',len(cases),'PASS')
    print('target p=13/19 mod 24 primes <=3000:',len(targets),'PASS')
    print('verified: Clausen p², Euler/Cauchy p², defect E[0..2], raw triangle J[0..2], reflected K[0..2], CM vanishing in finite targets')
    print('finite-only observation on targets: K0=0, K1=-1/2 mod p')
    print('p class Umodp thetaUmodp E0 K0 K1 K2')
    for v in table:print(*v)
    print('END PASS: exact modular integer arithmetic; no native experiment, independent review, or project admission')

if __name__ == '__main__': main()
