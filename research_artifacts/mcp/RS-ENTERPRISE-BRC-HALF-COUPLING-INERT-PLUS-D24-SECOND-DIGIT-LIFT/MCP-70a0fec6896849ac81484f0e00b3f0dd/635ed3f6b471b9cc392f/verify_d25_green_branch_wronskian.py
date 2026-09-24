from math import isqrt

# Exact finite regression only. The all-target identities are proved algebraically
# in d25_lift_green_branch_wronskian_20260924.md.

def primes_upto(n):
    s = [True] * (n + 1)
    s[0:2] = [False, False]
    for q in range(2, isqrt(n) + 1):
        if s[q]:
            for k in range(q*q, n + 1, q):
                s[k] = False
    return [q for q, ok in enumerate(s) if ok]

def inv(a, p):
    return pow(a % p, -1, p)

def check_prime(p):
    assert p % 24 in (13, 19)
    m = (p - 1) // 6

    # Low Gauss branch a_j = x_j mod p.
    a = [0] * (m + 1)
    a[0] = 1
    for j in range(m):
        a[j+1] = (a[j] * (m-j) * (2*m-j) *
                  inv(2*(j+1)*(j+1), p)) % p
        assert (2*(j+1)*(j+1)*a[j+1] -
                (m-j)*(2*m-j)*a[j]) % p == 0

    # Reflected boundary / negative-index Green branch.
    y = [0] * (m + 1)
    y[1] = inv(10, p)
    for r in range(1, m):
        y[r+1] = (y[r] * 2*r*r *
                  inv((r+m+1)*(r+2*m+1), p)) % p
        assert ((6*r+5)*(3*r+2)*y[r+1] -
                36*r*r*y[r]) % p == 0
        assert (2*r*r*y[r] -
                (r+m+1)*(r+2*m+1)*y[r+1]) % p == 0

    # Unique splice source: L_m G = -1/18.
    source = (-(m+1)*(2*m+1)*y[1]) % p
    assert source == (-inv(18, p)) % p

    # Original C_m double sum.
    c_double = 0
    for j in range(1, m + 1):
        for r in range(1, j + 1):
            c_double = (c_double +
                        (6*(j-r)+1)*a[j]*y[r]) % p

    # Positive-Laurent projection C_m = sum_h (6h+1)[z^h](A G).
    c_proj = 0
    for h in range(m):
        coeff = 0
        for r in range(1, m-h + 1):
            coeff = (coeff + a[h+r]*y[r]) % p
        c_proj = (c_proj + (6*h+1)*coeff) % p
    assert c_double == c_proj

    return c_double

def main():
    targets = [p for p in primes_upto(4999) if p % 24 in (13, 19)]
    failures = []
    for p in targets:
        try:
            check_prime(p)
        except Exception as exc:
            failures.append((p, repr(exc)))
    print('target_primes', len(targets))
    print('class13', sum(p % 24 == 13 for p in targets))
    print('class19', sum(p % 24 == 19 for p in targets))
    print('failures', len(failures))
    if failures:
        print(failures[:20])
        raise SystemExit(1)

if __name__ == '__main__':
    main()
