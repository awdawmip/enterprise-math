"""D25 author-side exact finite Pfaff-band certificate for p == 13 (mod 24).

All computations are integer modular arithmetic; no floating point or libraries.
The script is a portable checker, not a native H0/B0 evaluator or formal proof.
"""
from __future__ import annotations


def primes_through(limit: int):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if sieve[d]:
            sieve[d * d: limit + 1: d] = b'\x00' * ((limit - d * d) // d + 1)
    return [p for p in range(13, limit + 1) if sieve[p] and p % 24 == 13]


def certificate(p: int):
    assert p % 24 == 13
    m = (p + 3) // 8
    a, b = 5 * m - 2, 7 * m - 3
    assert p == 8 * m - 3 and 0 < m < a < b < p
    modulus = p * p
    fact = [1] * (b + 1)
    for k in range(1, b + 1):
        fact[k] = fact[k - 1] * k % modulus
    invfact = [1] * (b + 1)
    invfact[b] = pow(fact[b], -1, modulus)
    for k in range(b, 0, -1):
        invfact[k - 1] = invfact[k] * k % modulus

    def choose(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * invfact[k] * invfact[n - k] % modulus

    inv8 = pow(8, -1, modulus)
    inv9 = pow(9, -1, modulus)
    zpower = 1
    P = dP = 0
    for k in range(a + 1):
        value = choose(a, k) * choose(b, k) * zpower % modulus
        P = (P + value) % modulus
        dP = (dP + 9 * k * value) % p
        zpower = zpower * inv9 % modulus

    harmonic = [0] * m
    for j in range(1, m):
        harmonic[j] = (harmonic[j - 1] + pow(j, -1, p)) % p

    Q0 = Q1 = Qedge = 0
    inv8power = 1
    for k in range(m):
        signed = inv8power if k % 2 == 0 else -inv8power
        base = choose(a, k) * choose(m - 1, k) * signed % modulus
        Q0 = (Q0 + base) % modulus
        harmonic_jet = harmonic[m - 1 - k] - harmonic[m - 1]
        Q1 = (Q1 + (base % p) * harmonic_jet) % p
        inv8power = inv8power * inv8 % modulus

    for k in range(m, a + 1):
        # The isolated factor (1-m+p)_{k} contributes exactly one p.
        edge_term = (1 if (m - 1) % 2 == 0 else -1)
        edge_term *= fact[m - 1] * choose(a, k) * fact[k - m]
        edge_term *= invfact[k] * pow(inv8, k, p)
        Qedge = (Qedge + edge_term) % p

    prefactor = pow(8 * inv9 % modulus, a, modulus)
    reconstruction = prefactor * (Q0 + p * (Q1 + Qedge)) % modulus
    assert P == reconstruction, (p, P, reconstruction)
    # P mod p = prefactor * Q0, so a unit-equivalent root is Q0 == 0.
    assert (P % p == 0) == (Q0 % p == 0)
    assert Q0 % p == 0, (p, 'short root not observed')
    assert P % p == 0, (p, 'original root not observed')
    quotient = prefactor % p * ((Q0 // p + Q1 + Qedge) % p) % p
    assert quotient == P // p, (p, quotient, P // p)
    # R(z)=sum (-1)^k C(a,k) C(m-1,k) z^k(1-z)^(m-1-k).
    # R(1/9)=(8/9)^(m-1) * Q0, P=(1-z)^((p+1)/2) R mod p.
    z, w = inv9 % p, (1 - inv9) % p
    dR = R = 0
    for k in range(m):
        term = (1 if k % 2 == 0 else -1) * choose(a, k) * choose(m - 1, k)
        term = term * pow(z, k, p) * pow(w, m - 1 - k, p) % p
        R = (R + term) % p
        dR = (dR + term * (k * pow(z, -1, p) - (m - 1 - k) * pow(w, -1, p))) % p
    factor = pow(w, (p + 1) // 2, p)
    assert P % p == factor * R % p
    assert dP == (factor * dR - ((p + 1) // 2) * pow(w, (p - 1) // 2, p) * R) % p
    return {
        'p': p, 'm': m, 'a': a, 'b': b,
        'P_over_p': P // p, 'Q0_over_p': Q0 // p,
        'Q1': Q1, 'Qedge': Qedge, 'prefactor_mod_p': prefactor % p,
        'R_mod_p': R, 'R_prime_mod_p': dR,
        'P_prime_mod_p': dP,
    }


def main():
    rows = [certificate(p) for p in primes_through(10000)]
    assert len(rows) == 157
    assert all(r['R_mod_p'] == 0 for r in rows)
    assert all(r['R_prime_mod_p'] != 0 for r in rows)
    for row in rows:
        if row['p'] in (13, 37, 61, 109, 373):
            print(row)
    print('PASS: 157/157 exact mod-p factor/derivative and mod-p^2 Pfaff-band checks; 157 simple roots')
    r = next(r for r in rows if r['p'] == 373)
    assert (r['Q0_over_p'], r['Q1'], r['Qedge'], r['P_over_p']) == (296, 112, 183, 75)
    assert (r['P_over_p'] + 66 + 232) % 373 == 0
    print('p=373: 180*(296+112+183)=75 (mod373), and 75+66+232=0 (mod373)')


if __name__ == '__main__':
    main()
