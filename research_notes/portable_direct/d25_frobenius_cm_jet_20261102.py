"""Exact finite certificates for D25 Frobenius/Teichmueller jet covariance.
Standard library only. Author-side experiment, not native H0/B0.
"""
from math import isqrt, comb
import hashlib

LIMIT = 3000
assert LIMIT >= 373
isprime = [True] * (LIMIT + 1)
isprime[0] = isprime[1] = False
for d in range(2, isqrt(LIMIT) + 1):
    if isprime[d]:
        for j in range(d * d, LIMIT + 1, d):
            isprime[j] = False


def jets_at_original_and_frobenius(p, denomin, numerators, power, c, base):
    """F=sum a[k] at z=base^-1, with each a[k] defined by integral recursion."""
    m = p * p
    assert denomin in (216, 2304)
    scale = pow(pow(base, -1, m), p - 1, m)
    a = 1
    f = [0] * 4
    fomega = [0] * 3
    for k in range(p):
        z = a * pow(scale, k, m) % m
        for j in range(4):
            f[j] = (f[j] + pow(k, j, m) * a) % m
            if j < 3:
                fomega[j] = (fomega[j] + pow(k, j, m) * z) % m
        if k + 1 < p:
            num = 1
            for r in numerators:
                for t in range(1, r + 1):
                    num = num * (r * k + t) % m
            a = a * num * pow(denomin * (k + 1) ** power, -1, m) % m
    assert f[0] % p == f[1] % p == 0
    q = (pow(pow(base, -1, m), p - 1, m) - 1) // p
    q %= p
    for j in range(3):
        assert (fomega[j] - f[j] - p * q * f[j + 1]) % m == 0
    Y = (f[0] + c * f[1]) % m
    Yomega = (fomega[0] + c * fomega[1]) % m
    Y1 = (f[1] + c * f[2]) % m
    assert Y % p == 0
    assert (Yomega - Y - p * q * Y1) % m == 0
    return {
        'f': f, 'q': q, 'Y': Y, 'Yomega': Yomega, 'Y1': Y1,
        'slope_canonical': (f[1] // p + q * f[2]) % p,
        'value_digit': f[0] // p,
        'weighted_shift': ((Yomega - Y) % m) // p
    }


def independent_binomial(p, denominator, weight):
    m = p * p
    total = 0
    for k in range(p):
        if denominator == 216:
            coeff = comb(2 * k, k) ** 2 * comb(3 * k, k)
        else:
            coeff = comb(2 * k, k) ** 2 * comb(4 * k, 2 * k)
        total = (total + (weight * k + 1) * coeff * pow(denominator, -k, m)) % m
    return total

rows = []
for p in range(5, LIMIT + 1):
    if not isprime[p] or p % 24 not in (13, 19):
        continue
    A = jets_at_original_and_frobenius(p, 216, (2, 3), 5, 6, 2)
    B = jets_at_original_and_frobenius(p, 2304, (4,), 4, 8, 9)
    f, g, m = A['f'], B['f'], p * p
    a1, a2 = (f[1] + 6 * f[2]) % m, (f[2] + 6 * f[3]) % m
    b1, b2 = (g[1] + 8 * g[2]) % m, (g[2] + 8 * g[3]) % m
    D = (16 * b2 * a1 - 3 * b1 * a2) % m
    assert D % p == 0
    correction = a1 * b1 * (
        4 * pow(3, -1, p) * A['q'] - 3 * pow(4, -1, p) * B['q']) % p
    rhs = (6 * a1 * B['slope_canonical']
           + 3 * pow(2, -1, p) * a1 * B['value_digit']
           - 8 * b1 * A['slope_canonical']
           - 2 * b1 * A['value_digit'] + correction) % p
    assert D // p == rhs
    anomaly = (A['weighted_shift'] - 2 * B['weighted_shift']) % p
    if p in (13, 19, 37, 61, 373, 1171):
        assert A['Y'] == independent_binomial(p, 216, 6)
        assert B['Y'] == independent_binomial(p, 2304, 8)
    rows.append((p, D // p, A['q'], B['q'], A['slope_canonical'],
                 B['slope_canonical'], correction, A['weighted_shift'],
                 B['weighted_shift'], anomaly))
assert len(rows) == 107
assert all(x[-1] != 0 for x in rows)  # finite-domain observation ONLY
assert next(x for x in rows if x[0] == 373) == (373, 365, 169, 144, 81, 34, 18, 112, 271, 316)
print('targets=', len(rows), 'all exact Frobenius/CM-jet relations PASS')
print('all 107 target-prime bridge-gauge anomalies nonzero: FINITE observation')
print('columns p,D/p,qA,qB,canon_A,canon_B,correction,shift_A,shift_B,anomaly')
for row in rows:
    if row[0] in (13, 19, 37, 61, 373, 1171):
        print(','.join(str(x) for x in row))
print('sha256_rows=', hashlib.sha256(''.join(','.join(str(v) for v in row) + '\n' for row in rows).encode()).hexdigest())
