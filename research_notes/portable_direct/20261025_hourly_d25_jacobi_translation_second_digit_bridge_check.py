"""Exact author-side check of the D25 Jacobi-jet translation and corner port.
No CM/Frobenius or native BRC execution; only modular arithmetic.
"""
from math import isqrt


def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for d in range(2, isqrt(limit) + 1):
        if sieve[d]:
            for n in range(d * d, limit + 1, d):
                sieve[n] = False
    return [n for n in range(7, limit + 1) if sieve[n] and n % 6 == 1]


def verify(p):
    m, M = (p - 1) // 6, p**3
    inv2, inv6 = pow(2, -1, M), pow(6, -1, M)
    tau = -p * inv6 % M

    # Independent original-source recurrence, no parameter-jet input.
    r = [1]
    for n in range(p - 1):
        ratio = (6*n + 1) * (3*n + 1) * pow(36*(n + 1)**2, -1, M)
        r.append(r[-1] * ratio % M)
    g = sum(r) % M
    d = sum(n * r[n] for n in range(p)) % M
    h = (g + 12*d) % M

    # Taylor coefficients c[k] = [t^k] b_n(m+t), k = 0,1,2.
    c = [1, 0, 0]
    u, v, w = [], [], []
    F, D = [0]*3, [0]*3
    pow2 = [pow(inv2, n, M) for n in range(p)]
    for n in range(p):
        u.append(c[0]); v.append(c[1]); w.append(c[2])
        for k in range(3):
            F[k] = (F[k] + c[k]*pow2[n]) % M
            D[k] = (D[k] + n*c[k]*pow2[n]) % M
        if n > m:
            assert c[0] == 0
        if n > 2*m:
            assert c[1] == 0
        valuation = 0 if n <= m else (1 if n <= 2*m else 2)
        assert r[n] % p**valuation == 0
        assert r[n] % p**(valuation + 1) != 0
        if n < p - 1:
            a0, a1, a2 = (n-m)*(n-2*m), 4*m-3*n, 2
            inv = pow((n + 1)**2, -1, M)
            c = [c[0]*a0*inv % M,
                 (c[1]*a0+c[0]*a1)*inv % M,
                 (c[2]*a0+c[1]*a1+c[0]*a2)*inv % M]
    H = [(F[k]+12*D[k]) % M for k in range(3)]
    assert g == (F[0]+tau*F[1]+tau*tau*F[2]) % M
    assert h == (H[0]+tau*H[1]+tau*tau*H[2]) % M

    # Original signed ordered Clausen corner, independent of the jet port.
    Q = sum((6*(j+k)+1)*r[j]*r[k]
            for j in range(p) for k in range(max(0,p-j),p)) % M
    assert Q % (p*p) == 0
    T_direct = Q // (p*p)
    inv18 = pow(18, -1, p)
    T_jet = inv18 * sum((6*(j-ell)+1)*u[j]*w[p-ell]
                        *pow2[j]*pow2[p-ell]
                        for j in range(1,m+1)
                        for ell in range(1,j+1)) % p
    assert T_direct == T_jet, (p,T_direct,T_jet)

    if p % 24 in (13, 19):
        assert g % p == 0 and (g*h-p) % (p*p) == 0
        g01 = (F[0]+tau*F[1]) % M
        h01 = (H[0]+tau*H[1]) % M
        assert (g01*h01-p) % (p*p) == 0
        B = ((g01*h01-p) % M) // (p*p)
        jet2_correction = 2*F[2]*H[0]*pow(72,-1,p) % p
        delta = ((g*h-p) % M) // (p*p)
        assert delta == (B + jet2_correction) % p
        defect = (delta-T_jet)%p
        assert defect == (B+jet2_correction-T_jet)%p
        return (p, B, jet2_correction, T_jet, defect)
    return None


if __name__ == '__main__':
    samples = [verify(p) for p in primes_up_to(373)]
    target = [x for x in samples if x is not None]
    print('all eligible primes <=373:',len(samples))
    print('target residue classes:', len(target))
    for result in target:
        if result[0] in (13,19,37,43,61,67,109,139,373):
            print('p,B,jet2,T,defect =',result)
    assert next(x for x in target if x[0]==13) == (13,4,9,0,0)
    assert next(x for x in target if x[0]==19) == (19,1,11,12,0)
    assert next(x for x in target if x[0]==373) == (373,184,12,196,0)
    print('PASS: exact independent source, source-jet, corner and target-bridge identities')
