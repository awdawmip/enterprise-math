"""Author-side exact checks for the D24/D25 second-digit Clausen cutoff bridge.

No native Source/CLAIM/Driver assertion. Arithmetic uses only Z/(p^3)Z
with unit inverses, and an independent F_p binomial reflection.
"""
from math import comb, isqrt


def primes_under(n):
    for p in range(13, n):
        if p % 24 not in (13, 19):
            continue
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def direct_quantities(p):
    M = p ** 3
    b, w = [1], [1]
    for k in range(p - 1):
        b.append(b[-1] * (6*k + 1) * (3*k + 1) *
                 pow(36*(k+1)**2, -1, M) % M)
        w.append(w[-1] * (2*k + 1) * (3*k + 1) * (3*k + 2) *
                 pow(36*(k+1)**3, -1, M) % M)
    g = sum(b) % M
    h = sum((12*k+1)*a for k,a in enumerate(b)) % M
    W = sum((6*k+1)*a for k,a in enumerate(w)) % M
    U = (g*h - W) % M
    assert g % p == 0
    assert U % p**2 == 0
    assert (W - p) % p**2 == 0
    assert (g*h-p) % p**2 == 0
    return b, w, g, h, W, U


def reflected_tail(p, B):
    m = (p - 1)//6
    # A second route via finite-field terminated binomial coefficients.
    s0 = s1 = acc = 0
    b0 = 1
    d = 1
    for i in range(1,m+1):
        # b_i = 2^{-i} binom(m,i) binom(2m,i), because 1/6=-m,1/3=-2m in F_p.
        b0 = b0 * (m-i+1)*(2*m-i+1) * pow(2*i*i, -1,p) % p
        # d_i=2^(i-1)*(i-1)!^2/[(11/6)_(i-1)(5/3)_(i-1)]
        if i > 1:
            d = d * 36*(i-1)**2 * pow((6*i-1)*(3*i-1), -1,p) % p
        # Direct independent residue checks against p^3 series coefficients.
        assert B[i] % p == b0
        assert B[p-i] % p**2 == 0
        assert B[p-i] // p**2 == d * pow(10, -1, p) % p
        # Exact finite-field binomial checksum for small test points.
        if p <= 109:
            assert b0 == comb(m,i)*comb(2*m,i)*pow(2,-i,p)%p
            assert d == pow(2,i-1,p)*pow(comb(m+i,i-1)*comb(2*m+i,i-1),-1,p)%p
        s0 = (s0 + d)%p
        s1 = (s1 + i*d)%p
        acc = (acc + b0 * ((6*i+1)*s0-6*s1))%p
    return acc*pow(5,-1,p)%p


def direct_triangular_tail(p, B):
    m=(p-1)//6; M=p**3; acc=0
    for i in range(1,m+1):
        for j in range(p-i,p):
            # Both i,j admitted, one carries valuation zero, the other two.
            assert B[i] % p and B[j] % p**2 == 0
            acc += 2*(6*(i+j)+1)*B[i]*B[j]
    return (acc%M)//p**2


def main():
    samples = []
    count = w3 = 0
    for p in primes_under(5000):
        B, D, g, h, W, U = direct_quantities(p)
        t = reflected_tail(p,B)
        assert U // p**2 == t, (p, 'tail',U//p**2,t)
        assert (g*h-p)%(p**3)//p**2 == ((W-p)%(p**3)//p**2+t)%p
        if p in (13,19,37,43,61,67,109):
            assert t == direct_triangular_tail(p,B)
            # Degree <p exact Clausen coefficient, modulo p^3.
            M=p**3
            for n in range(p):
                cn=sum(B[k]*B[n-k] for k in range(n+1))%M
                assert cn == D[n],(p,n,cn,D[n])
            samples.append((p, ((g*h-p)%(p**3))//p**2,
                            ((W-p)%(p**3))//p**2, t))
        count += 1
        w3 += (W-p) % p**3 == 0
    print('ALL-PRIME IDENTITY SUPPORTED BY ALGEBRAIC DERIVATION; CHECKS BELOW ARE AUTHOR-SIDE')
    print(f'EXACT MODULAR REGRESSION: {count} target primes p<5000; {count} tail/Clausen bridge passes')
    print(f'FINITE OBSERVATION ONLY: W_p = p (mod p^3) on {w3}/{count} sampled target primes')
    print('p, Delta_p, (W_p-p)/p^2, cutoff_tail/p^2 (all modulo p):')
    for sample in samples:
        print(*sample)

if __name__=='__main__':
    main()
